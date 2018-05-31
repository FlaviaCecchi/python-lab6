import pymysql


def show_tasks():
    tasks = []
    sql = "SELECT * FROM tasks"
    connection = pymysql.connect(user="root", password="Nena1993", host="localhost", database="tasks")
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for task in results:
        tasks.append(task)
    connection.close()
    return tasks


def new_task(task):
    sql = "INSERT INTO tasks(todotask) VALUES (%s)"
    connection = pymysql.connect(user="root", password="Nena1993", host="localhost", database="tasks")
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    connection.close()


def remove_task(task_id):
    sql = 'DELETE FROM tasks WHERE id=%s'
    connection = pymysql.connect(user="root", password="Nena1993", host="localhost", database="tasks")
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    connection.close()