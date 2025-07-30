from models.maquina_model import (
    get_maquinas,
    create_maquina,
    delete_maquina,
    get_maquinas_por_tipo,
    create_maquina_tipo,
    delete_maquina_por_id,
    get_maquinas_preditiva,
    create_maquina_preditiva,
    update_status_maquina
)

# Funções gerais

def obter_maquinas():
    return get_maquinas()

def adicionar_maquina(nome, tipo_manutencao, funcionando):
    create_maquina(nome, tipo_manutencao, funcionando)

def remover_maquina(maquina_id):
    delete_maquina(maquina_id)


# Manutenção Preventiva

def listar_maquinas_preventiva():
    return get_maquinas_por_tipo("Preventiva")

def adicionar_maquina_preventiva(nome):
    create_maquina_tipo(nome, "Preventiva")

def remover_maquina_preventiva(id_maquina):
    delete_maquina_por_id(id_maquina)


# Manutenção Corretiva

def listar_maquinas_corretiva():
    return get_maquinas_por_tipo("Corretiva")

def adicionar_maquina_corretiva(nome):
    create_maquina_tipo(nome, "Corretiva")

def remover_maquina_corretiva(id_maquina):
    delete_maquina_por_id(id_maquina)


# Manutenção Preditiva

def listar_maquinas_preditiva():
    return get_maquinas_preditiva()

def adicionar_maquina_preditiva(nome, status):
    create_maquina_preditiva(nome, status)

def remover_maquina_preditiva(id_maquina):
    delete_maquina_por_id(id_maquina)

def atualizar_status_preditiva(id_maquina, status):
    update_status_maquina(id_maquina, status)
