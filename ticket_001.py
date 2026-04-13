import docker
import mlflow

# setup MLflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("simulasi kerja")


# setup docker
client = docker.from_env()
all_containers = client.containers.list(all=True)
running_containers = client.containers.list()

# Cetak ringkasan dulu
print(f"Total running: {len(running_containers)}")
print(f"Total semua (termasuk mati): {len(all_containers)}")

# Baru cetak detail SEMUA container (pakai all_containers)
for container in all_containers:
    # ambil tag dengan aman
    tags = container.image.tags
    image_name = tags[0] if tags else "<no tag>"

    print("=" * 40)
    print(f"Name   : {container.name}")
    print(f"Status : {container.status}")
    print(f"Image  : {image_name}")
    print("=" * 40)

hitung = float(len(all_containers))
coba = len(running_containers)

with mlflow.start_run():
    mlflow.log_metric("Total conntainer yang berjalan", coba)
    mlflow.log_metric("Total data container running dan exited", hitung)
    print(f"Data tercatat di MLflow: total={hitung}, running={coba}")
