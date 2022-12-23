# Toolkit

## Guide

### ping
Sim (python):
    - `python3 ping.py 82.115.20.167` -> "82.115.20.167 is UP."
    - `python3 ping.py 10.1.1.1` -> "10.1.1.1 is DOWN."
Actual (ping):
    - `sudo bash ping.sh 82.115.20.167` -> "82.115.20.167 is UP."
    - `sudo bash ping.sh 10.1.1.1` -> "10.1.1.1 is DOWN."

### IP range
Sim (python):
    - `python3 ip_range.py 82.115.20.167 160 170` -> "Port Open: --> 62411"
Actual (nmap):
    - See [http://ports.my-addr.com/](http://ports.my-addr.com/ip-range-port-scanner-tool.php)

### Port Scanner
Sim (python):
    - `python3 port_scanner.py 82.115.20.167 62410 62415` -> "Port Open: --> 62411"
Actual (hping3):
    - `sudo bash port_scanner.sh 82.115.20.167` -> "82.115.20.167 is UP."