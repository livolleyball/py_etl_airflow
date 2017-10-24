# coding:utf8

import airflow
from airflow.operators.mysql_operator import MySqlOperator
from airflow import DAG
from datetime import timedelta, datetime

default_args = {
    'owner': 'liyi',
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag1 = DAG('mysql_create_from', default_args=default_args, description='A simple create_mysql_data DAG',
           schedule_interval=timedelta(minutes=10))
# print(dag1)
# print(type(dag1))
sql1 = ["INSERT INTO airflow_test.test1_from (date1) values (now())"]

t1 = MySqlOperator(
    mysql_conn_id='liyi',
    sql=sql1,
    task_id='mysql_create_from',
    dag=dag1
)

sql2 = ["""insert into airflow_test.test1_in(date1)
select * from airflow_test.test1_from ORDER BY date1 DESC LIMIT 1;"""]

t2 = MySqlOperator(
    mysql_conn_id='liyi',
    sql=sql2,
    task_id='mysql_insert_into',
    dag=dag1
)

t2.set_upstream(t1)
