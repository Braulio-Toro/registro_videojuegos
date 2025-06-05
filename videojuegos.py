#Consolas de videojuegos
import os, time, msvcrt

menu=f"""\n--- MENÚ DE VIDEOJUEGOS ---
1) Registrar videojuegos
2) Ver videojuegos
3) Modificar videojuego
4) Eliminar videojuego
5) Salir
{"-"*30}"""
videojuegos=[]

plataformas=("PC", "PS5", "Xbox Series X", "Nimtendo Switch")

while True:
    os.system("cls || clear")
    print(menu)
    opc=input("Ingrese una opción (1-5): ")
    os.system("cls || clear")
    if opc=="1":
        codigo=int(input("Ingrese el código del videojuego: "))
        nombre=input("Ingrese el nombre del videojuego: ")
        genero=input("Ingrese el género del videojuego: ")
        print(f"""\nPLATAFORMAS DISPONIBLES: 
1) PC
2) PS5
3) Xbox Series X
4) Nintendo Switch
""")
        plataforma_codigo=int(input("Seleccione el número de la plataforma: "))
        plataforma=plataformas[plataforma_codigo - 1]
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
            print((f"-"*30))
            print("\nPresione cualquier tecla para continuar...")
            msvcrt.getch()
    elif opc=="3":
        codigo=int(input("Ingrese el código del juego a modificar: "))
        encontrado=False
        for v in videojuego:
            if v[codigo]==codigo:
                v["nombre"]=input("Nuevo Nombre: ")
                v["genero"]=input("Nuevo género: ")
                print(f"""\nPLATAFORMAS DISPONIBLES: 
1) PC
2) PS5
3) Xbox Series X
4) Nintendo Switch
""")
                plataforma_codigo=int(input("Seleccione el número de la plataforma: "))
                v["plataforma"]=plataformas[plataforma_codigo - 1]
                print("Videojuego modificado correctamente.")
                encontrado=True
            if not encontrado:
                print("Videojuego no encontrado.")
    elif opc=="4":
        pass
    elif opc=="5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción invalida")
        