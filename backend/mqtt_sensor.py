import paho.mqtt.client as mqtt
import database

BROKER = "broker.hivemq.com"  # Substitua pelo IP/Host do seu broker MQTT se for local
PORTA = 1883
TOPICO = "projeto/ultrassonico/distancia"

def ao_conectar(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conectado ao MQTT Broker! Inscrevendo no tópico: {TOPICO}")
        client.subscribe(TOPICO)
    else:
        print(f"Falha na conexão MQTT. Código de erro: {rc}")

def ao_receber_mensagem(client, userdata, msg):
    try:
        conteudo = msg.payload.decode("utf-8")
        distancia = float(conteudo)
        print(f"[MQTT] Nova distância recebida: {distancia} cm")
        
        # Salva a leitura no banco de dados SQLite
        database.salvar_medicao(distancia)
    except ValueError:
        print(f"[MQTT Erro] Mensagem inválida recebida: {msg.payload}")

def iniciar_mqtt():
    client = mqtt.Client()
    client.on_connect = ao_conectar
    client.on_message = ao_receber_mensagem
    
    print("Iniciando conexão MQTT...")
    client.connect(BROKER, PORTA, 60)
    client.loop_start()  # Roda a escuta em background

if __name__ == "__main__":
    database.criar_tabela()
    iniciar_mqtt()
    # Mantém o script rodando no terminal
    import time
    while True:
        time.sleep(1)