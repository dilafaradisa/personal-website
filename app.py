from flask import Flask, render_template
import sys

app = Flask(__name__, template_folder='templates', static_folder='static')

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
