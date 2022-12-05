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

#Admin


#Admin crea Company
#Sirve
#POST params: admin_api_key, name
@app.route('/api/v1/create_company', methods=['Post'])
def acreate_company():
    admin_api_key = request.args.get("admin_api_key")

    conn = db_conn()
    admin = conn.execute('SELECT username FROM admin WHERE admin_api_key = ?', (admin_api_key,)).fetchone()
    conn.close()

    name = request.args.get("name") #New Company Name
    
    flag = 0
    if admin:
        flag = 1

    if flag:
        #crear company_api_key
        company_api_key = "c_" + str(name) + "_api_key"

        #insert
        conn = db_conn()
        conn.execute("INSERT INTO company(company_name, company_api_key) VALUES (?,?)", (name, company_api_key))
        conn.commit()
        conn.close()

        return "key:" + company_api_key + " " + str(admin), 201
    else:
        
        return "err: No se cuenta con permisos de Admin", 401

#Admin get all company
#Sirve
#GET All company_api_key
@app.route('/api/v1/aget_all_company', methods=['Get'])
def aget_all_company():
    admin_api_key = request.args.get("admin_api_key")

    conn = db_conn()
    admin = conn.execute('SELECT username FROM admin WHERE admin_api_key = ?', (admin_api_key,)).fetchone()
    conn.close()
    answer = []
    flag = 0
    if admin:
        flag = 1

    if flag:

        conn = db_conn()
        comp = conn.execute('SELECT * FROM company').fetchall()
        print(comp)
        conn.close()
        for i in comp:
            answer.append("ID: " + str((i['ID'])))
            answer.append("Company_name: " + str(i['company_name']))
            answer.append("Company_api_key: " + str(i['company_api_key']))


        #Fix return
        return str(answer), 201

    else:
   
        return "err: No se cuenta con permisos", 401


#Admin crea Location
#Sirve
#POST params: admin_api_key, name, country, city, meta, company_id
@app.route('/api/v1/acreate_location', methods=['Post'])
def acreate_location():
    admin_api_key = request.args.get("admin_api_key")

    name = request.args.get("location_name")
    country = request.args.get("location_country")
    city = request.args.get("location_city")
    meta = request.args.get("location_meta")
    company_id = request.args.get("company_id")

    conn = db_conn()
    admin = conn.execute('SELECT username FROM admin WHERE admin_api_key = ?', (admin_api_key,)).fetchone()
    conn.close()


    flag = 0
    if admin:
        flag = 1

    if flag:

        #insert
        conn = db_conn()
        conn.execute("INSERT INTO location(company_id, location_name, location_country, location_city, location_meta) VALUES (?,?,?,?,?)", (company_id, name, country, city, meta))
        conn.commit()
        conn.close()

        return "created: "+ str(name) + ": " + str(country) + ", " + str(city) + " " + str(meta), 201
    else:
        
        return "err: No se cuenta con permisos de Admin", 401

#Admin get all location
#Sirve
#GET params: admin_api_key
@app.route('/api/v1/aget_all_location', methods=['Get'])
def aget_all_location():

    admin_api_key = request.args.get("admin_api_key")

    conn = db_conn()
    admin = conn.execute('SELECT username FROM admin WHERE admin_api_key = ?', (admin_api_key,)).fetchone()
    conn.close()


    flag = 0
    if admin:
        flag = 1
    
    if flag:
        conn = db_conn()
        loc = conn.execute('SELECT * FROM location').fetchall()
        conn.close()
        answer = []
        for i in loc:
            answer.append("company_id: " + str(i['company_id']))
            answer.append("location_name: " + str(i['location_name']))
            answer.append("location_country: " + str(i['location_country']))
            answer.append("location_city: " + str(i['location_city']))
            answer.append("location_meta" + str(i['location_meta']))
            

        return str(answer), 201
    else:

        return "err: No se cuenta con permisos", 401



#########################################
#########################################
#########################################
#########################################


