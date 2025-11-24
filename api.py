from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hospitals')
def get_hospitals():
    data = [
        {
            "id": 1,
            "name": "Bangalore City Hospital",
            "location": "Bangalore",
            "doctors": [
                {
                    "id": 101,
                    "name": "Dr. Rajesh Kumar",
                    "specialization": "Cardiologist",
                    "timeslots": ["10:00 AM", "11:00 AM", "03:00 PM"]
                },
                {
                    "id": 102,
                    "name": "Dr. Meera Sharma",
                    "specialization": "Dermatologist",
                    "timeslots": ["12:00 PM", "02:00 PM", "04:00 PM"]
                }
            ]
        },
        {
            "id": 2,
            "name": "Apollo Hospital Bangalore",
            "location": "Bangalore",
            "doctors": [
                {
                    "id": 201,
                    "name": "Dr. Arvind Rao",
                    "specialization": "Neurologist",
                    "timeslots": ["09:00 AM", "01:00 PM"]
                },
                {
                    "id": 202,
                    "name": "Dr. Sneha Iyer",
                    "specialization": "Pediatrician",
                    "timeslots": ["10:30 AM", "12:30 PM"]
                }
            ]
        }
    ]

    return jsonify(data)

if __name__ == '__main__':
    app.run()
