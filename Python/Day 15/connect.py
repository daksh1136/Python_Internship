import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="internship",
    user="postgres",
    password="7788",
    port="1136"
)

print("Database connected successfully!")