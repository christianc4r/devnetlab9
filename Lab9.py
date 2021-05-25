loop=True
equipments=[]

while loop:
    print("Bienvenido, que desea ingresar?:")
    print("1- Switches.")
    print("2- Routers.")
    print("3- Firewall.")
    print("4- Ver todos los equipos.")
    opt = int(input())
    name = ""
    equipment={}
    if opt == 1:
        print("Ingrese el nombre del Switch")
        name=input()
        equipment["Switch"]=name
        equipments.append(equipment)
    elif opt == 2:
        print("Ingrese el nombre del Router")
        name=input()
        equipment["Router"]=name
        equipments.append(equipment)
    elif opt == 3:
        print("Ingrese el nombre del Firewall")
        name=input()
        equipment["Firewall"]=name
        equipments.append(equipment)
    print("SWITCHS EN EL SISTEMA")
    for i in equipments:
        print(i["Switch"])
    print("ROUTERS EN EL SISTEMA")
    for i in equipments:
        print(i["Router"])
    print("Firewalls EN EL SISTEMA")
    for i in equipments:
        print(i["Firewall"])

        
    