<script setup>
import { computed, onMounted, ref } from 'vue'

const token = ref(localStorage.getItem('tw_token') || '')
const expiresMinutes = ref(Number(localStorage.getItem('tw_expires_minutes') || '10'))

const username = ref('')
const password = ref('')
const loginErr = ref('')
const loading = ref(false)

const newDesc = ref('')
const tasks = ref([])
const tasksErr = ref('')

const authed = computed(() => !!token.value)

async function api(path, opts = {}) {
  const headers = new Headers(opts.headers || {})
  headers.set('Content-Type', 'application/json')
  if (token.value) headers.set('Authorization', `Bearer ${token.value}`)

  const res = await fetch(path, { ...opts, headers })
  if (res.status === 401) {
    logout()
    throw new Error('unauthorized')
  }
  const text = await res.text()
  const data = text ? JSON.parse(text) : null
  if (!res.ok) throw new Error((data && data.detail) || `HTTP ${res.status}`)
  return data
}

function logout() {
  token.value = ''
  localStorage.removeItem('tw_token')
  localStorage.removeItem('tw_expires_minutes')
}

async function doLogin() {
  loginErr.value = ''
  loading.value = true
  try {
    const data = await api('/api/login', {
      method: 'POST',
      body: JSON.stringify({ username: username.value, password: password.value }),
    })
    token.value = data.access_token
    expiresMinutes.value = data.expires_minutes
    localStorage.setItem('tw_token', token.value)
    localStorage.setItem('tw_expires_minutes', String(expiresMinutes.value))
    await refresh()
  } catch (e) {
    loginErr.value = e?.message || String(e)
  } finally {
    loading.value = false
  }
}

async function refresh() {
  tasksErr.value = ''
  loading.value = true
  try {
    tasks.value = await api('/api/tasks')
  } catch (e) {
    tasksErr.value = e?.message || String(e)
  } finally {
    loading.value = false
  }
}

async function addTask() {
  if (!newDesc.value.trim()) return
  loading.value = true
  try {
    await api('/api/tasks', { method: 'POST', body: JSON.stringify({ description: newDesc.value }) })
    newDesc.value = ''
    await refresh()
  } catch (e) {
    tasksErr.value = e?.message || String(e)
  } finally {
    loading.value = false
  }
}

async function doneTask(id) {
  loading.value = true
  try {
    await api(`/api/tasks/${id}/done`, { method: 'POST' })
    await refresh()
  } catch (e) {
    tasksErr.value = e?.message || String(e)
  } finally {
    loading.value = false
  }
}

async function deleteTask(id) {
  loading.value = true
  try {
    await api(`/api/tasks/${id}`, { method: 'DELETE' })
    await refresh()
  } catch (e) {
    tasksErr.value = e?.message || String(e)
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  if (authed.value) await refresh()
})
</script>

<template>
  <div class="layout">
    <header class="topbar">
      <div class="brand">
        <div class="logo">TW</div>
        <div>
          <div class="title">Taskwarrior Web</div>
          <div class="sub">JWT session {{ expiresMinutes }} minutes</div>
        </div>
      </div>
      <div class="actions">
        <button v-if="authed" class="btn" @click="refresh" :disabled="loading">Refresh</button>
        <button v-if="authed" class="btn danger" @click="logout" :disabled="loading">Logout</button>
      </div>
    </header>

    <main class="card">
      <section v-if="!authed" class="stack">
        <h2>Login</h2>
        <div class="grid2">
          <label class="field">
            <span>Username</span>
            <input v-model="username" autocomplete="username" />
          </label>
          <label class="field">
            <span>Password</span>
            <input v-model="password" type="password" autocomplete="current-password" />
          </label>
        </div>
        <div class="row">
          <button class="btn primary" @click="doLogin" :disabled="loading">Login</button>
          <div class="muted">Config in <code>backend/config.yaml</code></div>
        </div>
        <p v-if="loginErr" class="err">{{ loginErr }}</p>
      </section>

      <section v-else class="stack">
        <h2>Tasks</h2>

        <div class="row">
          <input
            class="input"
            v-model="newDesc"
            placeholder="Add a task description…"
            @keyup.enter="addTask"
          />
          <button class="btn primary" @click="addTask" :disabled="loading">Add</button>
        </div>

        <p v-if="tasksErr" class="err">{{ tasksErr }}</p>

        <div v-if="tasks.length === 0" class="muted">No pending tasks.</div>

        <ul v-else class="list">
          <li v-for="t in tasks" :key="t.uuid" class="item">
            <div class="desc">
              <div class="descLine">{{ t.description }}</div>
              <div class="meta">
                <span v-if="t.id">#{{ t.id }}</span>
                <span v-if="t.project">project: {{ t.project }}</span>
                <span v-if="t.priority">pri: {{ t.priority }}</span>
              </div>
            </div>
            <div class="itemActions">
              <button class="btn" @click="doneTask(t.id)" :disabled="loading || !t.id">Done</button>
              <button class="btn danger" @click="deleteTask(t.id)" :disabled="loading || !t.id">
                Delete
              </button>
            </div>
          </li>
        </ul>
      </section>
    </main>
  </div>
</template>
