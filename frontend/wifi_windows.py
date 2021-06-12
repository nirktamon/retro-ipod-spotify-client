# This is a stub for a windows machine

import random

DEFAULT_WIFI_INTERFACE = "wifi"


def get_wifi_network_ssid(interface_name):
    return interface_name


def get_wifi_network_rssi(interface_name):
    return random.randint(-100, -30) + len(interface_name)
