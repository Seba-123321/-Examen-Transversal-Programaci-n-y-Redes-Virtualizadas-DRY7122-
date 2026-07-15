from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.81",
    "username": "admin",
    "password": "cisco123"
}

conexion = ConnectHandler(**router)

comandos = [
    "router eigrp EIGRP-NOMBRADO",

    "address-family ipv4 unicast autonomous-system 100",
    "network 192.168.1.0 0.0.0.255",
    "af-interface default",
    "passive-interface",
    "exit",

    "address-family ipv6 unicast autonomous-system 100",
    "af-interface default",
    "passive-interface",
    "exit"
]

resultado = conexion.send_config_set(comandos)

print(resultado)

conexion.save_config()

conexion.disconnect()
