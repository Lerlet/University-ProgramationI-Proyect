import mysql.connector

def conectarBD():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ACADEMICO",
        port=3306
    )

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
        conexion = conectarBD()
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
    def mostrar_todos():
        conexion = conectarBD()
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
    
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
    
    def eliminar_alumno(self, alumno):
        self.alumnos.remove(alumno)
    
    def obtener_alumnos(self):
        return self.alumnos
    
    def obtener_profesor(self):
        return self.profesor
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_cantidad_alumnos(self):
        return len(self.alumnos)