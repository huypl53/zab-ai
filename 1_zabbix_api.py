import json
import requests
import urllib3
from tqdm import tqdm
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ZABBIX_139_URL = "https://210.152.99.139/zabbix/api_jsonrpc.php"
ZABBIX_49_URL = "https://210.152.84.49/zabbix/api_jsonrpc.php"
ZABBIX_172_URL = "https://210.152.81.172/zabbix/api_jsonrpc.php"

USERNAME_139 = "HapinS"
USERNAME_49 = "Hapins"
USERNAME_172 = "Hapins"
PASSWORD = "k4YKy3kS"
HEADERS = {"Content-Type": "application/json"}


def zabbix_login(url, username, password):
    payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": password
        },
        "id": 1,
        "auth": None
    }
    # SSL verification bypassed
    response = requests.post(url, headers=HEADERS, json=payload, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()["result"]


def zabbix_api_request(url, method, params, auth_token):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "auth": auth_token,
        "id": 1
    }
    response = requests.post(url, headers=HEADERS, json=payload, verify=False)
    return response.json()


def get_all_items(url, auth_token, host_id):
    payload = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "extend",
            "hostids": host_id,
            "sortfield": "name"
        },
        "auth": auth_token,
        "id": 1
    }
    response = requests.post(url, headers=HEADERS, json=payload, verify=False)
    response.raise_for_status()
    return response.json()["result"]


def get_hosts(url, auth_token):
    payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": "extend"
        },
        "auth": auth_token,
        "id": 1
    }
    response = requests.post(url, headers=HEADERS, json=payload, verify=False)
    response.raise_for_status()
    return response.json()["result"]


def get_all_items(url, auth_token, host_id):
    payload = {
        'jsonrpc': '2.0',
        'method': 'item.get',
        'params': {
            'output': 'extend',
            'hostids': host_id,
            'sortfield': 'name'
        },
        'auth': auth_token,
        'id': 1
    }
    response = requests.post(url, headers=HEADERS, json=payload, verify=False)
    response.raise_for_status()
    return response.json()['result']


def get_history(url, auth_token, itemid, limit=10):
    payload = {
        "jsonrpc": "2.0",
        "method": "history.get",
        "params": {
            "output": "extend",
            "history": 0,
            "itemids": itemid,
            "sortfield": "clock",
            "sortorder": "DESC",
            "limit": limit
        },
        'auth': auth_token,
        "id": 1
    }
    response = requests.post(url, headers=HEADERS, json=payload, verify=False)
    response.raise_for_status()
    return response.json()['result']


def get_trend(url, auth_token, itemid, limit=10):
    payload = {
        "jsonrpc": "2.0",
        "method": "trend.get",
        "params": {
            "output": "extend",
            "history": 0,
            "itemids": itemid,
            "sortfield": "clock",
            "sortorder": "DESC",
            "limit": limit
        },
        'auth': auth_token,
        "id": 1
    }
    response = requests.post(url, headers=HEADERS, json=payload, verify=False)
    response.raise_for_status()
    return response.json()['result']


