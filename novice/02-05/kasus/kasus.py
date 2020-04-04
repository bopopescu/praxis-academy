import mysql.connector

db = mysql.connector.connect(
    host="192.168.1.91",
    user="danayoga",
    passwd="mastur",
    database="kasus0205"
)

cursor = db.cursor()
sql = "SELECT \
    movie.movie_rented \
    FROM namesaddress \
    INNER JOIN movie ON namesaddress.membership_id = movie.membership_id \
    WHERE namesaddress.full_names='Janet_Jones'"

cursor.execute(sql)
results = cursor.fetchall()

print("Janet Jones rent:")
for data in results:
    print(data)

