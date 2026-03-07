# HELLO! 
# Created by "stmarysdept" (stmarysdept@proton.me)
# Please do not redistribute!


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

def get_disk():
    disk = subprocess.run(
            ["df", "/home", "-h"],
            capture_output=True,
            text=True
        )
    return disk.stdout.strip()

def get_ram():
     ram = subprocess.run(
          "ps -eo pid,comm,%mem --sort=-%mem | head -6",
          capture_output=True,
          text=True,
          shell=True
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
        "ps -eo pid,comm,%cpu --sort=-%cpu | head -6",
        capture_output=True,
        text=True,
        shell=True #putting this here so i can use the pipe hehe
     )
     return cpu.stdout.strip()

def get_kernel():
     kernel = subprocess.run(
          ["uname", "-r"],
          capture_output=True,
          text=True
     )
     return kernel.stdout.strip()

def ips():
     ipo = subprocess.run(
          ["hostname", "-I"],
          capture_output=True,
          text=True
     ).stdout.strip()

     ipv4 = []
     ipv6 = []

     for ip in ipo.split():
          if "." in ip:
               ipv4.append(ip)
          elif ":" in ip:
               ipv6.append(ip)

     return ipv4, ipv6


def main(): 
        since, pretty = get_uptime()
        ipv4, ipv6 = ips()

        print("=" * 60)
        print("System Info\n".center(60))

        print("HOSTNAME:")
        print(f"{get_hostname()}\n")

        print("CURRENT DATE:")
        print(f"{get_datetime()}\n")

        print("UPTIME SINCE:")
        print(f"{since}, {pretty}\n")

        print("DISK USAGE DATA:")
        print(f"{get_disk()}\n")

        print("RAM USAGE DATA:")
        print(f"{get_ram()}\n")

        print("CPU USAGE DATA:")
        print(f"{get_cpu()}\n")

        print("CURRENTLY ACTIVE USERS:")
        print(f"{get_users()}\n")

        print("KERNEL VERS:")
        print(f"{get_kernel()}\n")

        print("IP ADDRESSES:")
        print("IPV4:")
        for ip in ipv4:
             print(ip)
        print("\nIPV6:")
        for ip in ipv6:
             print(ip)
             

        print("=" * 60)
if __name__ == "__main__":
     main()