#Location

#Company crea Location
#Sirve
#POST params: company_api_key, name, country, city, meta
@app.route('/api/v1/create_location', methods=['Post'])
def create_location():
    company_api_key = request.args.get("company_api_key")

    name = request.args.get("location_name")
    country = request.args.get("location_country")
    city = request.args.get("location_city")
    meta = request.args.get("location_meta")


    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()


    flag = 0
    if compid:
        flag = 1

    if flag:

        #insert
        conn = db_conn()
        conn.execute("INSERT INTO location(company_id, location_name, location_country, location_city, location_meta) VALUES (?,?,?,?,?)", (compid[0], name, country, city, meta))
        conn.commit()
        conn.close()

        return "created", 201

    else:
        
        return "err: No se cuenta con permisos", 401


#Company get 1 location
#Sirve
#GET params: company_api_key, location_id
@app.route('/api/v1/get_location', methods=['Get'])
def get_location():

    company_api_key = request.args.get("company_api_key")
    location_id = request.args.get("location_id")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()


    flag = 0
    if compid:
        flag = 1
    
    if flag:
        conn = db_conn()
        loc = conn.execute('SELECT * FROM location WHERE location_id = ?', (location_id,)).fetchone()
        conn.close()
        
        answer = []
        if loc:
            answer.append("company_id: " + str(loc['company_id']))
            answer.append("location_name: " + str(loc['location_name']))
            answer.append("location_country: " + str(loc['location_country']))
            answer.append("location_city: " + str(loc['location_city']))
            answer.append("location_meta: " + str(loc['location_meta']))
            
            return str(answer), 201
        return "no location"
    else:

        return "err: No se cuenta con permisos", 401

#Company get all location
#Sirve
#GET params: company_api_key
@app.route('/api/v1/get_all_location', methods=['Get'])
def get_all_location():

    company_api_key = request.args.get("company_api_key")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()


    flag = 0
    if compid:
        flag = 1
    
    if flag:
        conn = db_conn()
        loc = conn.execute('SELECT * FROM location WHERE company_id = ?', (compid[0],)).fetchall()
        conn.close()
        answer = []
        for i in loc:
            answer.append("company_id: " + str(i['company_id']))
            answer.append("location_name: " + str(i['location_name']))
            answer.append("location_country: " + str(i['location_country']))
            answer.append("location_city: " + str(i['location_city']))
            answer.append("location_meta" + str(i['location_meta']))
            

        return str(answer), 201
    else:

        return "err: No se cuenta con permisos", 401


#Company update location
#Sirve
#UPDATE params: company_api_key, name, country, city,meta, company_id, location_id
@app.route('/api/v1/update_location', methods=['Put'])
def update_location():

    company_api_key = request.args.get("company_api_key")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()

    name = request.args.get("location_name") #New Company Name
    country = request.args.get("location_country")
    city = request.args.get("location_city")
    meta = request.args.get("location_meta")

    location_id = request.args.get("location_id")

    flag = 0
    if compid:
        flag = 1
    
    if flag:

        if name:
            conn = db_conn()
            compid = conn.execute('UPDATE location set location_name = ? WHERE location_id = ?', (name, location_id,))
            conn.commit()
            conn.close()

        if country:
            conn = db_conn()
            compid = conn.execute('UPDATE location set location_country = ? WHERE location_id = ?', (country, location_id,))
            conn.commit()
            conn.close()

        if city:
            conn = db_conn()
            compid = conn.execute('UPDATE location set location_city = ? WHERE location_id = ?', (city, location_id,))
            conn.commit()
            conn.close()

        if meta:
            conn = db_conn()
            compid = conn.execute('UPDATE location set location_meta = ? WHERE location_id = ?', (meta, location_id,))
            conn.commit()
            conn.close()

        return "updated", 201
    else:
        
        return "err: No se cuenta con permisos de Admin", 401

