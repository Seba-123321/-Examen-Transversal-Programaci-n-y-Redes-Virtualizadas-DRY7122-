from ncclient import manager

router = {
    "host": "192.168.1.81",
    "port": 830,
    "username": "admin",
    "password": "cisco123",
    "hostkey_verify": False
}

config = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <hostname>SEBASTIAN-GONZALEZ</hostname>
 </native>
</config>
"""

with manager.connect(**router) as m:

    respuesta = m.edit_config(
        target="running",
        config=config,
        default_operation="merge"
    )

    print("Hostname cambiado correctamente")
    print(respuesta)
