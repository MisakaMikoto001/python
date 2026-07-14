r"""
    使用pymysql操作mysql数据库
        1.创建连接。MySQL服务器启动后，提供了基于TCP/IP的连接服务。我们可以通过pymysql模块中的connect()函数创建连接MySQL服务器。
            在调用connect()函数时，需要指定连接的参数，包括服务器地址、端口号、用户名、密码、数据库名称等，返回一个连接 connection 对象。
        2.创建游标。连接创建后，我们需要使用游标对象来执行SQL语句，MySQL会执行并将结果返回给游标对象。游标对象通过调用连接对象的cursor()方法创建。
        3.发出SQL语句。游标对象通过调用execute()方法发出SQL语句，MySQL会执行并将结果返回给游标对象。
        4.处理结果。如果 insert\update\delete 等操作，需求根据实际情况回滚或者提交事务。因为创建连接的是默认开启事务的，在操作完成后，
            需要使用连接对象commit()方法提交事务，或者使用rollback()方法回滚事务。执行select 操作时，需要使用游标对象的fetch()方法获取结果。
        5.关闭连接。在操作完成后，需要关闭游标对象和连接对象，释放释放的资源。
            关闭游标对象：游标对象通过调用finally中的close()方法关闭。
"""
# 插入数据

import pymysql

# no = int(input("请输入学号："))
# name = input("请输入姓名：")
# location = input("请输入地址：")

# 1创建连接池
# connection = pymysql.connect(host="localhost",port=3306,
#                              user="root",password="123456",
#                              database="word_tool",charset="utf8")


def insert_student(no,name,location):
    """ insert student """
    try:
        # 2创建游标对象
        with connection.cursor() as cursor:
            # 3通过游标对象向MySQL发送sql语句
            sql = """
            insert into td_student(no,name,location) values(%s,%s,%s)
            """
            affected_rows = cursor.execute(sql,(no,name,location))
            # 处理结果
            if affected_rows > 0:
                print("插入成功")
            else:
                print("插入失败")

            # 4提交事务
            connection.commit()
    except Exception as e:
        # 4回滚事务
        connection.rollback()
        print(e)
    finally:
        # 5关闭连接池
        connection.close()

# 删除数据
def delete_student(no):
    """ delete student """
    try:
        with connection.cursor() as cursor:
            # 3通过游标对象向MySQL发送sql语句

            sql = """
            delete from td_student where no=%s
            """
            affected_rows = cursor.execute(sql,(no,))
            # 处理结果
            if affected_rows > 0:
                print("删除成功")
            else:
                print("删除失败")

            # 4提交事务
            connection.commit()
    except Exception as e:
        # 4回滚事务
        connection.rollback()
        print(e)
    finally:
        # 5关闭连接池
        connection.close()

# 更新数据
def update_student(no,name,location):
    """ update student """
    try:
        with connection.cursor() as cursor:
            # 3通过游标对象向MySQL发送sql语句
            sql = """
            update td_student set name=%s,location=%s where no=%s
            """
            affected_rows = cursor.execute(sql,(name,location,no))
            # 处理结果
            if affected_rows > 0:
                print("更新成功")
            else:
                print("更新失败")
            # 4提交事务
            connection.commit()
    except Exception as e:
        # 4回滚事务
        connection.rollback()
        print(e)
    finally:
        # 5关闭连接池
        connection.close()

# 查询数据
def select_student(no):
    """ select student """
    try:
        with connection.cursor() as cursor:
            # 3通过游标对象向MySQL发送sql语句
            sql = """
            select name,location,no from td_student where no=%s
            """
            cursor.execute(sql,(no,))
            row= cursor.fetchone()
            while row:
                # 持续查询，直到没有数据了
                print(row)
                row= cursor.fetchone()
    except Exception as e:
        connection.rollback()
        print(e)
    finally:
        # 5关闭连接池
        connection.close()

# 分页查询
# page = int(input("请输入页码："))
# size = int(input("请输入每页数量："))

def select_student_by_page(page,size):
    """ select student by page """
    try:
        with connection.cursor() as cursor:
            sql = """
            select * from td_student order by no desc limit %s offset %s
            """
            cursor.execute(sql,(size,(page-1)*size))
            rows= cursor.fetchall()
            while rows:
                print(f'第{page}页数据：{rows}\n')
                rows= cursor.fetchall()
    except Exception as e:
        connection.rollback()
        print(e)
    finally:
        # 5关闭连接池
        connection.close()


# 综合例子
"""
    将数据库中的数据导出到excel文件中
"""
import openpyxl
import pymysql

# 创作工作簿对象
wb = openpyxl.Workbook()
# 获取默认工作表
ws = wb.active
# 表名
ws.title = "学生信息"
# 表头
ws.append(["学号","姓名","地址"])

# 创建连接池
connection = pymysql.connect(host="127.0.0.1",port=3306,
                             user="root",password="123456",
                             database="word_tool",charset="utf8")

def export_student_to_excel(connect, wb, ws):
    """ export student to excel """
    try:
        with connect.cursor() as cursor:
            sql = """
            select * from td_student
            """
            cursor.execute(sql)
            rows= cursor.fetchone()
            while rows:
                ws.append(rows)
                rows= cursor.fetchone()

        wb.save("学生信息.xlsx")
        print("导出成功")
    except Exception as e:
        print(e)
    finally:
        connect.close()
        wb.close()



if __name__ == '__main__':
    # insert_student(no,name,location)
    # delete_student(no)
    # update_student(no,name,location)
    # select_student(no)
    # select_student_by_page(page,size)
    export_student_to_excel(connection,wb,ws)
