import os
from datetime import datetime

loop=True
equipment={"Switch":[], "Router":[], "Firewall":[]}
options=["1","2","3","4","5"]

def export():
    date=str(datetime.now())
    filer = open("Routers.txt","w+")
    files = open("Switches.txt","w+")
    filef = open("Firewalls.txt","w+")
    print("***********Exportando archivos**************")
    files.write("**Switches en el sistema**"+date+os.linesep)
    filer.write("**Routers en el sistema**"+date+os.linesep)
    filef.write("**Firewalls en el sistema**"+date+os.linesep)
    for i in equipment["Switch"]:
        files.write(i+os.linesep)
    for i in equipment["Router"]:
        filer.write(i+os.linesep)
    for i in equipment["Firewall"]:
        filef.write(i+os.linesep)
    files.close()
    files.close()
    filef.close()
    print("***********Archivos exportados**************")

while loop:
    print("Bienvenido, que desea ingresar?:")
    print("1- Switches.")
    print("2- Routers.")
    print("3- Firewall.")
    print("4- Exportar dispositivos a .txt")
    print("5- Salir")
    opt = input()
    if opt in options:
        opt = int (opt)
    else:
        print("Opcion incorrecta, vuelve a intentarlo")
        continue
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
        export()
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
    print("***************************************************************************")