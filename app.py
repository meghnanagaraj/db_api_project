from flask import Flask, request, jsonify, render_template
from db_api import sql_execute
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",user_name=os.getenv("USER"),table_name='<table_name>',column_details='<column_name>=<value>')

@app.route(f"/<dbname>/<table_name>")
def get_data(dbname,table_name):
    args = request.args
    #print('$$$$$$$$',args)

    ##Fetch Coloumn Names
    cmd = f"select name from pragma_table_info('{table_name}')"

    result = sql_execute(cmd, fetch='all')
    if not result:
        return f"<p>Table '{table_name}' doesn't exists!</p>"

    column_name = [item[0] for item in result]

    ##Fetchng data
    cmd = f'SELECT {(",").join(column_name[:])} from {table_name}'

    if args:
        cmd += ' where '
        flag = False
        for k,v in args.items():
            if flag:
                cmd += " and "
            v = tuple(v.split(","))
            cmd += f"{k}='{v[0]}'" if len(v)==1 else f"{k} in {v}"
            flag = True

    print('#### QUERY IS ####',cmd)
    try:
        result=sql_execute(cmd,fetch='all')
        result = [dict(zip(column_name, each_res)) for each_res in result]
        return jsonify(result)
    except Exception as e:
        return f"<p>Error: {e}</p>"
