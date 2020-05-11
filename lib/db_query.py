import psycopg2
import json

DBNAME = 'testdb'
HOST = 'localhost'
USER = 'dbuser'
PASSWORD = '123456'

#---------- DB Tab&Fun QUERYs ----------#
def callDBtableview(schema,table):
    conn = psycopg2.connect(dbname=DBNAME, host=HOST, user=USER, password=PASSWORD)
    cur = conn.cursor()
    cur.execute('SELECT * FROM "'+schema+'"."'+table+'" ')
    colnames = [desc[0] for desc in cur.description]
    
    results = []
    for row in cur.fetchall():
        results.append(dict(zip(colnames, row)))

    return results #json.dumps(results, indent=2)

def callDBfunction(schema,fun,params):
    conn = psycopg2.connect(dbname=DBNAME, host=HOST, user=USER, password=PASSWORD)
    cur = conn.cursor()
    cur.execute('SELECT * FROM "'+schema+'"."'+fun+'"('+params+')')
    colnames = [desc[0] for desc in cur.description]
    
    results = []
    for row in cur.fetchall():
        results.append(dict(zip(colnames, [str(r) for r in row])))

    return results #json.dumps(results, indent=2)