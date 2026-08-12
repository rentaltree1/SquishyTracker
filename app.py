from flask import Flask, render_template
import threading
from bot import run_discord_bot

app = Flask(__name__)

# Start the Discord bot in a background thread
bot_thread = threading.Thread(target=run_discord_bot)
bot_thread.start()

# This tells Flask to load your shiny new UI from the templates folder!
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
