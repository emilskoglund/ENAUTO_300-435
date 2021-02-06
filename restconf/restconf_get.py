import requests
import json
from rich.console import Console
from rich.table import Table

from dotenv import load_dotenv
from getpass import getpass
import os


console = Console()

load_dotenv()

# Suppress warnings about certificates
requests.packages.urllib3.disable_warnings()


def check_dotenv(env_var: str, secret: bool = True):
    phrase = f"{env_var} not defined in '.env' file: "
    return (
        os.getenv(env_var)
        if os.getenv(env_var)
        else getpass(phrase)
        if secret
        else input(phrase)
    )

def test_log(data):
    enabled = False
    console.log("Hello from", console, "!")
    console.log(data)


USERNAME = check_dotenv("RESTCONF_USERNAME", secret=False)
PASSWORD = check_dotenv("RESTCONF_PASSWORD")

device_param = {
    "host": "192.168.1.19",
    "http_port": 443,
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

# ## Get interface address config using ietf yang data model
# endpoint = "restconf/data/ietf-interfaces:interfaces/interface=Loopback1351"

# ## Get hostname configuration using Cisco-IOS-XE-native.yang
# endpoint = "restconf/data/Cisco-IOS-XE-native:native/hostname"

# ## Get primary interface address config using Cisco-IOS-XE-native.yang
endpoint = "restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=1351/ip/address/primary/"


url = f"https://{device_param['host']}:{device_param['http_port']}/{endpoint}"


response = requests.get(
    url=url, headers=headers, auth=(USERNAME, PASSWORD), verify=False
).json()

print(response.keys())