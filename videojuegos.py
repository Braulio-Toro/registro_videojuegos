# Consolas de videojuegos
import os, time, msvcrt

menu=f"""\n--- MENÚ DE VIDEOJUEGOS ---
1) Registrar videojuegos
2) Ver videojuegos
3) Modificar videojuego
4) Eliminar videojuego
5) Salir
{"-"*30}"""
videojuegos=[]

plataformas=("PC", "PS5", "Xbox Series X", "Nintendo Switch")

while True:
    os.system("cls || clear")
    print(menu)
    opc=input("Ingrese una opción (1-5): ")
    os.system("cls || clear")
    if opc=="1":
        while True:
            try:
                codigo=int(input("Ingrese el código del videojuego: "))
                break
            except ValueError:
                print("ERROR! Debe ingresar un valor válido\n")
                time.sleep(2)
        while True:
            nombre=input("Ingrese el nombre del videojuego: ").strip().title()
            if len(nombre)<3:
                print("El nombre debe tener más de dos letras\n")
            else:
                break
        while True:
            genero=input("Ingrese el género del videojuego: ").strip().title()
            if len(genero)<3:
                print("El genero debe tener más de dos letras\n")
            else:
                break
        
        print(f"""\nPLATAFORMAS DISPONIBLES: 
1) PC
2) PS5
3) Xbox Series X
4) Nintendo Switch
""")
        while True:
            try:
                plataforma_codigo=int(input("Seleccione el número de la plataforma: "))
                plataforma=plataformas[plataforma_codigo - 1]
                if 1<=plataforma_codigo<=4:
                    break
                else:
                    print("Debe ser un número entre 1 y 4")
            except ValueError:
                print("ERROR! Debe ingresar un valor válido.\n")
            time.sleep(1)
        videojuego={
            "codigo":codigo,
            "nombre":nombre,
            "genero":genero,
            "plataforma":plataforma
        }
        videojuegos.append(videojuego)
        print("Videojuego registrado correctamente.")
    elif opc=="2":
        if len(videojuegos)==0:
            print("No hay videojuegos registrados.")
        else:
            print("\n--- LISTA DE VIDEOJUEGOS ---\n")
            for v in videojuegos:
                for key in v:
                    print(key, "=>", v[key])
                print(f"-"*30)
        print("\nPresione cualquier tecla para continuar...")
        msvcrt.getch()
    elif opc=="3":
        while True:
            try:
                codigo=int(input("Ingrese el código del juego a modificar: "))
                break
            except ValueError:
                print("ERROR! Debe ingresar un valor válido.\n")
        encontrado=False
        for v in videojuegos:
            if v["codigo"]==codigo:
                while True:
                    v["nombre"]=input("Nuevo Nombre: ").strip().title()
                    if len(v["nombre"])<3:
                        print("El nombre debe tener más de dos letras")
                    else:
                        break
                while True:
                    v["genero"]=input("Nuevo género: ").strip().title()
                    if len(v["genero"])<3:
                        print("El nombre debe tener más de dos letras.\n")
                    else:
                        break                   
                print(f"""\nPLATAFORMAS DISPONIBLES: 
1) PC
2) PS5
3) Xbox Series X
4) Nintendo Switch
""")
                while True:
                    try:
                        plataforma_codigo=int(input("Seleccione el número de la plataforma: "))
                        plataforma=plataformas[plataforma_codigo - 1]
                        if 1<=plataforma_codigo<=4:
                            break
                        else:
                            print("Debe ser un número entre 1 y 4")
                    except ValueError:
                        print("ERROR! Debe ingresar un valor válido.\n")
                    time.sleep(2)
                v["plataforma"]=plataformas[plataforma_codigo - 1]
                print("Videojuego modificado correctamente.")
                encontrado=True
                break
        if not encontrado:
            print("Videojuego no encontrado.")
    elif opc=="4":
        while True:
            try:
                codigo=int(input("Ingrese el código del videojuego que desea eliminar: "))
                break
            except ValueError:
                print("ERROR! Debe ingresar un valor válido.\n")
                time.sleep(2)
        eliminado=False
        for v in videojuegos:
            if v["codigo"]==codigo:
                videojuegos.remove(v)
                print("Videojuego eliminado correctamente.")
                eliminado=True
                break
        if not eliminado:
            print("Videojuego no encontrado.")
        time.sleep(3)
    elif opc=="5":
        print("Saliendo del programa.")
        time.sleep(0.5)
        break
    else:
        print("Opción invalida")
        time.sleep(3)