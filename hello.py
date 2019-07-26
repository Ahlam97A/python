from flask import Flask, render_template, request,jsonify
import sqlite3 as sql
import json
from flask import abort
from flask_json import FlaskJSON, JsonError
from passlib.hash import sha256_crypt
import hashlib, binascii, os
from flask_bcrypt import Bcrypt
import random
import string
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
bcrypt = Bcrypt(app)
app.config['CORS_HEADERS'] = 'Content-Type'

DATABASE = 'C:/Users/ahlam/OneDrive/Desktop/pizzatestdb.db'
conn = sql.connect(DATABASE)
print ("Opened database successfully")

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
 
@app.route('/addrec',methods = ['POST', 'GET'])
@cross_origin()
def addrec():
    if request.method == 'POST':
        try:
            data = request.get_json()
            #type1 = data.size
            #size = data.qaun   
            #data1=request.data
            #res=data1.decode('utf-8')
            result= data
            with sql.connect(DATABASE) as con:
                type1 = result["sel_s"]
                qaun = result["qaun"]
                size=result["size"]
                cur = con.cursor()          
                x=cur.execute("INSERT INTO order_pizza (type_pizza,size,quantity) VALUES (?,?,?)",(type1,size,qaun) )
                con.commit()
                
                record = json.dumps(result)
               
                return json.dumps(data)
        except:       
            msg = "error in insert operation"
            return msg



@app.route('/feedback',methods = ['POST', 'GET'])
@cross_origin()
def feedback():
    if request.method == 'POST':
        try:
            data = request.get_json()
            #type1 = data.size
            #size = data.qaun   
            #data1=request.data
            #res=data1.decode('utf-8')
            result= data
            with sql.connect(DATABASE) as con:
                id = result["sel_s"]
                feedback = result["qaun"]
               
                cur = con.cursor()          
                x=cur.execute("INSERT INTO feedback (id,feedback) VALUES (?,?)",(id,feedback,) )
                con.commit()
                
                record = json.dumps(result)
               
                return json.dumps(data)
        except:       
            msg = "error in insert operation"
            return msg



@app.route('/order',methods = ['POST'])
@cross_origin()
def order():
    if request.method == 'POST':
        try:
            #data = request.get_json()
         
            #result= data
            with sql.connect(DATABASE) as con:
                con.row_factory = dict_factory
                cur = con.cursor()          
                x=cur.execute('select * from order_pizza' )
                rows = cur.fetchall(); 
                con.commit()
                
                record = jsonify(rows)  
                x1=json.dumps(rows)    
                for x in rows:
                    print(x)   
                return x1
        except:       
            msg = "error in select operation"
            return msg



@app.route('/search',methods = ['POST'])
@cross_origin()
def search1():
    if request.method == 'POST':
        try:
            with sql.connect(DATABASE) as con:
                con.row_factory = dict_factory
                cur = con.cursor()          
                x=cur.execute('select * from order_pizza' )
                rows = cur.fetchall(); 
                con.commit()
                
                record = jsonify(rows)  
                x1=json.dumps(rows)    
                for x in rows:
                    print(x)   
                return x1
        except:       
            msg = "error in select operation"
            return msg


@app.route('/search2',methods = ['GET'])
@cross_origin()
def search2():
    username = request.args.get('query')
   
    try:
        data = request.get_json()
        #search = data["search"]
        username = request.args.get('query','')
            
        with sql.connect(DATABASE) as con:
                
            con.row_factory = dict_factory
                
            cur = con.cursor()          
            x=cur.execute('select * from order_pizza where type_pizza=?' ,(username,))
            rows = cur.fetchall(); 
            con.commit() 
            record = jsonify(rows)  
            x1=json.dumps(rows)    
             
            return x1
    except:       
        msg = "error in select operation"
        return msg

@app.route('/image',methods = ['POST'])
@cross_origin()
def photo():
    if request.method == 'POST':
        try:
            #data = request.get_json()
         
            #result= data
            with sql.connect(DATABASE) as con:
                con.row_factory = dict_factory
                curr = con.cursor()          
                x=curr.execute('select img,id,descr from admin' )
                rows = curr.fetchall() 
                con.commit()
                
                record = jsonify(rows)  
                x1=json.dumps(rows)           
                return x1
        except:       
            msg = "error in select operation"
            return msg


@app.route('/img11',methods = ['POST'])
@cross_origin()
def img11():
    if request.method == 'POST':
        try:
            #data = request.get_json()
         
            #result= data
            with sql.connect(DATABASE) as con:
                con.row_factory = dict_factory
                curr = con.cursor()          
                x=curr.execute('select image,id,name from images')
                rows = curr.fetchall() 
                con.commit()
                
                record = jsonify(rows)  
                x1=json.dumps(rows)           
                return x1
        except:       
            msg = "error in select operation"
            return json.dumps(msg)


@app.route('/login',methods = ['POST'])
@cross_origin()
def sub():
    if request.method == 'POST':
        try:           
            data = request.get_json()
            #type1 = data.size
            #size = data.qaun   
            #data1=request.data
            #res=data1.decode('utf-8')
            result= data
            with sql.connect(DATABASE) as con:
                #con.row_factory = dict_factory              
                name = result["name"]
                password = result["password"]  
                cur = con.cursor() 
                pw_hash = bcrypt.generate_password_hash(password)               
                #x=cur.execute('select * from login WHERE username =? AND password11=?',(name,password))
                x=cur.execute('select * from login  WHERE username =?',(name,))
                w=randomword(50)
                rows = cur.fetchall() 
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    becrypt=bcrypt.check_password_hash(dbPass, password) 
                    if becrypt :                        
                        con.commit()
                        insert=cur.execute("INSERT INTO token (user,passward,token) VALUES (?,?,?)",(name,password,w) )
                        con.commit()

                
                        record = jsonify(rows)  
                        x1=json.dumps(rows)                            
                        return json.dumps({"token":w})    
                    else:
                        return json.dumps({"error":"error"}) 

                return  abort(404)
        except:       
            msg = "error in select operation"
            return   abort(404)


@app.route('/logout',methods = ['POST'])
@cross_origin()
def logout():
    if request.method == 'POST':
        try:           
          
            with sql.connect(DATABASE) as con:
                cur = con.cursor() 
                            
                #x=cur.execute('select * from login WHERE username =? AND password11=?',(name,password))
                x=cur.execute('select * from login ')
                w=randomword(50)
                rows = cur.fetchall() 
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    becrypt=bcrypt.check_password_hash(dbPass, 'ahlam') 
                    if becrypt :                        
                        con.commit()
                        insert=cur.execute("DELETE FROM token WHERE user='ahlam'" )
                        con.commit()

                
                        record = jsonify(rows)  
                        x1=json.dumps(rows)                            
                        return x1
                    else:
                        return abort(404)
        except:       
            msg = "error in select operation"
            return   abort(404)

def randomword(length=50):
   letters = string.ascii_lowercase +string.digits + string.ascii_uppercase
   return ''.join(random.choice(letters) for i in range(length))

if __name__ == '__main__':
    app.run()
