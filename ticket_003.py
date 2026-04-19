import docker
import mlflow

# set mlflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("simulasi mlops day3")

# set docker
client = docker.from_env()
all_container = client.containers.list(all=True)
exited_container = [
    container for container in all_container if container.status == "exited"
]
total_crash = 0

for container in all_container:
    exit_code = container.attrs["State"]["ExitCode"]
    logs = container.logs(tail=10)
    nama_container = container.name
    if exit_code != 0:
        with mlflow.start_run():
            mlflow.log_param("Nama container ", nama_container)
            mlflow.log_metric("Exit Code ", exit_code)
        total_crash = total_crash + 1
        print("=" * 40)
        print(f"Name         :{container.name}")
        print(f"Exit Code    :{exit_code}")
        print(f"Log container:{logs.decode()}")
        print("=" * 40)

print(f"Total crash:{(total_crash)}container")