#Company delete location
#Sirve
#DELETE params: company_api_key, location_id
@app.route('/api/v1/delete_location', methods=['Delete'])
def delete_location():

    company_api_key = request.args.get("company_api_key")
    location_id = request.args.get("location_id")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()


    flag = 0
    if compid:
        flag = 1
    
    if flag:
        conn = db_conn()
        delet = conn.execute('DELETE FROM location WHERE location_id = ?', (location_id,)).fetchone()
        conn.commit()
        conn.close()
        return "daleted", 201
    else:
        
        return "err: No se cuenta con permisos", 401


#########################################
#########################################
#########################################
#########################################

#Sensor


#Company crea sensor
#Sirve
#POST params: company_api_key, location_id, sensor_name, sensor_category, sensor_meta
@app.route('/api/v1/create_sensor', methods=['Post'])
def create_sensor():

    company_api_key = request.args.get("company_api_key")

    location = request.args.get("location_id")
    name = request.args.get("sensor_name")
    category = request.args.get("sensor_category")
    meta = request.args.get("sensor_meta")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()

    flag = 0
    if compid:
        flag = 1

    if flag:
        #create key
        sensor_api_key = "s_" + name + "_api_key"
        #insert
        conn = db_conn()
        conn.execute("INSERT INTO sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?,?,?,?,?)", (location, name, category, meta, sensor_api_key))
        conn.commit()
        conn.close()
        print(sensor_api_key)
        return "created", 201

    else:
        
        return "err: No se cuenta con permisos", 401


#Company get 1 sensor
#
#GET params: company_api_key, sensor_id
@app.route('/api/v1/get_sensor', methods=['Get'])
def get_sensor():

    company_api_key = request.args.get("company_api_key")
    sensor_id = request.args.get("sensor_id")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()


    flag = 0
    if compid:
        flag = 1
    
    if flag:
        conn = db_conn()
        loc = conn.execute('SELECT * FROM sensor WHERE sensor_id = ?', (sensor_id,)).fetchone()
        conn.close()
        
        answer = []
        if loc:
            answer.append("location_id: "+ str(loc['location_id']))
            answer.append("sensor_id: "+ str(loc['sensor_id']))
            answer.append("sensor_name: " + str(loc['sensor_name']))
            answer.append("sensor_category: "+ str(loc['sensor_category']))
            answer.append("sensor_meta: " + str(loc['sensor_meta']))
            answer.append("sensor_api_key: " + str(loc['sensor_api_key']))

            return str(answer), 201
        return "no sensor"
    else:

        return "err: No se cuenta con permisos", 401


#Company get all sensor
#Sirve
#GET params: company_api_key
@app.route('/api/v1/get_all_sensor', methods=['Get'])
def get_all_sensor():

    company_api_key = request.args.get("company_api_key")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()


    flag = 0
    if compid:
        flag = 1
    
    if flag:
        conn = db_conn()
        loc = conn.execute('SELECT * FROM sensor WHERE location_id in (SELECT location_id from location WHERE company_id = ?)', (compid[0],)).fetchall()
        conn.close()
        answer = []
        for i in loc:

            answer.append("location_id: "+ str(i['location_id']))
            answer.append("sensor_id: "+ str(i['sensor_id']))
            answer.append("sensor_name: " + str(i['sensor_name']))
            answer.append("sensor_category: "+ str(i['sensor_category']))
            answer.append("sensor_meta: " + str(i['sensor_meta']))
            answer.append("sensor_api_key: " + str(i['sensor_api_key']))

        return str(answer), 201

    else:

        return "err: No se cuenta con permisos", 401



