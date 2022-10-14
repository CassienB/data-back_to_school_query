# pylint:disable=C0111,C0103
#import sqlite3

def students_from_city(db, city):
    """return a list of students from a specific city"""
    query = """SELECT s.first_name, s.last_name
                FROM students s
                WHERE birth_city = ?
            """
    params = (city,)
    db.execute(query, params)
    return db.fetchall()


# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
#

#conn = sqlite3.connect('data/school.sqlite')
#db = conn.cursor()
#print(students_from_city(db, 'Paris'))
