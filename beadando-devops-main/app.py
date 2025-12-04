from flask import Flask, jsonify
import webbrowser
import threading
import time

app = Flask(__name__)

@app.route('/')
def hello():
    
    return jsonify({"message": "Üdvözletem, ez a beadando alkalmazasom!"})

def open_browser():
    """Open the browser after a short delay to ensure the server is ready"""
    time.sleep(1.5)  # Wait for the server to start
    webbrowser.open('http://127.0.0.1:8080')

if __name__ == '__main__':
    # Start browser in a separate thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    app.run(host='0.0.0.0', port=8080)
