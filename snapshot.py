import datetime
import socket
import subprocess

def get_hostname():
    return socket.gethostname()

def get_datetime():
    t = datetime.datetime.now()
    return t.strftime("%Y-%m-%d, and it's currently: %H:%M:%S")

def get_uptime():
    uptime = subprocess.run(
            ["uptime", "-s"], 
            capture_output=True, 
            text=True
        )
    return uptime.stdout.strip()

def get_uptime_xtra():
    uptime_xtra = subprocess.run(
            ["uptime", "-p"], 
            capture_output=True, 
            text=True
        )
    return uptime_xtra.stdout.strip()
     # I really don't like the fact I had to make another
     # function just to relay a more human version of uptime
     # but I'll figure out how to fix that soon.

def get_disk():
    disk = subprocess.run(
            ["df", "/home", "-h"],
            capture_output=True,
            text=True
        )
    return disk.stdout.strip()


def main(): # would i rather have a thousand print commands
            # or a thousand newlines.. hmm...
        print("========================= CURRENT STATS ===============================")
        print(f"HOSTNAME:\n{get_hostname()} \n\n")
        print(f"CURRENT DATE:\n{get_datetime()} \n\n")
        print(f"UPTIME SINCE:\n{get_uptime()}, {get_uptime_xtra()} \n\n")
        print("DISK USAGE DATA:\n")
        print(f"{get_disk()}")
        print("=======================================================================")
if __name__ == "__main__":
     main()