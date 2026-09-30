import time
from datetime import datetime, timedelta

from database import definir_status, obter_status


TEMPO_ATIVACAO = 5 * 60


def ativar_monitoramento():
    status, ativacao_em = obter_status()

    if status == "ATIVO":
        print("Monitoramento já está ativo.")
        return

    if status == "PENDENTE":
        print(f"Ativação já está pendente para {ativacao_em}.")
        return

    ativacao = datetime.now() + timedelta(seconds=TEMPO_ATIVACAO)

    definir_status(
        "PENDENTE",
        ativacao.strftime("%Y-%m-%d %H:%M:%S")
    )

    print("Monitoramento programado para ativar em 5 minutos.")


def verificar_ativacao():
    status, ativacao_em = obter_status()

    if status != "PENDENTE" or not ativacao_em:
        return

    horario_ativacao = datetime.strptime(
        ativacao_em,
        "%Y-%m-%d %H:%M:%S"
    )

    if datetime.now() >= horario_ativacao:
        definir_status("ATIVO", None)
        print("Monitoramento ATIVO.")


def desativar_monitoramento():
    definir_status("DESATIVADO", None)
    print("Monitoramento DESATIVADO.")


def monitorar_ativacao():
    while True:
        verificar_ativacao()
        time.sleep(1)
