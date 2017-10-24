# coding:utf8
import pymysql

connect= pymysql.connect(host='192.168.64.5',
                         port=3306,
                         user='liyi',
                         password='liyi',
                         db='airflow',
                         charset='utf8')
print(connect)