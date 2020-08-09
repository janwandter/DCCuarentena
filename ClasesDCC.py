import os
path_usuarios = os.path.join("ArchivosDCC", "usuarios.csv")
path_posts = os.path.join("ArchivosDCC", "posts.csv")
path_seguidores = os.path.join("ArchivosDCC", "seguidores.csv")

class Usuario:
    def __init__(self):
        self.lista_de_usuarios = []

    def iniciar_sesion(self, usuario_registrado):
        match_usuarios_existentes = 0
        for iterador_lista_de_usuarios in self.lista_de_usuarios:
            if iterador_lista_de_usuarios == [usuario_registrado]:
                match_usuarios_existentes += 1
            else:
                match_usuarios_existentes += 0
        if match_usuarios_existentes == 1:
            return 1
        else:
            return 0
              
    def registrar(self, nuevo_usuario):
        condiciones_nombres = 0
        letras = 0
        numeros = 0 
        for letras_o_numeros in nuevo_usuario:
            if letras_o_numeros.isalpha():
                letras += 1
            elif letras_o_numeros.isdecimal():
                numeros += 1
            else:
                pass
        for iterador1_lista_de_usuarios in self.lista_de_usuarios:
            if iterador1_lista_de_usuarios == [nuevo_usuario]:
                condiciones_nombres += 1
        if condiciones_nombres == 0 and nuevo_usuario.isalnum() and letras > 0  \
                                        and numeros > 0 and len(nuevo_usuario) >= 8:
            with open(path_usuarios, "a") as archivo1:
                archivo1.write(nuevo_usuario+"\n")
            usuario.lista_de_usuarios = []
            with open(path_usuarios, "rt") as archivo:
                lineas_usuarios = archivo.readlines()
                for linea_usuario in lineas_usuarios:
                    fila_usuario = linea_usuario.strip().split(',')
                    usuario.lista_de_usuarios.append(fila_usuario)
            with open(path_seguidores, "a", encoding = "utf8") as archivo:
                archivo.write(f"{nuevo_usuario}\n")
            with open(path_seguidores, "rt", encoding = "utf8") as archivo:
                lineas_seguidos = archivo.readlines()
            for linea_seguidos in lineas_seguidos:
                fila_seguidos = linea_seguidos.strip().split(",", maxsplit = 2)
                seguidos.lista_de_seguidos.append(fila_seguidos)     
            return 1
        else:
            print(f"El nombre de usuario ya se encuentra en uso, "
            "o no cumple con los requisitos")
            return 0 

# Seguidos se refiere a las personas que el usuario sigue#
class Seguidos:
    def __init__(self):
        self.lista_de_seguidos = []
