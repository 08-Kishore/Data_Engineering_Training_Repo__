cat > atm_cash_dag.py <<'EOF'
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv


# Task 1
def load_atms():
    with open('/opt/airflow/dags/atm_cash.csv', newline='') as file:
        records = list(csv.DictReader(file))

    print('ATM records loaded:', len(records))
    return records


# Task 2
def identify_low_cash(ti):
    records = ti.xcom_pull(task_ids='task_1')

    low_cash_atms = []

    for row in records:
        cash_available = int(row['cash_available'])
        daily_demand = int(row['daily_demand'])

        if cash_available < daily_demand:
            low_cash_atms.append(row['atm_id'])

    print('Low-cash ATM IDs:', low_cash_atms)
    return low_cash_atms


# Task 3
def calculate_total_cash(ti):
    records = ti.xcom_pull(task_ids='task_1')

    total_cash = 0

    for row in records:
        total_cash += int(row['cash_available'])

    print('Total available cash:', total_cash)
    return total_cash


# Task 4
def generate_report(ti):
    records = ti.xcom_pull(task_ids='task_1')
    low_cash_atms = ti.xcom_pull(task_ids='task_2')
    total_cash = ti.xcom_pull(task_ids='task_3')

    print("Number of ATMs:", len(records))
    print("Low-cash ATM IDs:", low_cash_atms)
    print("Total available cash:", total_cash)


with DAG(
    dag_id='atm_cash_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task_1 = PythonOperator(
        task_id='task_1',
        python_callable=load_atms,
    )

    task_2 = PythonOperator(
        task_id='task_2',
        python_callable=identify_low_cash,
    )

    task_3 = PythonOperator(
        task_id='task_3',
        python_callable=calculate_total_cash,
    )

    task_4 = PythonOperator(
        task_id='task_4',
        python_callable=generate_report,
    )

    task_1 >> [task_2, task_3] >> task_4
EOF
