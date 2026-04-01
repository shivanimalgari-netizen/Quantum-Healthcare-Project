from flask import Flask, jsonify
import sqlite3
from encryption import generate_key, decrypt_data

app = Flask(__name__)

@app.route("/")
def home():
    return "Healthcare Secure API Running ✅"

@app.route("/data")
def get_data():
    conn = sqlite3.connect("healthcare.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()

    conn.close()

    return jsonify(data)

@app.route("/decrypt")
def decrypt_all():
    conn = sqlite3.connect("healthcare.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()

    conn.close()

    key = generate_key("securepassword123")

    decrypted_list = []

    for row in data:
        decrypted = decrypt_data(row[1], key)
        decrypted_list.append({
            "id": row[0],
            "data": decrypted
        })

    return jsonify(decrypted_list)

if __name__ == "__main__":
    app.run(debug=True)