cat > factory_quality_dag.py <<'EOF'
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv


def load_batches():
    with open("/opt/airflow/dags/factory_batches.csv", newline="") as file:
        rows = list(csv.DictReader(file))

    print("Batches loaded:", len(rows))
    return rows

def check_quality(ti):
    records = ti.xcom_pull(task_ids="load_batches")

    review_batches = []

    for row in records:
        produced = int(row["units_produced"])
        defective = int(row["defective_units"])

        if produced > 0 and (defective / produced) > 0.05:
            review_batches.append(row["batch_id"])

    print("Batches requiring review:", review_batches)
    return review_batches


def calculate_value(ti):
    records = ti.xcom_pull(task_ids="load_batches")

    total_value = 0

    for row in records:
        produced = int(row["units_produced"])
        value_per_unit = int(row["value_per_unit"])

        total_value += produced * value_per_unit

    print("Total production value:", total_value)
    return total_value


def generate_report(ti):
    records = ti.xcom_pull(task_ids="load_batches")
    review_batches = ti.xcom_pull(task_ids="check_quality")
    total_value = ti.xcom_pull(task_ids="calculate_value")

    print("Total batches:", len(records))
    print("Batches needing review:", review_batches)
    print("Total production value:", total_value)


with DAG(
    dag_id="factory_quality_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    load_batches_task = PythonOperator(
        task_id="load_batches",
        python_callable=load_batches,
    )

    check_quality_task = PythonOperator(
        task_id="check_quality",
        python_callable=check_quality,
    )

    calculate_value_task = PythonOperator(
        task_id="calculate_value",
        python_callable=calculate_value,
    )

    generate_report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    load_batches_task >> [check_quality_task, calculate_value_task] >> generate_report_task
EOF
