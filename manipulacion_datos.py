import base_datos
import mysql.connector
import time
import os

def limpiar():
    if os.name =='nt':
        os.system('cls')

def ejecutar_consulta(query):
    conexion = base_datos.conectarBD()
    cursor = conexion.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def ejecutar_modificacion (query):
    conexion = base_datos.conectarBD()
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.close()

    
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"
    
class Alumno(Persona):
    def __init__(self, cedula, nombre, apellido, edad, promedio):
        super().__init__(nombre, apellido, edad)
        self.cedula = cedula
        self.promedio = promedio

    def __str__(self):
        return f"{self.cedula} {self.nombre} {self.apellido} {self.edad} Promedio: {self.promedio}"

    def guardar_alumno(self):
        conexion = base_datos.conectarBD()
        cursor = conexion.cursor()
        sql = "INSERT INTO ESTUDIANTES (CEDULA, NOMBRE, EDAD, PROMEDIO) VALUES (%s, %s, %s, %s)"
        nombre_completo = f"{self.nombre} {self.apellido}"
        valores = (self.cedula, nombre_completo, self.edad, self.promedio)
        try:
            cursor.execute(sql, valores)
            conexion.commit()
            print("Alumno guardado correctamente.")
        except mysql.connector.Error as err:
            print("Error al guardar:", err)
        finally:
            conexion.close()

    @staticmethod
    def actualizar_alumno(cedula, nombre, edad, nota1, nota2, nota3):
     try:
        ejecutar_modificacion(f"UPDATE ESTUDIANTES SET NOMBRE='{nombre}', EDAD='{edad}', NOTA1='{nota1}', NOTA2='{nota2}', NOTA3='{nota3}' WHERE CEDULA='{cedula}' ")
     except mysql.connector.Error as r:
        print("Error al actualizar: ",r)

    @staticmethod
    def eliminar_alumnos(cedula):
        try:
         ejecutar_modificacion(f"DELETE FROM ESTUDIANTES WHERE CEDULA='{cedula}' ")
        except mysql.connector.Error as r:
         print("Error al eliminar: ",r)

    @staticmethod
    def mostrar_todos():
        conexion = base_datos.conectarBD()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ESTUDIANTES")
        for fila in cursor.fetchall():
            print(fila)
        conexion.close()


class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, materia):
        super().__init__(nombre, apellido, edad)
        self.materia = materia
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.materia}"

class Curso:
    def __init__(self, nombre, profesor, alumnos=None):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = alumnos if alumnos else []
    
    def __str__(self):
        return f"{self.nombre} - Profesor: {self.profesor} - Alumnos: {len(self.alumnos)}"
    
    def obtener_alumnos(self):
        self.alumnos = ejecutar_consulta("SELECT * FROM ESTUDIANTES")
        return self.alumnos
    
    def obtener_profesor(self):
        self.profesor = ejecutar_consulta("SELECT * FROM PROFESORES")
        print(type(self.profesor))
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_cantidad_alumnos(self):
        return len(self.alumnos)

def obtener_cursos():
    return ejecutar_consulta("SELECT * FROM CURSOS")

def obtener_matriculas():
    return ejecutar_consulta("SELECT * FROM MATRICULAS")

def calcular_promedio():
    resultados = ejecutar_consulta("SELECT * FROM ESTUDIANTES")

    for i in resultados:
        print("-"*30)
        print(f"NOMBRE ESTUDIANTE:{i[1]}")
        print(f"NOTA1: {i[3]}")
        print(f"NOTA2: {i[4]}")
        print(f"NOTA3: {i[5]}")
        promedio = (i[3] + i[4] + i[5]) / 3
        print(f"PROMEDIO: {round(promedio, 2)}")

def insertar_alumnos(cedula, nombre, edad, nota1, nota2, nota3):
    try:
        ejecutar_modificacion(f"INSERT INTO ESTUDIANTES (CEDULA,NOMBRE, EDAD, NOTA1, NOTA2, NOTA3) VALUES ('{cedula}','{nombre}','{edad}','{nota1}','{nota2}','{nota3}')")
    except mysql.connector.Error as r:
        print("Error al insertar: ",r)

