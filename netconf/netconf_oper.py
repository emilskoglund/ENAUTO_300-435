import os
import json
import yaml
import xmltodict
from ncclient import manager


def get_oper_data(
    host: str,
    username: str,
    password: str,
    filter: str,
    hostkey_verify: bool = False,
    allow_agent: bool = False,
    look_for_keys: bool = False,
    filter_method: str = "xpath",
    **kwargs,
):

    connect_params = {
        "host": host,
        "username": username,
        "password": password,
        "hostkey_verify": hostkey_verify,
        "allow_agent": allow_agent,
        "look_for_keys": look_for_keys,
    }

    with manager.connect(**connect_params) as conn:
        print(f"NETCONF session connected: {connect_params['host']}")

        resp = conn.get(filter=(filter_method, filter))

        jresp = xmltodict.parse(resp.xml)

        return jresp["rpc-reply"]["data"]


def get_config_data(
    host: str,
    username: str,
    password: str,
    filter: str,
    hostkey_verify: bool = False,
    allow_agent: bool = False,
    look_for_keys: bool = False,
    filter_method: str = "xpath",
    **kwargs,
):

    connect_params = {
        "host": host,
        "username": username,
        "password": password,
        "hostkey_verify": hostkey_verify,
        "allow_agent": allow_agent,
        "look_for_keys": look_for_keys,
    }

    with manager.connect(**connect_params) as conn:
        print(f"NETCONF session connected: {connect_params['host']}")

        resp = conn.get_config(source="running", filter=(filter_method, filter))

        jresp = xmltodict.parse(resp.xml)

        return jresp["rpc-reply"]["data"]
