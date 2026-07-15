from ncclient import manager


router = {
    "host": "192.168.1.81",
    "port": 830,
    "username": "cisco",
    "password": "cisco123",
    "hostkey_verify": False
}


with manager.connect(**router) as m:

    print("Conexion NETCONF exitosa")

    for capability in m.server_capabilities:
        print(capability)


