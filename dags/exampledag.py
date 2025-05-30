from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from datetime import datetime
import os

# Pegando o AIRFLOW_HOME do ambiente ou definindo um padrão
airflow_home = os.environ.get("AIRFLOW_HOME", "/usr/local/airflow")

my_db_dag = DbtDag(
    project_config=ProjectConfig(
        dbt_project_path=f"{airflow_home}/dags/dbt/application_prod",  # Pasta onde está seu dbt_project.yml
    ),
    profile_config=ProfileConfig(
        profile_name="application_prod",  # Nome do perfil no profiles.yml
        target_name="dev",                # Ambiente usado por padrão
        profiles_yml_filepath=f"{airflow_home}/dags/dbt/application_prod/profiles.yml",  # Atualizado: profiles.yml dentro de application_prod
    ),
    execution_config=ExecutionConfig(
        dbt_executable_path="/usr/local/bin/dbt"  # Caminho do dbt instalado no container
    ),
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    dag_id="application_prod",
)