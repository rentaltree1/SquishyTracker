from flask import Flask
import threading
from bot import run_discord_bot

app = Flask(__name__)

# This is what visitors see when they visit your website URL
@app.route('/')
def home():
    return """
    <h1>Squishy Tracker Dashboard</h1>
    <p>The Discord bot is running successfully in the background!</p>
    """

if __name__ == '__main__':
    # Start the Discord bot in a background thread
    bot_thread = threading.Thread(target=run_discord_bot)
    bot_thread.start()
    
    # Start the web server
    app.run(host='0.0.0.0', port=5000)