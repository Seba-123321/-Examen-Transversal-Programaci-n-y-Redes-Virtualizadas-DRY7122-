print("Clasificador de VLAN")

vlan = int(input("Ingrese numero de VLAN: "))


if vlan >= 1 and vlan <= 1005:
    print("VLAN rango normal")


elif vlan >=1006 and vlan <=4094:
    print("VLAN rango extendido")


else:
    print("VLAN incorrecta")
