import os
import sys
from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

# --- CACHE BUSTING CODE START ---
@app.context_processor
def inject_dated_url():
    def dated_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            if filename:
                # Find the absolute path to the static file
                file_path = os.path.join(app.root_path, endpoint, filename)
                try:
                    # Append the last modified time as a query parameter '?v=16900000'
                    values['v'] = int(os.stat(file_path).st_mtime)
                except OSError:
                    pass # If file isn't found, just ignore and proceed
        return url_for(endpoint, **values)
    
    # Overrides the default url_for in Jinja templates
    return dict(url_for=dated_url_for)
# --- CACHE BUSTING CODE END ---

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering index.html: {e}", file=sys.stderr)
        return f"Error: {e}", 500

if __name__ == '__main__':
    print("Starting Flask app on http://localhost:2605")
    app.run(debug=True, host='0.0.0.0', port=2605, use_reloader=False)