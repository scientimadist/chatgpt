import psycopg2

# TODO: we want a module that interact with the output of ChatGPT and the front-end Web Page

if __name__ == '__main__':
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='company1',
        user='postgres',
        password='123456'
    )

    cur = conn.cursor()
    name = "杨恒宇"
    department_id = 1
    job = '技术开发'
    email = '12012709@mail.sustech.edu.cn'
    nickname = '小杨'
    curr_task = '数据库后端开发'
    next_task = 'None'
    work_length = 'None'
    data = (name, department_id, job, email, nickname, curr_task, next_task, work_length)
    sql = 'insert into employee(employee_name, department_id, job, email, nickname, current_task, next_task, work_strength) values (%s, %s, %s, %s,%s, %s, %s, %s ) '
    cur.execute(sql, data)
    cur.execute('select * from employee')
    rows = cur.fetchall()
    for row in rows:
        print(rows)
