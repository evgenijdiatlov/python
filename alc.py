from sqlalchemy import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer, String
 
engine = create_engine('sqlite:///college.db', echo=True)
conn = engine.connect()
meta = MetaData()
 
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
)
 
meta.create_all(engine)
 
# st = students.insert().values(first_name='Yan', last_name='Shliakhau')
# result = conn.execute(st)
# st = students.insert().values(first_name='Kek', last_name='1234')
# result = conn.execute(st)
# st = students.insert().values(first_name='LOl', last_name='4321')
# result = conn.execute(st)
# print(st)
 
# conn = engine.connect()
 
 
# print(result)
 
# updater = (
#     students
#     .update()
#     .where(students.c.first_name=='Yan')
#     .values(first_name='Ivan')
# )
# print(updater)
# conn.execute(updater)
 
deleter = (
    students
    .delete()
    .where(students.c.id > 3)
)
print(deleter)
# conn.execute(deleter)
 
conn.execute(
    students.insert(),
    [
        {'first_name': 'one', 'last_name': '2'},
        {'first_name': 'two', 'last_name': '2'},
        {'first_name': 'three', 'last_name': '2'},
    ]
)
 
s = students.select()
print(s)
 
result = conn.execute(s)
print(result.fetchall())