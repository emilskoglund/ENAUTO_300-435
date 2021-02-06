import requests
import json
from pprint import pprint
import urllib3

# Suppress warnings about certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

router = {
    "host": "192.168.1.30",
    "port": 443,
    "user": "cisco",
    "password": "Cisco123"
}

wlc = {
    "host": "192.168.1.19",
    "username": "admin",
    "http_port": 443,
    "password": "Cisco01",
    "hostkey_verify": False
}

n9k = {
    "host": "127.0.0.1",
    "username": "skoglunde",
    "http_port": 1025,
    "password": "6Fem4321",
    "hostkey_verify": False
}

sandbox_csr = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": 10000,
    "http_port": 9443,
    "username": "developer",
    "password": "C1sco12345",
    "hostkey_verify": False
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = f"https://{n9k['host']}:{n9k['http_port']}/restconf/data/netconf-state/capabilities"


response = requests.get(url=url, headers=headers, auth=(
    n9k["username"], n9k["password"]), verify=False)


if response.status_code == 200:
    response_dict = response.json()
    for capability in response_dict["ietf-netconf-monitoring:capabilities"]["capability"]:
        print(capability)