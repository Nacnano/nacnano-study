import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import chain


dag_1 = DAG('this_dag_will_be_discovered')

with DAG(
    dag_id='my_dag',
    start_date=pendulum.datetime(2016, 1, 1, tz="UTC"),
    schedule_interval='@daily',
    catchup=False,
    default_args={'retries': 2},
) as dag:
    op = BashOperator(task_id='dummy', bash_command='Hello World!')
    print(op.retries)  # 2