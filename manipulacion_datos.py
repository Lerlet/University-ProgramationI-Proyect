import base_datos

def ejecutar_consulta(query):
    conexion = base_datos.conectarBD()
    cursor = conexion.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def obtener_cursos():
    return ejecutar_consulta("SELECT * FROM CURSOS")

def obtener_alumnos():
    return ejecutar_consulta("SELECT * FROM ESTUDIANTES")

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
        print(f"PROMEDIO: {round(promedio,1)}")