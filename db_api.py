import sqlite3

db_lookup = {
			'tcs' : '/home/meghna/tcs_project/db/tcs.db'
}

def sql_execute(cmd, dbname='tcs', fetch=None):
	conn = sqlite3.connect(db_lookup[dbname])

	try:
		if cmd!= None:
			out=conn.execute(cmd)
			if fetch == 'all':
				data=out.fetchall()
			elif fetch == 'one':
				data=out.fetchone()

			if not cmd.upper().startswith('SELECT'):
				conn.commit()
	except Exception as e:
		raise e		
	finally:	
		conn.close()

	if fetch:
		return data


### Select
# cmd = '''SELECT * from users
#  				  WHERE city='Amsterdam';'''
# res=sql_execute(cmd, fetch='one')
# print(res)

### Insert
# cmd = '''INSERT INTO users (firstname,lastname,age,company,city)
#  				VALUES ('Robin','Williams', 40, 'XYZ', 'Amsterdam'),
#  				('Charlie','Munger', 45, 'ABC', 'Belgium');'''
# sql_execute(cmd)


### Update
# cmd = ''' UPDATE bank_customers SET name = 'Tanuj'
# 			WHERE name = 'TANUJ';'''
# sql_execute('robo.db', cmd)


### Create Table
# cmd = '''CREATE TABLE users (
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
# 	firstname TEXT NOT NULL,
# 	lastname TEXT,
#  	age INTEGER,
#  	company TEXT,
#  	city TEXT,
#  	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#  	);'''

#sql_execute(cmd=None)
#print ("Table created successfully");
