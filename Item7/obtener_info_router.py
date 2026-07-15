from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.81",
    "username": "admin",
    "password": "cisco123",
}

conexion = ConnectHandler(**router)

print("=== INFORMACION DE INTERFACES ===")

interfaces = conexion.send_command("show ip interface brief")
print(interfaces)

print("\n=== RUNNING CONFIG EIGRP ===")

eigrp = conexion.send_command("show running-config | section eigrp")
print(eigrp)

print("\n=== VERSION DEL ROUTER ===")

version = conexion.send_command("show version")
print(version)

conexion.disconnect()
