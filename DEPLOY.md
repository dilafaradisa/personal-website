# Deployment Guide

## Prerequisites
- Python 3.10+ installed on VPS
- `python3-venv` package installed: `sudo apt install python3-venv`
- tmux installed on VPS: `sudo apt install tmux`
- Git installed on VPS: `sudo apt install git`

## Initial Setup (One Time)

```bash
# Clone the repo
cd ~
git clone https://github.com/dilafaradisa/personal-website.git personal-website
cd personal-website

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running with tmux

### Start the app in a detached tmux session
```bash
tmux new-session -d -s webapp gunicorn --bind 0.0.0.0:2605 --workers 4 app:app
```

This creates a session named `webapp` that runs in the background. You can close your terminal and the app stays running.

### Check if app is running
```bash
tmux list-sessions
```

### View the app logs (attach to session)
```bash
tmux attach -t webapp
```

To detach without killing the session, press `Ctrl+B` then `D`.

### Stop the app
```bash
tmux kill-session -t webapp
```

Or while attached (`tmux attach -t webapp`), press `Ctrl+C`.

## Quick Commands Cheat Sheet

| Command | Description |
|---------|-------------|
| `tmux new-session -d -s webapp gunicorn --bind 127.0.0.1:2605 --workers 4 app:app` | Start app in background |
| `tmux attach -t webapp` | View app logs |
| `tmux list-sessions` | List all tmux sessions |
| `tmux kill-session -t webapp` | Stop the app |
| `Ctrl+B` then `D` | Detach from session (while inside) |

---

## Alternative: Running with nohup

`nohup` (no hangup) is a simple way to run a process that survives terminal closure without additional tools.

### Start the app with nohup
```bash
cd ~/personal-website
source venv/bin/activate
nohup gunicorn --bind 0.0.0.0:2605 --workers 4 app:app > gunicorn.log 2>&1 &
```

This runs the app in the background and logs output to `gunicorn.log`. You can close your terminal and the app stays running.

### View logs
```bash
tail -f gunicorn.log
```

### Check if app is running
```bash
ps aux | grep gunicorn
```

### Stop the app
```bash
pkill gunicorn
```

Or kill by process ID:
```bash
kill <PID>
```

### nohup Commands Cheat Sheet

| Command | Description |
|---------|-------------|
| `nohup gunicorn --bind 0.0.0.0:2605 --workers 4 app:app > gunicorn.log 2>&1 &` | Start app in background |
| `tail -f gunicorn.log` | View logs (follow mode) |
| `ps aux \| grep gunicorn` | Check if running |
| `pkill gunicorn` | Stop the app |

### Advantages of nohup
- ✅ Simplest to use (no extra packages)
- ✅ Lightweight
- ✅ Works on any Unix-like system
- ✅ Good for quick deployments

### Disadvantages of nohup
- ⚠️ Doesn't auto-restart on failure
- ⚠️ Doesn't survive server reboot
- ⚠️ Harder to manage multiple instances
- ⚠️ No isolated environment

---

## Alternative: Running with Docker

Docker is recommended for production—it provides better isolation and easier management than tmux.

### Prerequisites
- Docker installed on VPS: `sudo apt install docker.io`
- Docker daemon running: `sudo systemctl start docker`
- Add your user to docker group (optional): `sudo usermod -aG docker $USER`

### Step 1: Create `Dockerfile` in your repo root

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:2605", "--workers", "4", "app:app"]
```

### Step 2: Build the Docker image
```bash
cd ~/personal-website
docker build -t personal-website .
```

### Step 3: Run the container
```bash
docker run -d --name dilafaradisa-personal-website -p 127.0.0.1:2605:2605 personal-website
```

The `-d` flag runs it in background (detached). The app stays running even if you close the terminal.

### Docker Commands

| Command | Description |
|---------|-------------|
| `docker build -t personal-website .` | Build the image |
| `docker run -d --name webapp -p 127.0.0.1:2605:2605 personal-website` | Start container in background |
| `docker ps` | List running containers |
| `docker logs -f webapp` | View container logs (follow mode) |
| `docker stop webapp` | Stop the container |
| `docker start webapp` | Restart the container |
| `docker rm webapp` | Remove stopped container |

### Advantages of Docker over tmux
- ✅ Isolated environment (no dependency conflicts)
- ✅ Easy to restart/update
- ✅ Portable (works anywhere Docker is installed)
- ✅ Better for production deployments
- ✅ Cleaner resource management
