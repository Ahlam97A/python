from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
import json
from flask import abort
from flask_json import FlaskJSON, JsonError
from passlib.hash import sha256_crypt
import hashlib
import binascii
import os
from flask_bcrypt import Bcrypt
import random
import string
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
bcrypt = Bcrypt(app)
app.config['CORS_HEADERS'] = 'Content-Type'

DATABASE11 = 'C:/Users/ahlam/OneDrive/Desktop/pizzatestdb.db'
DATABASE = 'C:/Users/ahlam/OneDrive/Desktop/Pits.sqlite'
conn = sql.connect(DATABASE)
print("Opened database successfully")
print(conn)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
@cross_origin()
def firt():
    return "ahlam"


@app.route('/pits', methods=['POST', 'GET'])
@cross_origin()
def a():
    if request.method == 'POST':
        data = request.get_json()
        type1 = data['min']
        print(type1)
        with sql.connect(DATABASE) as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            y="SELECT VehicleId,Latitude ,Longitude ,LastUpdate FROM PitsRecord where LastUpdate LIKE ? GROUP BY VehicleId ",('%'+str(type1)+'%')
            x = cur.execute("SELECT VehicleId,Latitude ,Longitude ,LastUpdate FROM PitsRecord where LastUpdate LIKE ? GROUP BY VehicleId",('%2019/07/07%'+'%'+str(type1)+'%',))
            rows = cur.fetchall()
            con.commit()
            record = jsonify(rows)
            x1 = json.dumps(rows)
            for x in rows:
                print(x)
            return x1

        msg = "error in select operation"
        return msg
    return "error"




@app.route('/static/img', methods=['POST', 'GET'])
@cross_origin()
def img():
    if request.method == 'POST':
    
        with sql.connect(DATABASE11) as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            x = cur.execute("SELECT id,image FROM images")
            rows = cur.fetchall()
            con.commit()
            record = jsonify(rows)
            x1 = json.dumps(rows)
            for x in rows:
                print(x)
            return x1

        msg = "error in select operation"
        return msg
    return "error"