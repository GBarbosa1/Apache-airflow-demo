from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")


with DAG(
    dag_id = "producer",
    schedule = "@daily",
    start_date = datetime(2023,8,15),
    catchup = False
    ):

    @task(outlets = [my_file])
    def update_dataset():
        with open(my_file.uri, "a+") as f:
            f.write("Producer update")
    
    @task(outlets = [my_file_2])
    def update_dataset():
        with open(my_file.uri, "a+") as f:
            f.write("Producer update")
    update_dataset()