#########################
### For 210.152.99.139 ###
#########################
try:
    # Get the authentication token
    AUTHEN_TOKEN_139 = zabbix_login(ZABBIX_139_URL, USERNAME_139, PASSWORD)
    print(f"Authentication token: {AUTHEN_TOKEN_139}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


def get_history_99_139():
    print("Begin fetch data from [210.152.99.139] Zabbix server")

    hosts = get_hosts(ZABBIX_139_URL, AUTHEN_TOKEN_139)
    with open("210.152.99.139/hosts_list.json", "w") as f:
        json.dump(hosts, f, indent=4)

    items_list = []
    for host in tqdm(hosts, total=len(hosts)):
        items = get_all_items(ZABBIX_139_URL, AUTHEN_TOKEN_139, host["hostid"])
        if len(items):
            items_list.extend(items)
            with open(f"210.152.99.139/items_list_{host['host']}.json", "w") as f:
                json.dump(items, f, indent=4)

    for item in tqdm(items_list, total=len(items_list)):
        history = get_history(ZABBIX_139_URL, AUTHEN_TOKEN_139, item["itemid"])
        if history:
            with open(f"210.152.99.139/item_history_{item['itemid']}.json", "w") as f:
                json.dump(history, f, indent=4)

    print("Done")


def get_trend_99_139():
    print("Begin fetch data from [210.152.99.139] Zabbix server")

    hosts = get_hosts(ZABBIX_139_URL, AUTHEN_TOKEN_139)
    with open("210.152.99.139/hosts_list.json", "w") as f:
        json.dump(hosts, f, indent=4)

    items_list = []
    for host in tqdm(hosts, total=len(hosts)):
        items = get_all_items(ZABBIX_139_URL, AUTHEN_TOKEN_139, host["hostid"])
        if len(items):
            items_list.extend(items)
            with open(f"210.152.99.139/items_list_{host['host']}.json", "w") as f:
                json.dump(items, f, indent=4)

    for item in tqdm(items_list, total=len(items_list)):
        trend = get_trend(ZABBIX_139_URL, AUTHEN_TOKEN_139, item["itemid"])
        if trend:
            with open(f"210.152.99.139/item_trend_{item['itemid']}.json", "w") as f:
                json.dump(trend, f, indent=4)

    print("Done")


#########################
### For 210.152.84.49 ###
#########################
try:
    # Get the authentication token
    AUTHEN_TOKEN_49 = zabbix_login(ZABBIX_49_URL, USERNAME_49, PASSWORD)
    print(f"Authentication token: {AUTHEN_TOKEN_49}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


def get_history_84_49():
    print("Begin fetch data from [210.152.84.49] Zabbix server")
    hosts = get_hosts(ZABBIX_49_URL, AUTHEN_TOKEN_49)
    with open("210.152.84.49/hosts_list.json", "w") as f:
        json.dump(hosts, f, indent=4)

    items_list = []
    for host in tqdm(hosts, total=len(hosts)):
        items = get_all_items(ZABBIX_49_URL, AUTHEN_TOKEN_49, host["hostid"])
        if len(items):
            items_list.extend(items)
            with open(f"210.152.84.49/items_list_{host['host']}.json", "w") as f:
                json.dump(items, f, indent=4)

    for item in tqdm(items_list, total=len(items_list)):
        history = get_history(ZABBIX_49_URL, AUTHEN_TOKEN_49, item["itemid"])
        if history:
            with open(f"210.152.84.49/item_history_{item['itemid']}.json", "w") as f:
                json.dump(history, f, indent=4)

    print("Done")


#########################
### For 210.152.81.172 ###
#########################
def get_history_81_172():
    try:
        # Get the authentication token
        AUTHEN_TOKEN_172 = zabbix_login(ZABBIX_172_URL, USERNAME_172, PASSWORD)
        print(f"Authentication token: {AUTHEN_TOKEN_172}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    print("Begin fetch data from [210.152.81.172] Zabbix server")

    hosts = get_hosts(ZABBIX_172_URL, AUTHEN_TOKEN_172)
    with open("210.152.81.172/hosts_list.json", "w") as f:
        json.dump(hosts, f, indent=4)

    items_list = []
    for host in tqdm(hosts, total=len(hosts)):
        items = get_all_items(ZABBIX_172_URL, AUTHEN_TOKEN_172, host["hostid"])
        if len(items):
            items_list.extend(items)
            with open(f"210.152.81.172/items_list_{host['host']}.json", "w") as f:
                json.dump(items, f, indent=4)

    for item in tqdm(items_list, total=len(items_list)):
        history = get_history(ZABBIX_172_URL, AUTHEN_TOKEN_172, item["itemid"])
        if history:
            with open(f"210.152.81.172/item_history_{item['itemid']}.json", "w") as f:
                json.dump(history, f, indent=4)

    print("Done")


def get_trend_81_172():
    try:
        # Get the authentication token
        AUTHEN_TOKEN_172 = zabbix_login(ZABBIX_172_URL, USERNAME_172, PASSWORD)
        print(f"Authentication token: {AUTHEN_TOKEN_172}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    print("Begin fetch data from [210.152.81.172] Zabbix server")

    hosts = get_hosts(ZABBIX_172_URL, AUTHEN_TOKEN_172)
    with open("210.152.81.172/hosts_list.json", "w") as f:
        json.dump(hosts, f, indent=4)

    items_list = []
    for host in tqdm(hosts, total=len(hosts)):
        items = get_all_items(ZABBIX_172_URL, AUTHEN_TOKEN_172, host["hostid"])
        if len(items):
            items_list.extend(items)
            with open(f"210.152.81.172/items_list_{host['host']}.json", "w") as f:
                json.dump(items, f, indent=4)

    for item in tqdm(items_list, total=len(items_list)):
        trend = get_trend(ZABBIX_172_URL, AUTHEN_TOKEN_172, item["itemid"])
        if trend:
            with open(f"210.152.81.172/item_trend_{item['itemid']}.json", "w") as f:
                json.dump(trend, f, indent=4)

    print("Done")


# get_trend_99_139()
get_trend_81_172()
