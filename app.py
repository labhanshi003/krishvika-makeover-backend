from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_db_connection

app = Flask(__name__)
CORS(app)

@app.route("/book", methods=["POST"])
def book_appointment():
    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO bookings (name, phone, service, date, time, message)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        data["name"],
        data["phone"],
        data["service"],
        data["date"],
        data["time"],
        data["message"]
    )

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Booking successful"}), 201

if __name__ == "__main__":
    app.run(debug=True)
