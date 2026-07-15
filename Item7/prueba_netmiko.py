from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.81",
    "username": "admin",
    "password": "cisco123"
}

conexion = ConnectHandler(**router)

print("Conexion exitosa al router")

conexion.disconnect()
