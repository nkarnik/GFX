import pandas as pd
from pandas.io import sql
import requests
from sqlalchemy import create_engine
import json
from flaskext.mysql import MySQL
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

t1 = json.dumps( [ [ 1, 9], [2, 5 ], [ 3, 7] ]);


engine = create_engine('mysql://root:cms001@localhost/test', echo=True)
cnx = engine.raw_connection()
 
mysql = MySQL()
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cms001'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
@app.route("/")
def hello():
    return render_template("ly.html")


@app.route("/maptest")
def map():
    return render_template("map1.html")


@app.route("/gdv")
def gdv():
    return render_template("carto1.html")

@app.route("/corrs")
def corrs():
    return render_template("pcorrs.html")

@app.route("/apitest")
def apit():
    return requests.get('http://npk.cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20gdv911%20LIMIT%20100&api_key=dc5c3b904661342a4c03c73597984d5c0fd1d1c4').text

@app.route("/USDJPY", methods=['GET'])
def USDJPY():
    pair = 'USDJPY'
    username = 'root'
    password = 'cms001'
    cursor = mysql.connect().cursor()
#    cursor.execute("SELECT * from fx where a = 'AUD' and b = 'USD' order by a, b, day limit 1000")
    
    cursor.execute("SELECT * from fx where a = 'USD' and b = 'JPY' order by a, b, day limit 10000")


    data = cursor.fetchall()
    table = []
    for t in data:
        temp = []
        for a in t:
            temp.append(a)
        table.append(temp)

    data = json.dumps(table)

    
    ran = 150

    if data is None:
     return "Username or Password is wrong"
    else:
     #return render_template('FX.html', entries=entries)
     print t1, data
     #return render_template('FX.html', data=table)
     return render_template("mychart2.html", var=data, pair=pair, ran=ran)
#     return render_template("chart1.html")
     #return "Connected"


@app.route("/EURUSD", methods=['GET'])
def EURUSD():
    pair = 'EURUSD'
    username = 'root'
    password = 'cms001'
    cursor = mysql.connect().cursor()
#    cursor.execute("SELECT * from fx where a = 'AUD' and b = 'USD' order by a, b, day limit 1000")
    
    cursor.execute("SELECT * from fx where a = 'EUR' and b = 'USD' and day != 20010607 order by a, b, day limit 50000")


    data = cursor.fetchall()
    table = []
    for t in data:
        temp = []
        for a in t:
            temp.append(a)
        table.append(temp)

    data = json.dumps(table)

    
    ran = 2

    if data is None:
     return "Username or Password is wrong"
    else:
     #return render_template('FX.html', entries=entries)
     print t1, data
     #return render_template('FX.html', data=table)
     return render_template("mychart2.html", var=data, pair=pair, ran=ran)
#     return render_template("chart1.html")
     #return "Connected"


@app.route("/EURJPY", methods=['GET'])
def EURJPY():
    pair = 'EURJPY'
    username = 'root'
    password = 'cms001'
    cursor = mysql.connect().cursor()
#    cursor.execute("SELECT * from fx where a = 'AUD' and b = 'USD' order by a, b, day limit 1000")
    
    cursor.execute("SELECT * from fx where a = 'EUR' and b = 'JPY' and day != 20010607 order by a, b, day limit 50000")


    data = cursor.fetchall()
    table = []
    for t in data:
        temp = []
        for a in t:
            temp.append(a)
        table.append(temp)

    data = json.dumps(table)

    
    ran = 200

    if data is None:
     return "Username or Password is wrong"
    else:
     #return render_template('FX.html', entries=entries)
     print t1, data
     #return render_template('FX.html', data=table)
     return render_template("mychart2.html", var=data, pair=pair, ran=ran)

@app.route("/EURGD", methods=['GET'])
def EURGD():
    pair = 'EURGD'
    username = 'root'
    password = 'cms001'
    cursor = mysql.connect().cursor()
#    cursor.execute("SELECT * from fx where a = 'AUD' and b = 'USD' order by a, b, day limit 1000")
   

    cursor.execute("select day, sum(SumArticles)/norm from gdecon2 where (Actor1Code = 'CHE' or Actor2Code = 'CHE') and day > 20000101 group by day order by day limit 1000000")

    print 1

    data = cursor.fetchall()
    print 2
    print data
    table = []
    for t in data:
        temp = []
        for i, a in enumerate(t):
            if i == 1: temp.append(float(a))
            else: temp.append(a)
        table.append(temp)

    data = json.dumps(table)


    ran = 0.1

    if data is None:
     return "Username or Password is wrong"
    else:
     #return render_template('FX.html', entries=entries)
     print t1, data
     #return render_template('FX.html', data=table)
     return render_template("mychart2.html", var=data, pair=pair, ran=ran)



@app.route("/ALLUSD", methods=['GET'])
def ALLUSD():
    pair = 'USD'
    username = 'root'
    password = 'cms001'
    cursor = mysql.connect().cursor()

#    cursor.execute("SELECT * from fx where a = 'AUD' and b = 'USD' order by a, b, day limit 1000")
    
    sqlst = "SELECT * from fx where a = 'GBP' and b = 'USD' order by a, b, day limit 50000"
    cursor.execute(sqlst)
    #df = sql.read_sql(sqlst, cnx)

    """
    AUDUSD = df[(df.a == 'AUD') & (df.b == 'USD')]
    EURUSD = df[(df.a == 'EUR') & (df.b == 'USD')]
    GBPUSD = df[(df.a == 'GBP') & (df.b == 'USD')]
    USDCAD = df[(df.a == 'USD') & (df.b == 'CAD')]
    USDCHF = df[(df.a == 'USD') & (df.b == 'CHF')]
    USDJPY = df[(df.a == 'USD') & (df.b == 'JPY')]

    upairs = [AUDUSD, EURUSD, GBPUSD, USDCAD, USDCHF, USDJPY]
    """
    #for p in upairs: print p

    data = cursor.fetchall()
    #print df
    table = []
    for t in data:
        temp = []
        for a in t:
            temp.append(a)
        table.append(temp)

    data = json.dumps(table)

    
    ran = 2

    if data is None:
     return "Username or Password is wrong"
    else:
     #return render_template('FX.html', entries=entries)
     print t1, data
     #return render_template('FX.html', data=table)
     return render_template("mychart2.html", var=data, pair=pair, ran=ran)






if __name__ == "__main__":
    app.run(host='0.0.0.0')
