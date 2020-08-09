import sys
from datetime import date
import ClasesDCC
print(f"""Bienvenid@ a DCCahuin!
Seleccione una opción:""")
while True:
    print(f"""[1] Iniciar sesión
""" """[2] ¿Eres nuev@? Registra tu usuario
""" """[0] Salir""")
    respuesta = input()
    if respuesta == "1":  # Iniciar Sesión #
        print("Ingrese nombre de usuario:")
        usuario_ingresado = input()
        if ClasesDCC.usuario.iniciar_sesion(usuario_ingresado) == 1:  # Entró el usuario #
            while True:
                print(f"""[1] Menú de prograposts
"""             """[2] Menú de seguidores
"""             """[0] Salir""")
                eleccion_de_menu = input()
                if eleccion_de_menu == "1":
                    print(f"""[1] Crear prograpost
"""                 """[2] Eliminar prograpost
"""                 """[3] Tus prograpost
"""                 """[4] Tu muro (aquí están los prograposts """
                    """de los usuarios que sigues)
"""                 """[0] Volver a la selección de menú""")
                    decision_menu_prograpost = input()
                    if decision_menu_prograpost == "1":  # Crear prograpost #
                        print(f"Escribe tu prograpost, recuerda "
                        "que debe tener 1-140 caracteres")
                        fecha_hoy = str(date.today())
                        user = usuario_ingresado
                        if ClasesDCC.posts.crear_prograpost(user, fecha_hoy, input()) == 1:
                            pass
                        else:
                            print(f"Tu prograpost no cumple con los limites de caracteres")
                            pass
                    elif decision_menu_prograpost == "2":  # Eliminar prograpost #
                        ClasesDCC.posts.eliminar_prograpost(usuario_ingresado)
                                                      
                    elif decision_menu_prograpost == "3":  # Tus prograpost #
                        print(f"""Indica en qué orden los quieres ver
"""                     """[1] Ascendente
"""                     """[2] Descendiente""")
                        orden_e = input()
                        if orden_e == "1" or orden_e == "2":                            
                            ClasesDCC.posts.ver_prograposts_propios(usuario_ingresado, int(orden_e))
                        else:
                            print("Esa opción no existe, vuelves al menú")
                            pass
                    elif decision_menu_prograpost == "4":  # Tu muro #
                        print(f"""Indica en qué orden los quieres ver
"""                     f"""[1] Ascendente
"""                     f"""[2] Descendiente""")
                        orden_1_2 = input()
                        if orden_1_2 == "1" or orden_1_2 == "2":                            
                            ClasesDCC.posts.ver_prograposts_seguidos(usuario_ingresado, int(orden_1_2))
                        else:
                            print("Esa opción no existe, vuelves al menú")
                            pass
                    
                    elif decision_menu_prograpost == "0": # Equivocacion de tecla #
                        pass
                    else:
                        print(f"No existe esa opción, está de vuelta en el menú")

                elif eleccion_de_menu == "2": # Menu de seguidores #
                    print(f"""[1] Seguir un usuario
"""                 f"""[2] Dejar de seguir a un usuario
"""                 f"""[0] Volver a la selección de menú""")
                    decision_menu_seguidos = input()
                    if decision_menu_seguidos == "1": # Seguir un usuario #
                        print(f"Ingrese el nombre del usuario que quiere seguir")
                        ClasesDCC.seguidos.seguir(usuario_ingresado, input())
                    elif decision_menu_seguidos == "2": # Dejar de seguir a un usuario #
                        print(f"Ingrese el nombre del usuario que quiere "
                        "dejar de seguir")
                        ClasesDCC.seguidos.dejar_de_seguir(usuario_ingresado, input())             
                    elif decision_menu_seguidos == 0:
                        pass
                    else:
                        print(f"No existe esa opción")
                        pass
                
                elif eleccion_de_menu == "0": # Salir #
                    sys.exit()

                else: # Equivoación de tecla #
                    print(f"No existe esa opción")

        else: # Error iniciar sesión #
            print("El nombre de usuario no está registrado")

    elif respuesta == "2": # Resgistrarse #
        print(f"Escriba el nombre de usuario que desea tener, "
        "debe contener más de 8 caracteres alfanumericos y "
        "mínimo una letra y un número")
        nuevo_usuario_registrado = input()
        if ClasesDCC.usuario.registrar(nuevo_usuario_registrado) == 1: #Registro sin errores #
            print(f"Bienvenid@ {nuevo_usuario_registrado}, ahora eres "
            "parte de DCCahuin, proceda a iniciar sesión")

        else: # Error Registro #
            pass

    elif respuesta == "0":  #S alir #
        sys.exit()
    
    else:  # Equivocacion de tecla #
        print(f"No existe esa opción")