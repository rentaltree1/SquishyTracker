from flask import Flask, render_template, request, jsonify
import threading
import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from bot import run_discord_bot

app = Flask(__name__)

# --- FIREBASE SETUP ---
firebase_json = os.getenv("FIREBASE_CREDENTIALS")
db = None

if firebase_json:
    try:
        cred_dict = json.loads(firebase_json)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        print("🔥 Firebase Successfully Connected!")
    except Exception as e:
        print("Error connecting to Firebase:", e)

# Start the Discord bot in a background thread
bot_thread = threading.Thread(target=run_discord_bot)
bot_thread.start()

@app.route('/')
def home():
    return render_template('index.html')

# --- THE API: This listens for your UI button clicks ---
@app.route('/notify', methods=['POST'])
def toggle_notify():
    if not db:
        return jsonify({"error": "Database not connected"}), 500
    
    data = request.json
    item_name = data.get("item")
    is_tracking = data.get("tracking")
    
    # Save or update the item in your Firebase Database
    doc_ref = db.collection("tracking").document(item_name)
    doc_ref.set({
        "name": item_name,
        "is_tracking": is_tracking,
        "store": "Target"
    }, merge=True)
    
    return jsonify({"success": True, "message": f"Updated database for {item_name}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
