import os
import time
import psutil
from datetime import datetime


APP_NAME = os.getenv("APP_NAME", "python-monitor")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
LOG_FILE = "/tmp/python-automation.log"


def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()

    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    return f"{days} days, {hours} hours, {minutes} minutes"


def get_disk_usage():
    disk = psutil.disk_usage("/")
    return {
        "total": f"{disk.total / (1024 ** 3):.2f} GB",
        "used": f"{disk.used / (1024 ** 3):.2f} GB",
        "free": f"{disk.free / (1024 ** 3):.2f} GB",
        "percent": f"{disk.percent}%"
    }


def get_memory_usage():
    memory = psutil.virtual_memory()

    return {
        "total": f"{memory.total / (1024 ** 3):.2f} GB",
        "used": f"{memory.used / (1024 ** 3):.2f} GB",
        "available": f"{memory.available / (1024 ** 3):.2f} GB",
        "percent": f"{memory.percent}%"
    }


def get_running_processes():
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "status"]
    ):
        try:
            info = process.info
            processes.append(info)
        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    return processes[:10]


def create_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")


def monitor_system():
    print("=" * 60)
    print(f"Application : {APP_NAME}")
    print(f"Environment : {ENVIRONMENT}")
    print("=" * 60)

    uptime = get_uptime()
    print(f"System Uptime : {uptime}")
    create_log(f"System Uptime: {uptime}")

    disk = get_disk_usage()

    print("\nDisk Usage")
    print(f"Total   : {disk['total']}")
    print(f"Used    : {disk['used']}")
    print(f"Free    : {disk['free']}")
    print(f"Usage   : {disk['percent']}")

    create_log(f"Disk Usage: {disk}")

    memory = get_memory_usage()

    print("\nMemory Usage")
    print(f"Total     : {memory['total']}")
    print(f"Used      : {memory['used']}")
    print(f"Available : {memory['available']}")
    print(f"Usage     : {memory['percent']}")

    create_log(f"Memory Usage: {memory}")

    processes = get_running_processes()

    print("\nRunning Processes")

    for process in processes:
        print(
            f"PID: {process['pid']} | "
            f"Name: {process['name']} | "
            f"Status: {process['status']}"
        )

    create_log(
        f"Detected {len(processes)} running processes"
    )

    print("\nLog file created:")
    print(LOG_FILE)

    print("=" * 60)


if __name__ == "__main__":
    monitor_system()