from flask import Flask, request, jsonify
import hmac
import hashlib
import os

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    # Process webhook data
    data = request.json
    app.logger.info(f"Received webhook data: {data}")

    # Add your webhook processing logic here

    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
