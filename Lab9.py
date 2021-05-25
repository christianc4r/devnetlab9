loop=True
equipment={"Switch":[], "Router":[], "Firewall":[]}

while loop:
    print("Bienvenido, que desea ingresar?:")
    print("1- Switches.")
    print("2- Routers.")
    print("3- Firewall.")
    print("4- Salir")
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
    print("***************************************************************************")