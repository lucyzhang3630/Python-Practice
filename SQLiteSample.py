#in Sqlite, search names based on score range
# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# data initialization:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    'return names in required score range, ordered by score from low to high'
    conn1 = sqlite3.connect(db_file)
    cursor1 = conn1.cursor()
    cursor1.execute('select name from user where score between ? and ? order by score',(low,high))
    values = cursor1.fetchall()
    results = [i[0] for i in values]
    '''
    for x in range(len(values)):
        results.append(values[x])'''
    print(results)
    cursor1.close()
    conn1.close()
    return results


# test
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
#print(get_score_in(80,95))

print('Pass')
