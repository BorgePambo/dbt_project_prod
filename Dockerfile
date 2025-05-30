FROM astrocrpublic.azurecr.io/runtime:3.0-2

# Instale o dbt em um ambiente virtual (já feito)
RUN python -m venv /usr/local/airflow/dbt_venv && \
    /usr/local/airflow/dbt_venv/bin/pip install dbt-postgres

# Adiciona o executável do dbt ao PATH
ENV PATH="/usr/local/airflow/dbt_venv/bin:${PATH}"

# Copia a pasta application_prod com tudo dentro
COPY dags/dbt/application_prod /usr/local/airflow/dags/dbt/application_prod

# Opcional: cria um link simbólico ou cópia direta do profiles.yml (se precisar)
RUN mkdir -p /usr/local/airflow/dags/dbt && \
    ln -s /usr/local/airflow/dags/dbt/application_prod/profiles.yml /usr/local/airflow/dags/dbt/profiles.yml