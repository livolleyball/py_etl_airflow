# coding:utf8
import petl as etl

# print(c)

cols1 = [[0, 1, 2], ['a', 'b', 'c']]
tb1 = etl.fromcolumns(cols1)
print(tb1)

# add "missing"
cols2 = [[0, 1, 2, 3], ['a', 'b', 'c']]
tb2 = etl.fromcolumns(cols2, missing='NA')
print(tb2)

# petl.io.json.fromjson()
dict = [{'foo': 'a', 'bar': 1},
        {'foo': 'b', 'bar': 2},
        {'foo': 'c', 'bar': 3},
        {'foo': 'd'}]
# 缺失值填充int:4
tb3 = etl.fromdicts(dict, header=['foo', 'bar'], missing=4)
print(tb3)

import sqlite3  # sqlite3 newDBName.db  新建数据库
# import string
# import random
import sqlalchemy

# conn = sqlite3.connect('/Users/huaminli/PycharmProjects/1py_etl_dag／data-dev.sqlite')
# c = conn.cursor()
# c.execute('''CREATE TABLE example (year INT, county TEXT, population INT)''')
# for i in string.ascii_lowercase:
#     c.execute('INSERT INTO example VALUES (?,?,?)',
#               (random.uniform(1000, 2000), i, random.uniform(20000, 30000)))
# conn.commit()
# tb4=etl.fromdb(conn,'select * from example')
# print(tb4)
# 新建表foobar
# c.execute('''CREATE TABLE foobar ( foo TEXT, bar INT)''')
# etl.todb(tb3,conn,'foobar')
# tb5=etl.fromdb(conn,'select * from foobar')
# print(tb5)

# etl.todb(tb3,conn,'foobar1',create=True)   # 须提前import sqlalchemy  ,参数create=true
# tb6=etl.fromdb(conn,'select * from foobar1')
# print(tb6)

# arrays(Numpy)
# import numpy as np
#
# t = [('foo', 'bar', 'baz'),
#      ('apples', 1, 2.5),
#      ('oranges', 3, 4.4),
#      ('pears', 7, .1)]
# a = etl.toarray(t, dtype='U4, i2, f4')
# print(a)
#
# array1 = np.array([('apples', 1, 2.5),
#                    ('oranges', 3, 4.4),
#                    ('pears', 7, .1)], dtype='U4, i2, f4')
# tb7 = etl.fromarray(array1)
# print(tb7)

# dataframe(pandas)
import pandas as pd

records = [('apple', 1, 2.5), ('orange', 3, 4.5), ('pears', 5, 6.5)]
df = pd.DataFrame.from_records(records, columns=('foo', 'bar', 'baz'))
tb8 = etl.fromdataframe(df)
print(tb8)

# load data from given table into dataframe
table = [('foo', 'bar', 'baz'),
         ('apple', 1, 2.5), ('orange', 3, 4.5), ('pears', 5, 6.5)]

df= etl.todataframe(table)
print(df)

# excel xls/xlsx
# HDFS
# oracle
