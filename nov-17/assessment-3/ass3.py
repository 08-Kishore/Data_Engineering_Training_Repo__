cat > airport_baggage_dag.py <<'EOF'

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv

# Task 1
def load_baggage():
    with open('/opt/airflow/dags/airport_baggage.csv', newline='') as file:
        records = list(csv.DictReader(file))

    print('Baggage records loaded:', len(records))
    return records


# Task 2
def identify_review_bags(ti):
    records = ti.xcom_pull(task_ids='load_baggage')

    review_bags = [
        record['bag_id']
        for record in records
        if record['screening_status'] == 'Review'
        or int(record['weight_kg']) > 23
    ]

    print("Review Bags:", review_bags)
    return review_bags


# Task 3
def calculate_total_weight(ti):
    records = ti.xcom_pull(task_ids='load_baggage')

    total_weight = sum(int(record['weight_kg']) for record in records)

    print("Total Weight:", total_weight)
    return total_weight


# Task 4
def generate_report(ti):
    records = ti.xcom_pull(task_ids='load_baggage')
    review_bags = ti.xcom_pull(task_ids='identify_review_bags')
    total_weight = ti.xcom_pull(task_ids='calculate_total_weight')
    print(f"Number of bags: {len(records)}")
    print(f"Bags requiring review: {review_bags}")
    print(f"Total baggage weight: {total_weight} kg")



with DAG(
    dag_id='airport_baggage_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['airport', 'baggage']
) as dag:

    load_baggage_task = PythonOperator(
        task_id='load_baggage',
        python_callable=load_baggage
    )

    identify_review_bags_task = PythonOperator(
        task_id='identify_review_bags',
        python_callable=identify_review_bags
    )

    calculate_total_weight_task = PythonOperator(
        task_id='calculate_total_weight',
        python_callable=calculate_total_weight
    )

    generate_report_task = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report
    )

    load_baggage_task >> [
        identify_review_bags_task,
        calculate_total_weight_task
    ] >> generate_report_task
EOF
