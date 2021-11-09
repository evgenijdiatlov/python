import sqlite3 as sql
 
class DBWorker:
    def __init__(self, db_name):
        self.cur_db = sql.connect(db_name)
        self.cursor = None
        self.result = None
    def connect_db(self):
        self.cursor = self.cur_db.cursor()
    def use_query(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.cur_db.commit()
    def return_result(self):
        return self.result 


db = DBWorker('fresh.db')
db.connect_db()
#db.use_query('CREATE TABLE month (id int, name varchar(10), days int)')
#db.use_query("INSERT INTO month (id,name,days) VALUES (1, 'January', 31)")
#db.use_query("INSERT INTO month (id,name,days) VALUES (2, 'February', 29)")
#db.use_query("INSERT INTO month (id,name,days) VALUES (3, 'March', 31)")
# db.use_query("INSERT INTO month (id,name,days) VALUES (4, 'April', 30)")
# db.use_query("INSERT INTO month (id,name,days) VALUES (5, 'May', 31)")
# db.use_query("INSERT INTO month (id,name,days) VALUES (6, 'June', 30)")
# db.use_query("INSERT INTO month (id,name,days) VALUES (7, 'Jule', 31)")
# db.use_query("INSERT INTO month (id,name,days) VALUES (5, 'Augest', 30)")
# db.use_query("INSERT INTO month (id,name,days) VALUES (5, 'Septembre', 31)")


#db.use_query("SELECT * FROM month") вывод всех значений
#db.use_query("SELECT name FROM month WHERE days=31") вывод назания месяца в котором 31 день
#db.use_query("SELECT id, name  FROM month WHERE days=31")
#db.use_query("SELECT id, name FROM month WHERE days in (30,31)")
#db.use_query("SELECT id, name FROM month WHERE name like 'May'")
#db.use_query("SELECT id, name FROM month WHERE (id > 1 AND days <31) OR id =1")
#db.use_query("SELECT count(id), name, days FROM month GROUP BY days") count - сортировка по количесту дней
#db.use_query("SELECT id, name, avg(days) FROM month GROUP BY days") avg - среднее значение
#db.use_query("SELECT count(id), name, days FROM month WHERE id > 1 GROUP BY days")
#db.use_query("SELECT count(id), name, days FROM month WHERE id > 0 GROUP BY days HAVING count(id)>3")
#db.use_query("SELECT id, name, days FROM month ORDER BY -days, name") #ORDER BY days сортировка по дням
# for row in db.result:
#     print(row)


# создаем таблицы магазины и города

# db.use_query('CREATE TABLE shop (id int, name varchar(10))')
# db.use_query('CREATE TABLE city (id int, shop_id int, addr varchar(10))')


# db.use_query("INSERT INTO shop (id,name) VALUES (1, 'Евроопт')")
# db.use_query("INSERT INTO shop (id,name) VALUES (2, 'Соседи')")
# db.use_query("INSERT INTO shop (id,name) VALUES (3, 'Корона')")
# db.use_query("INSERT INTO shop (id,name) VALUES (4, 'Виталюр')")

# db.use_query("INSERT INTO city (id,shop_id,addr) VALUES (1, 1, 'Какой-то')")
# db.use_query("INSERT INTO city (id,shop_id,addr) VALUES (2, 1, 'Ещё один')")
# db.use_query("INSERT INTO city (id,shop_id,addr) VALUES (3, 1, 'Новый')")

# db.use_query("""
# SELECT * FROM shop LEFT JOIN city on city.shop_id = shop.id
# """)

# db.use_query("""
# SELECT count(shop.id), shop.name
# FROM shop JOIN city on city.shop_id = shop.id
# GROUP BY shop.name
# HAVING count(shop.id) > 1
# """)


# db.use_query('''
# UPDATE city
# SET shop_id = 1
# WHERE addr = "Новый"
# ''')
# db.use_query('SELECT * FROM city')

# db.use_query('''
# DELETE FROM city
# WHERE addr = "Новый"
# ''')
# db.use_query('SELECT * FROM city')
# db.use_query('''
# DROP TABLE city      drop удалить таблицу полностью
# ''')
# db.use_query('SELECT * FROM city')

# print(db.result)