# El primer elemento de cafa elemento de lista_de_seguidos es el usuario correspondiente#    
    def seguir(self, nombre_del_usuario, nuevo_seguido):
        if nombre_del_usuario == nuevo_seguido:
            print(f"No puedes seguirte")
            return 0
        contador_usuarios_existentes = 0
        for iterador_lista_de_usuarios in usuario.lista_de_usuarios:
            if nuevo_seguido in iterador_lista_de_usuarios:
                contador_usuarios_existentes += 1
        if contador_usuarios_existentes == 0:
            print(f"No existe el usuario: {nuevo_seguido}")
            return 0
        for index_nombre_de_usuario in range(len(self.lista_de_seguidos)):
            if nombre_del_usuario == self.lista_de_seguidos[index_nombre_de_usuario][0]:
                if nuevo_seguido not in self.lista_de_seguidos[index_nombre_de_usuario]:
                    self.lista_de_seguidos[index_nombre_de_usuario].append(nuevo_seguido)
                    with open(path_seguidores, "w", encoding = "utf8") as archivo:
                        for lineas_lista_de_seguidores in self.lista_de_seguidos:
                            linea_momentanea = ""
                            for strings_en_lineas in lineas_lista_de_seguidores:
                                linea_momentanea += (strings_en_lineas+",")    
                            archivo.write(f"{linea_momentanea[:-1]}\n")
                    seguidos.lista_de_seguidos = []
                    with open(path_seguidores, "rt", encoding = "utf8") as archivo:
                        lineas_seguidos = archivo.readlines()
                    for linea_seguidos in lineas_seguidos:
                        fila_seguidos = linea_seguidos.strip().split(",")
                        seguidos.lista_de_seguidos.append(fila_seguidos)
                else:
                    print(f"Usted ya sigue al usuario \"{nuevo_seguido}\"")
    
    def dejar_de_seguir(self, nombre_del_usuario, seguido_eliminado):
        for index_usuario_seguidos in range(len(self.lista_de_seguidos)):
            if nombre_del_usuario == self.lista_de_seguidos[index_usuario_seguidos][0]:
                if seguido_eliminado in self.lista_de_seguidos[index_usuario_seguidos]:
                    elemento_a_sacar = self.lista_de_seguidos[index_usuario_seguidos].index(seguido_eliminado)
                    self.lista_de_seguidos[index_usuario_seguidos].pop(elemento_a_sacar)
                else:
                    print(f"No sigues al usuario: {seguido_eliminado}")
                    return 0
        with open(path_seguidores, "w", encoding = "utf8") as archivo:
            for lineas_lista_de_seguidores in self.lista_de_seguidos:
                linea_momentanea = ""
                for strings_en_lineas in lineas_lista_de_seguidores:
                    linea_momentanea += (strings_en_lineas+",")    
                archivo.write(f"{linea_momentanea[:-1]}\n")
        seguidos.lista_de_seguidos = []
        with open(path_seguidores, "rt", encoding = "utf8") as archivo:
            lineas_seguidos = archivo.readlines()
        for linea_seguidos in lineas_seguidos:
            fila_seguidos = linea_seguidos.strip().split(",")
            seguidos.lista_de_seguidos.append(fila_seguidos)
        
