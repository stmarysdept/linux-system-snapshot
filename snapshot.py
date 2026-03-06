import datetime
import socket
import subprocess

def get_hostname():
    return socket.gethostname()

def get_datetime():
    t = datetime.datetime.now()
    return t.strftime("%Y-%m-%d, and it's currently: %H:%M:%S")

def get_uptime():
     since = subprocess.run(["uptime", "-s"], capture_output=True, text=True).stdout.strip()
     pretty = subprocess.run(["uptime", "-p"], capture_output=True, text=True).stdout.strip()
     return since, pretty
since, pretty = get_uptime()

def get_disk():
    disk = subprocess.run(
            ["df", "/home", "-h"],
            capture_output=True,
            text=True
        )
    return disk.stdout.strip()

def get_ram():
     ram = subprocess.run(
          ["free", "-h"],
          capture_output=True,
          text=True
     )
     return ram.stdout.strip()

def get_users():
     users = subprocess.run(
          ["who"],
          capture_output=True,
          text=True
     )
     return users.stdout.strip()

def get_cpu():
     cpu = subprocess.run(
        ["uptime"],
        capture_output=True,
        text=True
     )
     
     return cpu.stdout.strip()


def main(): 
        print("=" * 60)
        print("System Info".center(60))
#TODO parse/split the disk usage and ram usage data
        print(f"HOSTNAME:\n{get_hostname()} \n\n")
        print(f"CURRENT DATE:\n{get_datetime()} \n\n")
        print(f"UPTIME SINCE:\n{since}, {pretty} \n\n")
        print("DISK USAGE DATA:")
        print(f"{get_disk()}\n")

        print("RAM USAGE DATA:")
        print(f"{get_ram()}\n")

        print("CPU USAGE DATA (load times):") #good enough for now
        print(f"{get_cpu()}\n")

        print(f"CURRENTLY ACTIVE USERS:\n{get_users()}")


        print("=" * 60)
if __name__ == "__main__":
     main()