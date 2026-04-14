import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anselemngo97$",
    database="taxify"
)

mycursor = mydb.cursor()

# Clear table first to avoid duplicate entry errors
mycursor.execute("TRUNCATE TABLE cabs")
mydb.commit()

sql = "INSERT INTO routes (id, route_name, start_location, end_location, cabs_assigned, amount, opening_time, closing_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = [
    ("01", "Ikeja", "Ikeja", "Oshodi", 5, 500, "08:00", "20:00"),
    ("02", "Oshodi", "Oshodi", "Cele", 20, 1500, "08:00", "20:00"),
    ("03", "Cele", "Cele", "lawson", 7, 400, "08:00", "20:00"),
    ("04", "Cele", "Cele", "Ago Palaceway", 7, 400, "08:00", "20:00"),
    ("05", "Cele", "Cele", "jakande", 5, 1000, "08:00", "20:00"),
    ("06", "Cele", "Cele", "Ikotun", 5, 1000, "08:00", "20:00"),
    ("07", "Cele", "Cele", "Yaba", 5, 1000, "08:00", "20:00"),
    ("08", "Ago Palaceway", "Ago Palaceway", "Mile 2", 6, 3000, "08:00", "20:00"),
    ("09", "Ago Palaceway", "Ago Palaceway", "Isolo", 6, 3000, "08:00", "20:00"),
    ("10", "Apple Junction", "Apple Junction", "Festac", 5, 500, "08:00", "20:00"),
    ("11", "Apple Junction", "Apple Junction", "Second Rainbow", 20, 1500, "08:00", "20:00")
    
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "cabs inserted successfully.")