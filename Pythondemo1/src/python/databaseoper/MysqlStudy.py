from ftplib import all_errors

import mysql.connector as conn


def select_dap_service(host, port, user, pwd, database):
    current_conn = conn.connect(host=host, port=port, user=user, passwd=pwd, db=database)
    cursor = current_conn.cursor()
    sql = "select * from t_flow_module_conf"
    cursor.execute(sql)
    result_all = cursor.fetchall()
    print(result_all)


def save_student(host, port, user, pwd, database):
    current_conn = conn.connect(host=host, port=port, user=user, passwd=pwd, db=database)
    cursor = current_conn.cursor()
    sql = 'insert into student(no,name, age) values (%s,%s,%s)'
    cursor.execute(sql, [1, "张三", 18])

    # 提交
    current_conn.commit()

    #关闭链接
    current_conn.close()
    cursor.close()


if __name__ == "__main__":
    host = "192.168.119.151"
    port = 3307
    user = "root"
    pwd = "123456"
    # database = "sc6kd_dap_dsgn_db"
    # select_dap_service(host, port, user, pwd, database)

    database = "test"
    save_student(host, port, user, pwd, database)
