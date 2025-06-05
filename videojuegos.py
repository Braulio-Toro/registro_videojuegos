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
        print(f"""PLATAFORMAS DISPONIBLES: 
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
        pass
    elif opc=="3":
        pass
    elif opc=="4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción invalida")
        