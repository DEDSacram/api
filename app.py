import string
from flask import Flask, render_template
from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL
from flask import request
import json
from Calc_Score_neighbour import Calc_Score

from sqlalchemy import true
from flask import jsonify

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'akvarko'
 
mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def indexsss():
    pagetitle = "HomePage"
    return render_template("index.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")

@app.route('/scoregame/<promo>',methods=['GET', 'POST'])
def scoregame(promo):
    if promo:
        cursor = mysql.get_db().cursor()
        query_game = "INSERT INTO hra (promokod) VALUES (%s)"
        cursor.execute(query_game,(promo,))
        cursor = mysql.get_db().cursor()
        query_lastid = "SELECT ID FROM hra WHERE promokod = %s ORDER BY `datetime` DESC LIMIT 1"
        cursor.execute(query_lastid,(promo,))
        result = cursor.fetchall()
        lastid = result[0][0]
        for player in request.json:
            query_player = "INSERT INTO hrac (nazev,grid,skore,id_hry) VALUES (%s,%s,%s,%s)"
            cursor.execute(query_player, (player['name'],json.dumps(player['Grid']),Calc_Score(player['Grid']),lastid))
        return json.dumps(lastid)


@app.route('/games/<promo>', methods=['GET'])
def games(promo):
    cursor = mysql.get_db().cursor()
    query_string = "SELECT ID,datetime FROM hra WHERE promokod = %s ORDER BY `datetime` DESC"
    # query_string = "SELECT ID,datetime FROM hra WHERE promokod = %s"
    cursor.execute(query_string, (promo,))
    result = cursor.fetchall()
    cursor.close()

    if result:
        return json.dumps(result,default=str)
    return json.dumps(False)

@app.route('/players/<game>',methods=['GET'])
def score(game):
    cursor = mysql.get_db().cursor()
    query_string = "SELECT nazev,grid,skore FROM hrac WHERE id_hry = %s"
    cursor.execute(query_string, (game,))
    # result = cursor.fetchall()
    columns = cursor.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    cursor.close()
    
    if result:
        return json.dumps(result)
    return json.dumps(False)

@app.route('/signin/<promo>',methods=['GET'])
def index(promo):
    cursor = mysql.get_db().cursor()

    query_string = "SELECT * FROM promo WHERE promokod = %s"
    cursor.execute(query_string, (promo,))
    result = cursor.fetchall()
    cursor.close()
    if result:
        return json.dumps(True)
    return json.dumps(False)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=9000, debug=True)