#Company update sensor
#Sirve
#UPDATE params: company_api_key, name, country, city,meta, company_id, sensor_id
@app.route('/api/v1/update_sensor', methods=['Put'])
def update_sensor():

    company_api_key = request.args.get("company_api_key")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()

    name = request.args.get("sensor_name") 
    category = request.args.get("sensor_category")
    meta = request.args.get("sensor_meta")

    sensor_id = request.args.get("sensor_id")

    flag = 0
    if compid:
        flag = 1
    
    if flag:

        if name:
            conn = db_conn()
            compid = conn.execute('UPDATE sensor set sensor_name = ? WHERE sensor_id = ?', (name, sensor_id,))
            conn.commit()
            conn.close()

        if category:
            conn = db_conn()
            compid = conn.execute('UPDATE sensor set sensor_category = ? WHERE sensor_id = ?', (category, sensor_id,))
            conn.commit()
            conn.close()

        if meta:
            conn = db_conn()
            compid = conn.execute('UPDATE sensor set sensor_meta = ? WHERE sensor_id = ?', (meta, sensor_id,))
            conn.commit()
            conn.close()

        return "updated", 201
    else:
        
        return "err: No se cuenta con permisos", 401


#Company delete sensor
#Sirve
#DELETE params: company_api_key, sensor_id
@app.route('/api/v1/delete_sensor', methods=['Delete'])
def delete_sensor():

    company_api_key = request.args.get("company_api_key")
    sensor_id = request.args.get("sensor_id")

    conn = db_conn()
    compid = conn.execute('SELECT ID FROM company WHERE company_api_key = ?', (company_api_key,)).fetchone()
    conn.close()


    flag = 0
    if compid:
        flag = 1
    
    if flag:
        conn = db_conn()
        delet = conn.execute('DELETE FROM sensor WHERE sensor_id = ?', (sensor_id,)).fetchone()
        conn.commit()
        conn.close()
        return "deleted", 201
    else:
        
        return "err: No se cuenta con permisos", 401


#########################################
#########################################
#########################################
#########################################

#Sensor Data

#Sensor crea sensor data
#
#POST params: sensor_api_key, date, medicion1, medicion2, medicion3
@app.route('/api/v1/create_sensordata', methods=['Post'])
def create_sensordata():

    sensor_api_key = request.args.get("sensor_api_key")

    date = request.args.get("date")
    medicion1 = request.args.get("medicion1")
    medicion2 = request.args.get("medicion2")
    medicion3 = request.args.get("medicion3")

    conn = db_conn()
    senid = conn.execute('SELECT sensor_id FROM sensor WHERE sensor_api_key = ?', (sensor_api_key,)).fetchone()
    conn.close()

    flag = 0
    if senid:
        flag = 1

    if flag:
        #insert
        
        if medicion2:

            if medicion3:
                conn = db_conn()
                conn.execute("INSERT INTO sensordata(sensor_id, date, medicion1, medicion2, medicion3) VALUES (?,?,?,?,?)", (senid[0], date, medicion1, medicion2, medicion3))
                conn.commit()
                conn.close()
            else:
                conn = db_conn()
                conn.execute("INSERT INTO sensordata(sensor_id, date, medicion1, medicion2) VALUES (?,?,?,?)", (senid[0], date, medicion1, medicion2))
                conn.commit()
                conn.close()

        else:
            conn = db_conn()
            conn.execute("INSERT INTO sensordata(sensor_id, date, medicion1) VALUES (?,?,?)", (senid[0], date, medicion1))
            conn.commit()
            conn.close()

        
        return "created", 201

    else:
        
        return "err: No se cuenta con dicho sensor", 400



#Sensor get 1 sensordata
#Sirve
#GET params: sensor_api_key, sensordata_id
@app.route('/api/v1/get_sensordata', methods=['Get'])
def get_sensordata():

    sensor_api_key = request.args.get("sensor_api_key")
    sensordata_id = request.args.get("sensordata_id")

    conn = db_conn()
    senid = conn.execute('SELECT sensor_id FROM sensor WHERE sensor_api_key = ?', (sensor_api_key,)).fetchone()
    conn.close()


    flag = 0
    if senid:
        flag = 1
    
    if flag:
        conn = db_conn()
        loc = conn.execute('SELECT * FROM sensordata WHERE ID = ?', (sensordata_id,)).fetchone()
        conn.close()
        answer = []
        if loc:
            for i in loc:
                answer.append(i)

            return str(answer), 201
        return "no data", 400
    else:

        return "err: No se cuenta con permisos", 401

