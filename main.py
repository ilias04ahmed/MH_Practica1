import time

from generaInstancias import generar_instancia
from inicial import construir_mapa_estudiantes, solucion_inicial
from funcionObjetivo import evaluar_detallado
from busquedaLocal import busqueda_primer_mejor, busqueda_mejor
from graficas import grafica_convergencia, graficas_comparativas, histograma_alumnos


def imprimir_detalle(nombre, sol, exams, rooms, mapa_estudiantes, n_slots, tiempo, evaluaciones, evolucion):
    total, p1, p2, p3, v = evaluar_detallado(sol, exams, rooms, mapa_estudiantes, n_slots)

    print("------", nombre, "------")
    print("Coste total:", round(total, 2))
    print(" Penalizacion consecutivos:", p1)
    print(" Penalizacion mismo dia:", p2)
    print(" Penalizacion distribucion:", round(p3, 2))
    print(" Violaciones:", v)
    print(" Tiempo:", round(tiempo, 4), "segundos")
    print(" Evaluaciones:", evaluaciones)
    print(" Iteraciones (mejoras):", len(evolucion) - 1)
    print()


def ejecutar_experimentos():
    # Listas para el resumen final
    nombres_instancias = []
    costes_pm = []
    costes_mm = []
    tiempos_pm = []
    tiempos_mm = []

    exams_media = None

    # Datos de las 3 pruebas
    casos_exams = [50, 100, 200]
    casos_students = [1000, 2000, 4000]
    casos_rooms = [5, 10, 20]
    casos_slots = [25, 40, 100]
    nombres = ["Pequeña (50 ex)", "Media (100 ex)", "Grande (200 ex)"]

    for i in range(3):
        print("\n========================================================")
        print(" EJECUTANDO INSTANCIA:", nombres[i])
        print("========================================================")

        # Instancia
        student_exam, exams, rooms, n_slots = generar_instancia(
            n_exams=casos_exams[i], 
            n_students=casos_students[i], 
            n_rooms=casos_rooms[i], 
            n_slots=casos_slots[i], 
            seed=42
        )
        mapa_estudiantes = construir_mapa_estudiantes(student_exam)

        print("Examenes:", len(exams))
        print("Estudiantes:", len(mapa_estudiantes))
        print("Aulas:", len(rooms))
        print("Slots:", n_slots)
        print()

        # Solucion inicial
        inicio = time.time()
        sol_ini = solucion_inicial(exams, rooms, n_slots)
        t_ini = time.time() - inicio

        total_ini, p1_ini, p2_ini, p3_ini, v_ini = evaluar_detallado(sol_ini, exams, rooms, mapa_estudiantes, n_slots)

        print("------ SOLUCION INICIAL ------")
        print("Coste total:", round(total_ini, 2))
        print(" Violaciones:", v_ini)
        print(" Tiempo:", round(t_ini, 4), "segundos")
        print()

        # Primer Mejor
        inicio = time.time()
        sol_pm, coste_pm, eval_pm, evo_pm = busqueda_primer_mejor(
            sol_ini, exams, rooms, mapa_estudiantes, n_slots
        )
        t_pm = time.time() - inicio

        imprimir_detalle(
            "BUSQUEDA PRIMER MEJOR",
            sol_pm, exams, rooms, mapa_estudiantes, n_slots,
            t_pm, eval_pm, evo_pm
        )

        # Mejor Vecino
        inicio = time.time()
        sol_mm, coste_mm, eval_mm, evo_mm = busqueda_mejor(
            sol_ini, exams, rooms, mapa_estudiantes, n_slots
        )
        t_mm = time.time() - inicio

        imprimir_detalle(
            "BUSQUEDA MEJOR VECINO",
            sol_mm, exams, rooms, mapa_estudiantes, n_slots,
            t_mm, eval_mm, evo_mm
        )

        print(f"Generando grafica de convergencia para {nombres[i]}...")
        grafica_convergencia(evo_pm, evo_mm, nombres[i])

        # Guardar datos
        nombres_instancias.append(nombres[i])
        costes_pm.append(coste_pm)
        costes_mm.append(coste_mm)
        tiempos_pm.append(t_pm)
        tiempos_mm.append(t_mm)

        if i == 1:
            exams_media = exams


    print("\n\n-------------------------------------------------------------------------------------------------")
    print(" TABLA RESUMEN")
    print("-------------------------------------------------------------------------------------------------")
    
    print("Instancia\t\tCoste PM\tCoste MV\tTiempo PM\tTiempo MV")
    print("-----------------------------------------------------------------------------------------")
    
    for i in range(3):
        nombre_str = nombres_instancias[i]
        
        # Alinear columnas
        if len(nombre_str) < 16:
            nombre_str += "\t"
            
        c_pm = round(costes_pm[i], 2)
        c_mm = round(costes_mm[i], 2)
        t_pm = round(tiempos_pm[i], 2)
        t_mm = round(tiempos_mm[i], 2)
        
        print(nombre_str + "\t" + str(c_pm) + "\t" + str(c_mm) + "\t" + str(t_pm) + " s\t" + str(t_mm) + " s")
        
    print("-------------------------------------------------------------------------------------------------\n")

    # Generar graficas finales
    graficas_comparativas(nombres_instancias, costes_pm, costes_mm, tiempos_pm, tiempos_mm)
    histograma_alumnos(exams_media, "Instancia Media")
    
    print("Ejecucion terminada. Graficas guardadas.")


if __name__ == "__main__":
    ejecutar_experimentos()