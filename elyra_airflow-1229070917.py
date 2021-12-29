from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "elyra_airflow-1229070917",
}

dag = DAG(
    "elyra_airflow-1229070917",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.4.0 pipeline editor using `elyra_airflow.pipeline`.",
    is_paused_upon_creation=False,
)


# Ensure that the secret named 'my-airflow-aws' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="my-airflow-aws",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="my-airflow-aws",
    key="AWS_SECRET_ACCESS_KEY",
)


# Operator source: {'catalog_type': 'elyra-airflow-examples-catalog', 'component_ref': {'component-id': 'bash_operator.py'}}
op_b62180de_f900_4244_ba27_013913617f16 = BashOperator(
    task_id="BashOperator",
    bash_command="echo '\u54c8\u54c8'",
    xcom_push=True,
    env={},
    output_encoding="utf-8",
    dag=dag,
)
