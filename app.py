from flask import Flask
import threading
from bot import run_discord_bot

app = Flask(__name__)

# We moved this up here so Render actually runs it!
bot_thread = threading.Thread(target=run_discord_bot)
bot_thread.start()

@app.route('/')
def home():
    return """
    <h1>Squishy Tracker Dashboard</h1>
    <p>The Discord bot is running successfully in the background!</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
