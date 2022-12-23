import os
import sys
import platform
import subprocess


def ping(hostname: str):
    """
        Pings a host to check if it is up 

        Parameters:
            host: Hostname or IP address
        Returns:
            Whether the host is active or not
    """

    flag = '-n' if platform.system().lower() == 'windows' else '-c'     # Get flag based on OS
    return os.system(f"ping {flag} 3 " + hostname)                      # Execute and get ping response
        


if __name__ == "__main__":

    # Arguments
    args = sys.argv[1:]
    # host = args[0]
    host = "82.115.20.167"  # UP
    # host = "10.1.1.1"       # DOWN

    if ping(host) == 0:
        print(f"'{host}' is UP.")
    else:
        print(f"'{host}' is DOWN.")