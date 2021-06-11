import subprocess
import re

DEFAULT_WIFI_INTERFACE = "wlan0"

RSSI_REGEX = r"Signal level=(\-?\d+) dBm"


def get_wifi_network_ssid(interface_name):
    arg_list = ['iwgetid', '-r']

    proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            universal_newlines=True)

    output, dummy = proc.communicate()

    return output.strip()


def get_wifi_network_rssi(interface_name):
    arg_list = ['iwconfig', interface_name]

    proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            universal_newlines=True)
    output, dummy = proc.communicate()

    m = re.search(RSSI_REGEX, output.strip())

    return int(m.groups()[0])

