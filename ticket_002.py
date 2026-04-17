import docker
import mlflow

# setup mlflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("simulasi day 2")

# setup docker
client = docker.from_env()
all_container = client.containers.list(all=True)

with mlflow.start_run():
    for container in all_container:
        if container.status == "exited":
            exit_code = container.attrs["State"]["ExitCode"]
            log_container = container.logs(tail=5)
            mlflow.log_param(f"exit_code:{container.name}", exit_code)
            mlflow.log_text(log_container.decode(), f"Logs:{container.name}.txt")
            print("=" * 40)
            print(f"Name         :{container.name}")
            print(f"Kode exit    :{exit_code}")
            print(f"Satus        :{container.status}")
            print(f"Log container:{log_container.decode()}")
            print("=" * 40)
        else:
            print("tidak ada container yang exited")
