import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anselemngo97$",
    database="taxify"
)

mycursor = mydb.cursor()

sql = "INSERT INTO cabs (vehicle_name, cab_id, plate_number, route, vehicle_colour) VALUES (%s, %s, %s, %s, %s)"

val = [
    ("Toyota Corolla",   1, "Eky-918", "Ago Palaceway", "Blue"),
    ("Lexus 350",        2, "fes-919", "Oshodi",        "Red"),
    ("Mazda CX-5",       3, "ikr-920", "Ikotun",        "Green"),
    ("Audi A4",          4, "fes-921", "Festac",        "Yellow"),
    ("BMW",              5, "iky-922", "Ikeja",         "Black"),
    ("Honda Civic",      6, "iky-923", "Agege",         "White"),
    ("Sienna",           7, "Epe-924", "Surulere",      "Gray"),
    ("Range Rover",      8, "Epe-925", "Yaba",          "Silver"),
    ("Mercedes-Benz",    9, "Epe-926", "Mile 2",        "Maroon"),
    ("Hyundai Elantra", 10, "Epe-927", "Alaba",         "Purple"),
    ("Suzuki",            14, "Epe-924", "Jakande",       "Gray"),
    ("Toyota Camry",      15, "Eky-948", "Ajegunle",      "Blue"),
    ("Lexus 300",         16, "fes-910", "Oshodi",        "Red"),
    ("Toyota Prius",      17, "ikr-950", "Ago Palaceway", "Green"),
    ("Mercedes C-class",  18, "fes-901", "Mile 2",        "Yellow"),
    ("Toyota Highlander", 19, "iky-927", "Ikeja",         "Black"),
    ("Honda Accord",      20, "iky-926", "Mushin",        "White"),
    ("Tesla Model S",     21, "Epe-924", "Surulere",      "Gray")
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "cabs inserted successfully.")
