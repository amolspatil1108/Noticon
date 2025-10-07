from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/services')
def get_services():
    services = [
        {
            "name": "WhatsApp",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"
        },
        {
            "name": "Telegram",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg"
        },
        {
            "name": "Outlook",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Microsoft_Office_Outlook_%282018–present%29.svg"
        },
        {
            "name": "Gmail",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png"
        }
    ]
    return jsonify(services)

if __name__ == '__main__':
    app.run(debug=True)