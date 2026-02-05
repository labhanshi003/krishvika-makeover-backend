from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/book", methods=["POST"])
def book():
    data = request.json

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO bookings (name, phone, service, date, time)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data["name"],
        data["phone"],
        data["service"],
        data["date"],
        data["time"]
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Appointment booked successfully!"})

if __name__ == "__main__":
    app.run()
