import sqlite3, os, psycopg2
from flask import Flask, g, jsonify, send_file, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
DATABASE = 'student_fingerprint.db'
LOG_DATABASE = 'authentication_log.db'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = ['http://localhost*', 'https://jacobianproject.vercel.app*']
cors = CORS(app, origins=['http://localhost*', 'https://jacobianproject.vercel.app'], allow_headers=['Content-Type'])
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = psycopg2.connect(os.environ['DATABASE_URL'])
    return db
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
    log_db = getattr(g, '_log_database', None)
    if log_db is not None:
        log_db.close()
def jsonify_results(result):
    print(result)
    res = dict()
    res['id'] = result[0]
    res['fName'] = result[1]
    res['surname'] = result[2]
    res['registration'] = result[3]
    res['fingerprint_position'] = result[4]
    res['active'] = result[5]
    return res
def jsonify_logresults(result):
    print(result)
    res = dict()
    res['id'] = result[0]
    res['fName'] = result[1]
    res['surname'] = result[2]
    res['registration'] = result[3]
    res['fingerprint_position'] = result[4]
    res['timestamp'] = result[5]
    return res
@app.route('/')
def status1():
    return 'ok'
@app.route('/status')
def status():
    return 'ok'
@app.route('/create/my/db')
def create():
    query = '''CREATE table authenticationLog(id INTEGER PRIMARY KEY,
                                              fName TEXT NOT NULL,
                                              surname TEXT NOT NULL,
                                              registration TEXT NOT NULL,
                                              fingerprint_position INTEGER NOT NULL,
                                              timestamp datetime NOT NULL)'''
    try:
        c = get_db().cursor()
        c.execute(query)
        get_db().commit()
        c.close()
        return "Success"
    except Exception as e:
        return f"{e}"
@app.route('/getLogDB')
def return_log_db():
    return send_file(LOG_DATABASE)
@app.route('/getLogs')
def get_logs():
    c = get_db().cursor()
    c.execute("SELECT * from authenticationLog")
    results = c.fetchall()
    mylist = []
    for i in results:
        mylist.append(jsonify_logresults(i))
    return jsonify(mylist)

@app.route('/addLog', methods=['POST'])
def addLog():
    try:
        data = request.get_json()
        print(data)
        fname = data['fName']
        surname = data['surname']
        position = int(data['fingerprint_position'])
        registration = data['registration']
        timestamp = data['timestamp']
        query = "INSERT into authenticationLog (fName, surname, registration, fingerprint_position, time_stamp) VALUES ('{}', '{}', '{}', {}, '{}')".format(fname, surname, registration, position, timestamp)        
        db = get_db()
        c = db.cursor()
        c.execute(query)
        db.commit()
        c.close()
        return "logged!"
    except Exception as e:
        print(e)
        return f"{e}"


@app.route('/addRecords', methods=['POST', 'OPTIONS'])
@cross_origin(headers=['Content-Type'])
def addRecords():
    try:
        data = request.get_json()
        fname = data['fName']
        surname = data['surname']
        position = int(data['fingerprint_position'])
        registration = data['registration']
        active = 1
        query = "INSERT into students (fName, surname, registration, fingerprint_position, active) VALUES ('{}', '{}', '{}', {}, {})".format(fname, surname, registration, position, active)
        c = get_db().cursor()
        c.execute(query)
        get_db().commit()
        c.close()
    except Exception as e:
        return f"{e}"
    return 'Inserted!'

@app.route('/getAll')
def getAll():
    c = get_db().cursor()
    c.execute('SELECT * FROM students')
    results = c.fetchall()
    mylist = []
    for i in results:
        mylist.append(jsonify_results(i))
    return jsonify(mylist)

@app.route('/getReport')
def getReport():
    return 'getReport'
@app.route('/getDatabase')
def getDatabase():
    return send_file(DATABASE)
if __name__ == '__main__':
    try:
        if os.environ['PORT']:
            port_run = os.environ['PORT']
        else:
            port_run = 5000
    except KeyError:
        port_run = 5000
    #print(app.config)
    app.run(port=port_run, host='0.0.0.0')
