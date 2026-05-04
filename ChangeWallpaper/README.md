## ChangeWallpaper

一个桌面壁纸替换脚本，支持从 Bing 抓取图片并更换桌面壁纸。

### 功能

- **按时间间隔更换**：`run` 子命令循环运行
- **手动触发更换**：`once` 子命令立即更换
- **图片目录可配置**：`config.json` 的 `image_dir`
- **分辨率要求 2K+**：通过 `min_width/min_height` 校验（依赖 Pillow）
- **Linux 桌面支持**
  - GNOME/Ubuntu 等：`gsettings`
  - X11 兜底：安装 `feh` 后可用（Wayland 下建议用 GNOME 的 `gsettings`）

### 安装依赖

在 `ChangeWallpaper/` 目录执行：

```bash
python3 -m pip install -r requirements.txt
```

### 配置

复制示例配置：

```bash
cp config.example.json config.json
```

然后按需修改 `image_dir`、`market`、`interval_seconds` 等字段。

### 使用

手动更换一次：

```bash
python3 -m ChangeWallpaper -c ChangeWallpaper/config.json once
```

定时更换（每 30 分钟）：

```bash
python3 -m ChangeWallpaper -c ChangeWallpaper/config.json run --interval 30m
```

临时覆盖图片目录：

```bash
python3 -m ChangeWallpaper -c ChangeWallpaper/config.json --image-dir ~/Pictures/wallpapers once
```

