import docker
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("simulasi-kerja")

client = docker.from_env()
containers = client.containers.list()
all_container = client.containers.list(all=True)

if len(containers) == 0:
    print("=" * 40)
    print("Tidak ada container yang sedang berjalan")
    print("=" * 40)
    for container in all_container:
        tagss = container.image.tags
        if tagss:
            print(f"Image     :{container.image.tags[0]}")
        else:
            print("image     :<no tag>")
            print("=" * 40)
            print("Semua yang sedang berjalan dan yang exited")
            print("=" * 40)
            print(f"Name      :{container.name}")
            print(f"Status    :{container.status}")
            print(tagss)
            print("=" * 40)

else:
    total = len(containers)
    print("=" * 40)
    print(f"Total Container yang sedang berjalan:    {total}")
    print("=" * 40)
    for container in containers:
        tagss = container.image.tags
        if tagss:
            print(f"Image     :{container.image.tags[0]}")
        else:
            print("image     :<no tag>")
            print("=" * 40)
            print("Container yang sedang berjalan")
            print("=" * 40)
            print(f"Name      :{container.name}")
            print(f"Status    :{container.status}")
            print(tagss)
            print("=" * 40)
    for container in all_container:
        print("=" * 40)
        print("Semua yang sedang berjalan dan yang exited")
        print("=" * 40)
        print(f"Name      :{container.name}")
        print(f"Status    :{container.status}")
        print(tagss)
        print("=" * 40)
