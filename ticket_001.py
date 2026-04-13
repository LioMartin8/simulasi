import docker
import mlflow

# setup mlflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("simulasi_kerja *ulang")

# setup docker
client = docker.from_env()
all_container = client.containers.list(all=True)
running = client.containers.list()

for container in all_container:
    tags = container.image.tags
    image_name = tags[0] if tags else "<no tags>"
    print("=" * 40)
    print(f"Name Container    :{container.name}")
    print(f"Status Container  :{container.status}")
    print(f"Image Container   :{image_name}")
    print("=" * 40)

# tampilkan ringkasan
print("*" * 40)
print("Total semua container", len(all_container))
print("Total Running container", len(running))
print("*" * 40)

# catat di mlflow
total_running = len(running)
total_container = len(all_container)
with mlflow.start_run():
    mlflow.log_metric("Total container yang berjalan: ", total_running)
    mlflow.log_metric("Total semua container running dan exited: ", total_container)

    print(f"tercatat: running={total_running}, total={total_container}")
