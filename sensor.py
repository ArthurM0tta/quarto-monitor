from gpiozero import MotionSensor
from database import (
    criar_banco,
    registrar_movimento,
    obter_status_monitoramento
)
from monitoramento import monitorar_ativacao
from notifications import enviar_notificacao

import threading
from datetime import datetime


sensor = MotionSensor(17)

criar_banco()

thread_ativacao = threading.Thread(
    target=monitorar_ativacao,
    daemon=True
)

thread_ativacao.start()

print("Monitor do quarto iniciado.")
print("Aguardando movimento...")


while True:
    sensor.wait_for_motion()

    status = obter_status_monitoramento()

    print(f"Movimento detectado! Monitoramento: {status}")

    if status == "ATIVO":

        registrar_movimento()

        horario = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        mensagem = (
            "🚨 MOVIMENTO DETECTADO!\n\n"
            "🏠 Monitor do Quarto\n"
            f"🕐 {horario}"
        )

        enviar_notificacao(mensagem)

        print("Movimento registrado no banco.")
        print("Notificação enviada.")

    sensor.wait_for_no_motion()
