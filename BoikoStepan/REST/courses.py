import sqlite3


data = [
    {'id': 1, "name": "Python", "videos": 10},
    {'id': 2, "name": "Java", "videos": 20},
    {'id': 3, "name": "C++", "videos": 30},
]


conn = sqlite3.connect('courses.db')


cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE courses
    (id INTEGER PRIMARY KEY, name TEXT, videos INTEGER)
''')


for course in data:
    cursor.execute(f'''
        INSERT INTO courses (id, name, videos) 
        VALUES ({course['id']}, '{course['name']}', {course['videos']})
    ''')


conn.commit()


conn.close()