#Sensor get all sensordata
#Sirve
#GET params: sensor_api_key
@app.route('/api/v1/get_all_sensordata', methods=['Get'])
def get_all_sensordata():

    sensor_api_key = request.args.get("sensor_api_key")


    conn = db_conn()
    senid = conn.execute('SELECT sensor_id FROM sensor WHERE sensor_api_key = ?', (sensor_api_key,)).fetchone()
    conn.close()


    flag = 0
    if senid:
        flag = 1
    
    if flag:
        conn = db_conn()
        loc = conn.execute('SELECT * FROM sensordata WHERE sensor_id = ?', (senid[0],)).fetchall()
        conn.close()
        answer = []
        if loc:
            for i in loc:
                answer.append("ID: " + str(i['ID']))
                answer.append("date: " + str(i['date']))
                answer.append("medicion1 :" + str(i['medicion1']))
                answer.append("medicion2: " + str(i['medicion2']))
                answer.append("medicion3: " + str(i['medicion3']))

            return str(answer), 201
        return "no sensor", 400
    else:

        return "err: No se cuenta con permisos", 401

#sensor update sensordata
#Sirve
#UPDATE params: sensor_api_key, date, medicion1, medicion2, medicion3, sensordata_id
@app.route('/api/v1/update_sensor', methods=['Put'])
def update_sensordata():

    sensor_api_key = request.args.get("sensor_api_key")
    
    date = request.args.get("date")
    medicion1 = request.args.get("medicion1")
    medicion2 = request.args.get("medicion2")
    medicion3 = request.args.get("medicion3")
    sensordata_id = request.args.get("sensordata_id")

    conn = db_conn()
    senid = conn.execute('SELECT ID FROM sensor WHERE sensor_api_key = ?', (sensor_api_key,)).fetchone()
    conn.close()

    flag = 0
    if senid:
        flag = 1
    
    if flag:

        if date:
            conn = db_conn()
            senid = conn.execute('UPDATE sensordata set date = ? WHERE ID = ?', (date, sensordata_id,))
            conn.commit()
            conn.close()

        if medicion1:
            conn = db_conn()
            senid = conn.execute('UPDATE sensordata set medicion1 = ? WHERE ID = ?', (medicion1, sensordata_id,))
            conn.commit()
            conn.close()

        if medicion2:
            conn = db_conn()
            senid = conn.execute('UPDATE sensordata set medicion2 = ? WHERE ID = ?', (medicion2, sensordata_id,))
            conn.commit()
            conn.close()
        
        if medicion3:
            conn = db_conn()
            senid = conn.execute('UPDATE sensordata set medicion3 = ? WHERE ID = ?', (medicion3, sensordata_id,))
            conn.commit()
            conn.close()


        return "updated", 201
    else:
        
        return "err: No se cuenta con permisos", 401


#sensor delete sensor
#Sirve
#DELETE params: sensor_api_key, sensordata_id
@app.route('/api/v1/delete_sensordata', methods=['Delete'])
def delete_sensordata():

    sensor_api_key = request.args.get("sensor_api_key")
    sensordata_id = request.args.get("sensordata_id")

    conn = db_conn()
    senid = conn.execute('SELECT ID FROM sensor WHERE sensor_api_key = ?', (sensor_api_key,)).fetchone()
    conn.close()


    flag = 0
    if senid:
        flag = 1
    
    if flag:
        conn = db_conn()
        delet = conn.execute('DELETE FROM sensordata WHERE ID = ?', (sensordata_id,)).fetchone()
        conn.commit()
        conn.close()
        return "deleted", 201
    else:
        
        return "err: No se cuenta con permisos", 401



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
    app.run(host = '0.0.0.0', debug=True)