class Posts:
    def __init__(self):
        self.lista_de_posts=[]

    def crear_prograpost(self, usuario_creador, fecha, cuerpo_creado): 
        if 1<=len(cuerpo_creado) and len(cuerpo_creado) <= 140:
                fecha_formateada = fecha.replace("-", "/")
                with open(path_posts, "a", encoding = "utf8") as archivo1:
                    archivo1.write(f"{usuario_creador},{fecha_formateada},{cuerpo_creado}\n")
                posts.lista_de_posts = []
                with open(path_posts, "rt", encoding = "utf8") as archivo:
                    lineas_posts = archivo.readlines()
                for linea_posts in lineas_posts:
                    fila_posts = linea_posts.strip().split(",", maxsplit = 2)
                    posts.lista_de_posts.append(fila_posts)
                return 1
        else:
            return 0
            
    def ver_prograposts_propios(self, nombre_del_usuario, orden):
        lista_copia_de_prograpost = self.lista_de_posts
        contador_prograpost_propios = 0
        lista_orden_elegido = sorted(lista_copia_de_prograpost,  \
                                    key = lambda orden_fecha: orden_fecha[1], reverse = (2 == orden)) #si es True es descendiente
        for iterador_lista_de_prograpost in lista_orden_elegido:
            if iterador_lista_de_prograpost[0] == nombre_del_usuario:
                print(iterador_lista_de_prograpost[1])
                print(iterador_lista_de_prograpost[2])
                contador_prograpost_propios = 1
        if contador_prograpost_propios == 1:
            return 0
        else:
            return (print(f"No tienes prograpost aún"))

    def eliminar_prograpost(self, nombre_del_usuario):
        lista_posibles_eliminados = []
        lista_momentanea_copia = []
        print(f"Indique el post que desea eliminar")
        for iterador_numerico in range(len(self.lista_de_posts)):
            if self.lista_de_posts[iterador_numerico][0] == nombre_del_usuario:
                lista_momentanea_copia = self.lista_de_posts[iterador_numerico].copy()
                lista_momentanea_copia.append(iterador_numerico)
                lista_posibles_eliminados.append(lista_momentanea_copia)
        for iterador_numerico_prograpost_propios in range(len(lista_posibles_eliminados)):
            opcion_numero = iterador_numerico_prograpost_propios
            fecha_prograpost = lista_posibles_eliminados[iterador_numerico_prograpost_propios][1]
            cuerpo_prograpost = lista_posibles_eliminados[iterador_numerico_prograpost_propios][2]
            print(f"""[{opcion_numero}] {fecha_prograpost}
    """             f"""{cuerpo_prograpost}""")
        if len(lista_posibles_eliminados) == 0:
            print("Usted no tiene prograposts, está de vuelta en el menú")
            return 0
        print(f"[s] Volver al menu")
        seleccion_de_eliminar = input()
        if seleccion_de_eliminar == "s":
            pass
        else:
            prograpost_eliminado = lista_posibles_eliminados[int(seleccion_de_eliminar)][3]
            self.lista_de_posts.pop(prograpost_eliminado)
            with open(path_posts, "w", encoding = "utf8") as archivo:
                for lineas_lista_de_post in self.lista_de_posts:
                    linea_momentanea = ""
                    for strings_en_lineas in lineas_lista_de_post:
                        linea_momentanea += (str(strings_en_lineas)+",")    
                    archivo.write(f"{linea_momentanea[:-1]}\n") #borra la ultima coma
            posts.lista_de_posts = []   
            with open(path_posts, "rt", encoding = "utf8") as archivo:
                lineas_posts = archivo.readlines()
            for linea_posts in lineas_posts:
                fila_posts = linea_posts.strip().split(",", maxsplit = 2)
                posts.lista_de_posts.append(fila_posts)
    
    def ver_prograposts_seguidos(self, nombre_del_usuario, orden):
        lista_para_ordenar_prograposts = self.lista_de_posts
        contador_prograpost = 0
        for iterador_lista_de_seguidos in seguidos.lista_de_seguidos:
            if iterador_lista_de_seguidos[0] == nombre_del_usuario:
                lista_seguidos_usuario = iterador_lista_de_seguidos[1:] 
        lista_para_ordenar_prograposts = sorted(lista_para_ordenar_prograposts, \
                                key = lambda orden_fecha: orden_fecha[1], reverse = (2 == orden)) #si es True es descendiente
        for iterador_lista_de_prograpost in lista_para_ordenar_prograposts:
            if iterador_lista_de_prograpost[0] in lista_seguidos_usuario:
                usuario_post_seguido = iterador_lista_de_prograpost[0] 
                fecha_post_seguido = iterador_lista_de_prograpost[1]
                cuerpo_post_seguido = iterador_lista_de_prograpost[2]
                print(f"""{usuario_post_seguido}  {fecha_post_seguido}
"""             f"""{cuerpo_post_seguido}
"""             f"""""")
                contador_prograpost = 1
        if contador_prograpost == 1:
            return 0
        else:
            return (print(f"Tus seguidos no tienen prograpost aún"))        

#Instancias y lectura de archivos
usuario = Usuario()
with open(path_usuarios, "rt") as archivo:
    lineas_usuarios=archivo.readlines()
for linea_usuario in lineas_usuarios:
    fila_usuario = linea_usuario.strip().split(',')
    usuario.lista_de_usuarios.append(fila_usuario)
posts = Posts()
with open(path_posts, "rt", encoding = "utf8") as archivo:
    lineas_posts = archivo.readlines()
for linea_posts in lineas_posts:
    fila_posts = linea_posts.strip().split(",", maxsplit = 2)
    posts.lista_de_posts.append(fila_posts)
seguidos = Seguidos()
with open(path_seguidores, "rt", encoding = "utf8") as archivo:
    lineas_seguidos = archivo.readlines()
for linea_seguidos in lineas_seguidos:
    fila_seguidos = linea_seguidos.strip().split(",")
    seguidos.lista_de_seguidos.append(fila_seguidos)







        
    