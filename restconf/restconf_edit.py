import requests
import json
from pprint import pprint

# Suppress warnings about certificates
requests.packages.urllib3.disable_warnings()

wlc = {
    "host": "192.168.1.19",
    "username": "admin",
    "http_port": 443,
    "password": "Cisco01",
    "hostkey_verify": False
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback1351",
        "description": "test_from_restconf",
        "type": "iana-if-type:softwareLoopback",
        "enabled": "true",
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "1.1.1.61",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}
jpayload = json.dumps(payload)

payload = {"ietf-interfaces:enabled": "true"}
jpayload = json.dumps(payload)
payload = {
    "ietf-ip:address": [
        {
            "ip": "10.255.255.3",
            "netmask": "255.255.255.0"
        }
    ]
}


url = f"https://{wlc['host']}:{wlc['http_port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback1351/description"

response = requests.put(url=url, headers=headers, auth=(
    wlc["username"],
    wlc["password"]),
    data=jpayload,
    verify=False)

print(response)
print(response.text)


url = f"https://{wlc['host']}:{wlc['http_port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback1351/description"
get_response = requests.get(url=url, headers=headers, auth=(
    wlc["username"], wlc["password"]), verify=False).json()

print(json.dumps(get_response, indent=4))
