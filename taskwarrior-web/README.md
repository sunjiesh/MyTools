# taskwarrior-web

一个基于 Taskwarrior（数据目录 `~/.task`）的简易 Web 系统：

- 后端：Python HTTP 服务（FastAPI），登录使用用户名密码（写死在配置），Session 使用 JWT（默认 10 分钟，可配置）
- 前端：Vue 3（Vite）

## 目录结构

- `backend/`: Python 后端
- `frontend/`: Vue 前端

## 后端启动

1. 安装依赖

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. 配置

复制并修改 `backend/config.yaml`（默认可直接使用）。

3. 启动

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## 前端启动

```bash
cd frontend
npm install
npm run dev
```

开发环境下默认后端 `http://localhost:8000`，前端 `http://localhost:5173`。

