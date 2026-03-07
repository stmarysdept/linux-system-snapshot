# linux-system-snapshot

hi sysadmins (or NORMAL people). tired of running multiple commands to gather data on your currently running system/server? linux-system-snapshot is a basic cli-only tool that takes a current "snapshot" of important details about what you're running, such as:


_HOSTNAME_

_CURRENT DATE AND TIME_

_SYSTEM UPTIME_

_DISK,RAM,AND CPU USAGE DATA_

_USERS ACTIVE ON SESSION_

_KERNEL VERSION_

_IP ADDRESSES (IPv4 & IPv6)_

# requirements

all you need is: 

_Linux_ 

_Python 3_ 

# usage

_git clone https://github.com/stmarysdept/linux-system-snapshot_

_cd linux-system-snapshot_

_python3 snapshot.py_


# example output
```
============================================================
                        System Info

HOSTNAME:
mypc

CURRENT DATE:
2026-03-07, and it's currently: 06:17:32

UPTIME SINCE:
2026-03-06 06:03:18, up 6 hours, 14 minutes

DISK USAGE DATA:
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p2  xx  xx  xxx  xx% /

RAM USAGE DATA:
PID COMMAND         %MEM
  57287 xx              10.4
   4334 xx               2.8
   9643 xx               2.6
  37825 xx               1.9
  49494 xx               1.8

CPU USAGE DATA:
PID COMMAND         %CPU
  12409 xx              it's over 9000!!
  67135 xx            45.4
  57287 xx            26.1
   4334 xx            12.0
   2767 xx             6.4

CURRENTLY ACTIVE USERS:
mypc seat0        2026-03-06 12:07 (login screen)
mypc tty2         2026-03-06 12:07 (tty2)

KERNEL VERS:
6.8.0-101-generic

IP ADDRESSES:
IPV4:
192.168.0.xxx

IPV6:
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
