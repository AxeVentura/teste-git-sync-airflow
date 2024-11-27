from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Definição da função que será executada
def tarefa_simples():
    print("Hello, Airflow!")

# Configuração da DAG
with DAG(
    dag_id="exemplo_simples",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    tarefa = PythonOperator(
        task_id="minha_tarefa",
        python_callable=tarefa_simples,
    )

    tarefa
