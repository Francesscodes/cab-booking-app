import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.environ.get("DB_PASSWORD"),
    database="taxify"
)