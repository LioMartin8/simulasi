import time
import docker
import mlflow

# set mlflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("monitor-realtime_simulasi day4")

# set docker
client = docker.from_env()
all_container = client.containers.list(all=True)
status_sebelumnya = {}

while True:
    all_container = client.containers.list(all=True)
    for container in all_container:
        exit_code = container.attrs["State"]["ExitCode"]
        print("=" * 40)
        print("Data Container")
        print("=" * 40)
        print(f"Name       :{container.name}")
        print(f"Status     :{container.status}")
        if container.name in status_sebelumnya:
            if (
                status_sebelumnya[container.name] == "running"
                and container.status == "exited"
            ):
                print("CRASH DETECTED!!")
                nama_container = container.name
                print(f"Exit Code  :{exit_code}")

                with mlflow.start_run():
                    mlflow.log_param("Nama container: ", nama_container)
                    mlflow.log_metric("Exit Code: ", exit_code)
        # update status (di dalam loop)
        status_sebelumnya[container.name] = container.status
        print("=" * 40)
    time.sleep(30)