def actualizar_alumno(cedula, nombre, edad, nota1, nota2, nota3):
    try:
        ejecutar_modificacion(f"UPDATE ESTUDIANTES SET NOMBRE='{nombre}', EDAD='{edad}', NOTA1='{nota1}', NOTA2='{nota2}', NOTA3='{nota3}' WHERE CEDULA='{cedula}' ")
    except mysql.connector.Error as r:
        print("Error al actualizar: ",r)

def eliminar_alumnos(cedula):
    try:
        ejecutar_modificacion(f"DELETE FROM ESTUDIANTES WHERE CEDULA='{cedula}' ")
    except mysql.connector.Error as r:
        print("Error al eliminar: ",r)

def asignar_materia(estudiante_cedula, curso_id):
    try:
        ejecutar_modificacion(f"INSERT INTO MATRICULAS (ESTUDIANTE_CEDULA, CURSO_ID) VALUES ('{estudiante_cedula}','{curso_id}')")
    except mysql.connector.Error as r:
        print("Error al asignar: ",r)




def menu():
   while True:
    print("Bienvenido al Sistema de gestion de estudiantes\n")
    print("Porfavor seleccione una opcion\n")
    print("1-Insertar estudiante\n")
    print("2-Asignar materias a un estudiante\n")
    print("3-Comprobar promedios\n")
    print("4-Finalizar\n")
    opcion = input("Digite su numero de opcion: ")

    if opcion not in["1","2","3","4"]:
            print ("Opcion inexistente, intente de nuevo")
            time.sleep(0.75)
            continue
    
    elif opcion == "1":
        print ("Bienvenido al sistema de ingreso de estudiantes\n")
        while True:
            repetir = input("Desea ingresar un alumno?     S o N\n").lower()        
            if repetir in ["s", "n"]:
                print("Preparando...\n")
                if repetir == "s":
                    cedula = input("Ingrese la cedula del alumno\n")
                    nombre = input("Ingrese el nombre del alumno\n")
                    edad = input("Ingrese la edad del alumno\n")
                    nota1 = input("Ingrese la primera nota del alumno\n")
                    nota2 = input("Ingrese la segunda nota del alumno\n")
                    nota3 = input("Ingrese la tercera nota del alumno\n")
                    insertar_alumnos(cedula, nombre, edad, nota1, nota2, nota3)
                    print("Alumno guardado correctamente\n")
                elif repetir == "n":
                    print("Gracias por usar el sistema\n")
                    time.sleep(0.75)
                    limpiar()
                    break
                else:
                    continue

            else:
                print("Opcion inexistente, intente de nuevo")
                time.sleep(0.75)
                limpiar()
                continue

    elif opcion == "2":
         print ("Bienvenido al sistema de asignacion de materias\n")
         while True:
            repetir = input("Desea asignar una materia?     S o N\n").lower()        
            if repetir in ["s", "n"]:
                print("Preparando...\n")
                if repetir == "s":
                    estudiante_cedula = input("Ingrese la cedula del alumno\n")
                    curso_id = input("Ingrese la ID del curso a asignar\n")
                    asignar_materia(estudiante_cedula, curso_id)
                    print("Materia asignada correctamente\n")
                elif repetir == "n":
                    print("Gracias por usar el sistema\n")
                    time.sleep(0.75)
                    limpiar()
                    break
                else:
                    continue

            else:
                print("Opcion inexistente, intente de nuevo")
                time.sleep(0.75)
                limpiar()
                continue
       
        
    
    elif opcion == "3":
        print ("Bienvenido al sistema de promedios\n")
        calcular_promedio()
        input("Presione ENTER para regresar")
 

    
    elif opcion == "4":
       print ("Gracias por usar el sistema\n")
       time.sleep(0.75)
       break

    else:
       print ("Opcion inexistente, intente de nuevo")
       time.sleep(0.75)
       continue
    