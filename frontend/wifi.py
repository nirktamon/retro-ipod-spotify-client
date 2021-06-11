import objc

DEFAULT_WIFI_INTERFACE = "en1"

def get_wifi_network_ssid(interface_name):
    objc.loadBundle('CoreWLAN',
                    bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
                    module_globals=globals())

    for iname in CWInterface.interfaceNames():
        if interface_name == iname:
            return CWInterface.interfaceWithName_(iname).ssid()

    return None


def get_wifi_network_rssi(interface_name):
    objc.loadBundle('CoreWLAN',
                    bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
                    module_globals=globals())

    for iname in CWInterface.interfaceNames():
        if interface_name == iname:
            return CWInterface.interfaceWithName_(iname).rssi()

    return None
