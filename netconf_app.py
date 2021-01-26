from netconf import get_oper_data
from netconf import get_config_data
from pprint import pprint


# Memory operation data
xpath_filter_mem = "/memory-statistics/memory-statistic[name='Processor']"
sub_filter_mem = """
<memory-statistics xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-memory-oper">
  <memory-statistic>
    <name>Processor</name>
  </memory-statistic>
</memory-statistics>""".strip()

# CPU opeartional data
xpath_filter_cpu = ""
sub_filter_cpu = """
<cpu-usage xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-process-cpu-oper">
  <cpu-utilization/>
</cpu-usage>
""".strip()

# Vlans operational data
xpath_filter_oper_vlans = "/vlans/vlan/vlan-interfaces"
sub_filter_oper_vlans = """
<vlans xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-vlan-oper">
  <vlan/>
</vlans>""".strip()

# Usernam configurational data
xpath_filter_conf_username = "/native/username"
sub_filter_conf_username = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <username/>
</native>""".strip()

# Device conn params
device = {
    "name": "192.168.1.19",
    "role": "wlc",
    "username": "admin",
    "password": "Cisco01",
}

# Get operational data
vlan_data = get_oper_data(
    host=device["name"],
    username=device["username"],
    password=device["password"],
    filter=xpath_filter_oper_vlans,
)

# Get configurational data
vlan_conf = get_config_data(
    host=device["name"],
    username=device["username"],
    password=device["password"],
    filter=sub_filter_conf_username,
    filter_method='subtree'
)

print()
print("#" * 40, "VLANS operational data", "#" * 40)
print()
pprint(vlan_data)
print()
print("#" * 40, "VLANS operational data end", "#" * 40)

print()
print("#" * 40, "Username configurational data", "#" * 40)
print()
pprint(vlan_conf)
print()
print("#" * 40, "Username configurational data end", "#" * 40)
