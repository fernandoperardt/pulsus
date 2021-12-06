import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()


create_table = "CREATE TABLE IF NOT EXISTS device (id INTEGER PRIMARY KEY, deviceid text, data date)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS nome (id INTEGER PRIMARY KEY, device_id INTERGER, nome text, data date, FOREIGN KEY (device_id) REFERENCES device(id))"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS localizacao (id INTEGER PRIMARY KEY,  device_id INTERGER, longitude float(10, 8), latitude float(10, 8),  data date, FOREIGN KEY (device_id) REFERENCES device(id) )"
cursor.execute(create_table)



connection.commit()

connection.close()