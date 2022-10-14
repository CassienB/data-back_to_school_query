# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/school.sqlite')
db = conn.cursor()



def students_from_city(db, city):
    """return a list of students from a specific city"""
    query = """SELECT *
                FROM students s
                WHERE birth_city = ?
            """
    db.execute(query, (city,))
    sortie = db.fetchall()
    return sortie

print(students_from_city(db, 'Paris'))




# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
