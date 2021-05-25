loop=True
equipment={"Switch":[], "Router":[], "Firewall":[],"APs":[]}

while loop:
    print("Bienvenido, que desea ingresar?:")
    print("1- Switches.")
    print("2- Routers.")
    print("3- Firewall.")
    print("4- Aps.")
    print("5- Salir")
    opt = int(input())
    name = ""
    
    if opt == 1:
        print("Ingrese el nombre del Switch")
        name=input()
        equipment["Switch"].append(name)
    elif opt == 2:
        print("Ingrese el nombre del Router")
        name=input()
        equipment["Router"].append(name)
    elif opt == 3:
        print("Ingrese el nombre del Firewall")
        name=input()
        equipment["Firewall"].append(name)
    elif opt == 4:
        print("Ingrese el nombre del AP")
        name=input()
        equipment["APs"].append(name)
    elif opt == 5:
        loop=False
    print("***************************************************************************")
    print("SWITCHS EN EL SISTEMA")
    for i in equipment["Switch"]:
        print(i)
    print("ROUTERS EN EL SISTEMA")
    for i in equipment["Router"]:
       print(i)
    print("Firewalls EN EL SISTEMA")
    for i in equipment["Firewall"]:
        print(i)
    print("Aps EN EL SISTEMA")
    for i in equipment["APs"]:
        print(i)
    print("***************************************************************************")