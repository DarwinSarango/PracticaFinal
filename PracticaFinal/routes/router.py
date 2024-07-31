from flask import Blueprint, jsonify, abort , request, render_template, redirect, Flask, flash, url_for
from controls.restaurante.restauranteControl import RestauranteControl
from controls.tda.graph.graphNoManagedLabel import GraphNoManagedLabel
from controls.restaurante.restauranteGrafo import RestauranteGrafo
from controls.tda.linked.linkedList import Linked_List
import time


router = Blueprint('router', __name__)


#GET: PARA PRESENTAR DATOS
#POST: GUARDA DATOS, MODIFICA DATOS Y EL INICIO DE SESION, EVIAR DATOS AL SERVIDOR

@router.route('/') #SON GETS
def home():
    return redirect("/restaurantes", code=302)

@router.route('/grafo')
def grafo():
    return render_template("d3/grafo.html")


#LISTA PERSONAS
@router.route('/restaurantes')
def lista_negocios():
    nc = RestauranteControl()
    return render_template('restaurante/lista.html', lista=nc.to_dic())


@router.route('/restaurantes/agregar')
def ver_guardar_negocios():
    return render_template('restaurante/guardar.html')


@router.route('/restaurantes/guardar', methods=["POST"])
def guardar_negocios():
    nc = RestauranteControl()
    data = request.form
    
    nc._restaurante._nombre = data["nombre"]
    nc._restaurante._direccion = data["direccion"]
    nc._restaurante._horario = data["horario"]
    nc._restaurante._lng = data["lng"]
    nc._restaurante._lat = data["lat"]
    nc.save
        
    return redirect("/restaurantes", code=302)

@router.route('/restaurantes/grafo_negocio')
def grafo_negocio():
    ng = RestauranteGrafo()
    ng.create_graph()
    return render_template("d3/grafo.html")

@router.route('/grafo_negocio/ver')
def ver_grafo_negocio():
    return render_template("d3/grafo.html")

@router.route('/restaurantes/grafo_ver_admin')
def grafo_ver_admin():
    nc = RestauranteControl()
    grafo = RestauranteGrafo()._grafo
    arrayNegocios = nc.to_dic()
    matriz_adyencia = [
        [
            grafo.weight_edges_E(arrayNegocios[i]["nombre"], arrayNegocios[j]["nombre"])
            if grafo.exist_edge_E(arrayNegocios[i]["nombre"], arrayNegocios[j]["nombre"]) else "--"
            for j in range(len(arrayNegocios))
        ]
        for i in range(len(arrayNegocios))
    ]
    return render_template("restaurante/grafo.html", lista=arrayNegocios, matrizAux=matriz_adyencia)

@router.route('/restaurantes/adyacencia', methods=["POST"])
def crear_ady():
    ndc = RestauranteControl()
    grafo = RestauranteGrafo()._grafo
    data = request.form
    origen, destino = data["origen"], data["destino"]

    if origen == destino or grafo.exist_edges(int(origen)-1, int(destino)-1):
        flash('Seleccione un origen y destino diferente' if origen == destino else 'Ya existe una adyacencia entre estos restaurantes', 'error')
    else:
        OrigenN = ndc._list().binary_search_models_int(int(origen), "_id")
        DestinoN = ndc._list().binary_search_models_int(int(destino), "_id")
        
        # Verificar tipos de OrigenN y DestinoN
        print(f"OrigenN type: {type(OrigenN)}, DestinoN type: {type(DestinoN)}")
        
        RestauranteGrafo().create_graph(OrigenN, DestinoN)
    
    return redirect("/restaurantes/grafo_ver_admin", code=302)


#Editar restaurantes
@router.route('/restaurantes/editar/<pos>')
def ver_editar(pos):
    nc = RestauranteControl()
    grafo = nc._list().getNode(int(pos)-1)
    print(grafo)
    return render_template("restaurante/editar.html", data = grafo )



@router.route('/restaurantes/modificar', methods=["POST"])
def modificar_negocios():
    nc = RestauranteControl()
    data = request.form
    pos = data["id"]
    print(pos)
    negocio = nc._list().getNode(int(pos)-1)
    
    if not "nombre" in data.keys():
        abort(400)
        
    #TODO ...Validar
    nc._negocio = negocio
    nc._negocio._nombre = data["nombre"]
    nc._negocio._direccion = data["direccion"]
    nc._negocio._horario = data["horario"]
    nc._negocio._lng = data["lng"]
    nc._negocio._lat = data["lat"]
    nc.merge(int(pos)-1)
    return redirect("/restaurantes", code=302)


#Eliminar
@router.route('/restaurantes/eliminar/<pos>')
def eliminar_grafo(pos):
    nc = RestauranteControl()
    nc.delete(int(pos)-1)
    return redirect("restaurantes", code=302)

@router.route('/restaurantes/eliminar')
def eliminar():
    nc = RestauranteControl()
    nc.delete()
    return redirect("/restaurantes", code=302)

#Buscar el camino mas corto

@router.route('/restaurantes/camino_minimo', methods=["POST"])
def camino_minimo():
    data = request.form
    origen, destino, metodo = data["origen"], data["destino"], data["metodo"]

    gf = RestauranteGrafo()
    
    # Verificar si el grafo está conectado
    if not gf._grafo.siEstaConectado():
        flash('El grafo no está conectado. No se puede calcular el camino más corto.', 'error')
        return redirect("restaurantes/grafo_ver_admin", code=302)

    if metodo == "dijkstra":
        startD = time.time()
        path, distance, elapsed_time = gf._grafo.shortest_path_dijkstra(origen, destino)
        elapsed_time = time.time() - startD
        print(f"Tiempo Ejecución Dijstrak: {elapsed_time}")
    else:
        startF = time.time()
        path, distance, elapsed_time = gf._grafo.shortest_path_floyd(origen, destino)
        elapsed_time = time.time() - startF
        print(f"Tiempo Ejecución Floyd: {elapsed_time}")
    return render_template('restaurante/camino_minimo.html', path=path, distance=distance, metodo=metodo, elapsed_time=elapsed_time)


