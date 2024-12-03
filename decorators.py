from airflow import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

def _choose_best_model():
    accuracy = 6
    if accuracy > 5:
        return 'accurate'
    return 'inaccurate'

with DAG('branching', start_date=datetime(2023, 1, 1), schedule='@daily', catchup=False):
    choose_best_model = BranchPythonOperator(
    task_id='choose_best_model',
    python_callable=_choose_best_model
)

    accurate = EmptyOperator(
    task_id='accurate'
    )

    inaccurate = EmptyOperator(
    task_id='inaccurate'
)

choose_best_model >> [accurate, inaccurate]