from models.maquina_model import (
    get_maquinas,
    create_maquina,
    delete_maquina,
    get_maquinas_por_tipo,
    create_maquina_tipo,
    delete_maquina_por_id
)

def listar_maquinas_preventiva():
    return get_maquinas_por_tipo("Preventiva")

def adicionar_maquina_preventiva(nome):
    create_maquina_tipo(nome, "Preventiva")

def remover_maquina_preventiva(id):
    delete_maquina_por_id(id)

def listar_maquinas_corretiva():
    return get_maquinas_por_tipo("Corretiva")

def adicionar_maquina_corretiva(nome):
    create_maquina_tipo(nome, "Corretiva")

def remover_maquina_corretiva(id):
    delete_maquina_por_id(id)
