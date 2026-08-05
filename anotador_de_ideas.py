import random
ids = []
titulos = []
descripciones = []
categorias = []
prioridades = []
estados = []
fechas = []
observaciones = []
#--------------------------------------#
#--|menu_principal_anotador_de_ideas|--#
#--------------------------------------#
while True:
    print("menu principal anotador de ideas")
    print("1) crear idea")
    print("2) editar idea")
    print("3) eliminar idea")
    print("4) buscar idea")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #----------------#
    #--|crear_idea|--#
    #----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_idea = 1
        else:
            id_idea = ids[-1] + 1
        titulo = input("título: ")
        descripcion = input("descripción: ")
        categoria = input("categoría: ")
        prioridad = input("prioridad (alta, media o baja): ")
        estado = input("estado (pendiente, en desarrollo o completada): ")
        fecha = input("fecha: ")
        observacion = input("observación: ")
        ids.append(id_idea)
        titulos.append(titulo)
        descripciones.append(descripcion)
        categorias.append(categoria)
        prioridades.append(prioridad)
        estados.append(estado)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("idea registrada correctamente.")
        print("id:", id_idea)
    #-----------------#
    #--|editar_idea|--#
    #-----------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen ideas registradas.")
        else:
            print("editar idea")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {prioridades[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id de la idea: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {descripciones[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                descripciones[posicion] = input("nueva descripción: ")
                categorias[posicion] = input("nueva categoría: ")
                prioridades[posicion] = input("nueva prioridad: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                observaciones[posicion] = input("nueva observación: ")
                print("idea actualizada correctamente.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|eliminar_idea|--#
    #-------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen ideas registradas.")
        else:
            print("eliminar idea")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {prioridades[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id de la idea: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos de la idea")
                print(f"{ids[posicion]} | {titulos[posicion]} | {descripciones[posicion]}")
                respuesta = input("¿desea eliminar esta idea? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    descripciones.pop(posicion)
                    categorias.pop(posicion)
                    prioridades.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    observaciones.pop(posicion)
                    print("idea eliminada correctamente.")
                else:
                    print("la idea no fue eliminada.")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|buscar_idea|--#
    #-----------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen ideas registradas.")
        else:
            print("buscar idea")
            id_buscar = int(input("ingrese la id de la idea: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("título:", titulos[posicion])
                print("descripción:", descripciones[posicion])
                print("categoría:", categorias[posicion])
                print("prioridad:", prioridades[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen ideas registradas.")
        else:
            pendientes = 0
            desarrollo = 0
            completadas = 0
            prioridad_alta = 0
            prioridad_media = 0
            prioridad_baja = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {prioridades[i]} | {estados[i]}")
                if estados[i].lower() == "pendiente":
                    pendientes += 1
                elif estados[i].lower() == "en desarrollo":
                    desarrollo += 1
                elif estados[i].lower() == "completada":
                    completadas += 1
                if prioridades[i].lower() == "alta":
                    prioridad_alta += 1
                elif prioridades[i].lower() == "media":
                    prioridad_media += 1
                elif prioridades[i].lower() == "baja":
                    prioridad_baja += 1
            print("estadísticas anotador de ideas")
            print("cantidad de ideas:", len(ids))
            print("ideas pendientes:", pendientes)
            print("ideas en desarrollo:", desarrollo)
            print("ideas completadas:", completadas)
            print("prioridad alta:", prioridad_alta)
            print("prioridad media:", prioridad_media)
            print("prioridad baja:", prioridad_baja)
            posicion = random.randint(0, len(ids) - 1)
            print("idea seleccionada")
            print("id:", ids[posicion])
            print("título:", titulos[posicion])
            print("descripción:", descripciones[posicion])
            print("categoría:", categorias[posicion])
            print("prioridad:", prioridades[posicion])
            print("estado:", estados[posicion])
            print("fecha:", fechas[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el anotador de ideas.")
        break
    else:
        print("opción no válida.")