from airflow.decorators import dag
from airflow.operators.bash import BashOperator
import pendulum


@dag(
    dag_id="search-engine",
    schedule="@daily",
    start_date=pendulum.datetime(2023, 7, 20, tz="UTC"),
    catchup=False,
    #dagrun_timeout=datetime.timedelta(minutes=60),
)
def ProcessDownload():
    task_download = BashOperator(
        task_id="download_cv",
        bash_command="source /home/noor/projects/search-engine/.venv/bin/activate && "+ 
        " cd /mnt/c/Users/noora/OneDrive/Desktop/Internsip/Seach-Engine- && "+
        " python Cv_downloader.py ",
    )
    

    task_indix = BashOperator(
        task_id="Indixing_cv",
        bash_command="source /home/noor/projects/search-engine/.venv/bin/activate && "+ 
        " cd /mnt/c/Users/noora/OneDrive/Desktop/Internsip/Seach-Engine- && "+
        " python extractPDFFile.py ",
    )
    task_download >> task_indix
ProcessDownload()
