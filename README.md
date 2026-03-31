# Personal Website

A simple personal website built with Flask.

## Project Structure

```
├── app.py           # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile       # Docker configuration
├── test_app.py      # Tests
├── static/          # CSS and static files
│   └── style.css
└── templates/       # HTML templates
    ├── base.html
    └── index.html
```

## Setup

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd personal-website
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```
   Open `http://localhost:5000` in your browser.

## Deployment

See [`DEPLOY.md`](DEPLOY.md) for detailed deployment instructions using:
- **tmux** (simple, quick)
- **Docker** (recommended for production)

### Quick Deploy with Docker

```bash
docker build -t personal-website .
docker run -d --name webapp -p 127.0.0.1:2605:2605 personal-website
```

## Testing

Run tests with:
```bash
python -m pytest test_app.py
```

## Tech Stack

- **Framework:** Flask
- **Server:** Gunicorn
- **Containerization:** Docker
- **Tunneling:** Cloudflare Tunnel
