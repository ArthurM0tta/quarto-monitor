# Monitor do Quarto

Sistema de monitoramento de movimento desenvolvido com Raspberry Pi e sensor PIR.

## Sobre o projeto

O Monitor do Quarto é um sistema IoT desenvolvido em Python para detectar movimentos através de um sensor PIR conectado a um Raspberry Pi.

Quando o monitoramento está ativo e um movimento é detectado, o sistema registra o evento em um banco de dados SQLite e envia uma notificação para o Telegram.

## Funcionalidades

- Detecção de movimento com sensor PIR
- Ativação do monitoramento com período de espera de 5 minutos
- Cancelamento da ativação
- Desativação imediata
- Registro de movimentos em banco SQLite
- Dashboard web
- Contagem de movimentos do dia
- Visualização do último movimento
- Histórico dos últimos eventos
- Notificações pelo Telegram
- Inicialização automática dos serviços no Raspberry Pi

## Tecnologias

- Python
- Flask
- SQLite
- gpiozero
- Requests
- python-dotenv
- Telegram Bot API
- HTML
- CSS
- JavaScript
- Raspberry Pi

## Hardware

- Raspberry Pi 4B
- Sensor de movimento HC-SR501

## Estrutura do projeto

```text
quarto-monitor/
├── app.py
├── sensor.py
├── database.py
├── monitoramento.py
├── notifications.py
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
│   └── index.html
└── database/
```
## Status do projeto

Em desenvolvimento.

O sistema atualmente possui detecção de movimento, dashboard web, armazenamento dos eventos e notificações pelo Telegram.
