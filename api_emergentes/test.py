from flask import Flask, make_response, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

def db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = db_conn()
    sensors = conn.execute('SELECT * FROM sensor').fetchall()
    conn.close()
    return render_template('index.html', sensors=sensors)

'''
@app.route('/sensor', methods=['GET'])
def sensors():
    return make_response(jsonify(sensor), 200)

@app.route('/sensor', methods=['GET','PUT','DELETE'])
def sensor(location_id, sensor_id):
    if request.method == "GET":
        sensor_x = sensor.get(location_id, sensor_id, {})
        if sensor_x:
            return make_response(jsonify(sensor_x), 200)
        else:
            return make_response(jsonify(sensor_x), 404)
    elif request.method == "PUT":
        edit = request.json
        sensor[location_id,sensor_id] = edit
        sensor_x = sensor.get(location_id, sensor_id, {})
        return make_response(jsonify(sensor_x), 200)
    elif request.method == "DELETE":
        if location_id and sensor_id in sensor:
            del sensor[location_id,sensor_id]
        return make_response(jsonify(sensor_x))
'''

if __name__ == '__main__':
    app.run(debug=True)