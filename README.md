# DOCUMENTAÇÃO DO PROJETO
# Monitoramento de Segurança Industrial — IoT

## 1. Introdução

O projeto Monitoramento de Segurança Industrial — IoT tem como finalidade desenvolver um sistema capaz de realizar medições de distância utilizando um sensor ultrassônico, identificar diferentes níveis de proximidade e transmitir essas informações para um painel de monitoramento.

A proposta consiste na integração entre componentes eletrônicos, programação e comunicação de dados. O sistema utiliza um Arduino para realizar as leituras do sensor, um Raspberry Pi para receber e transmitir os dados por meio do protocolo MQTT, uma API desenvolvida com FastAPI para receber e armazenar as medições em um banco de dados SQLite e uma interface web para apresentar as informações.

Dessa forma, o projeto demonstra a aplicação de conceitos de Internet das Coisas (IoT), comunicação entre dispositivos, desenvolvimento Back-end, desenvolvimento Front-end e armazenamento de dados.

## 2. Objetivo geral

Desenvolver um sistema de monitoramento capaz de identificar a distância de objetos por meio de um sensor ultrassônico, emitir alertas visuais e sonoros conforme a proximidade identificada e disponibilizar as medições em uma interface web.

## 3. Objetivos específicos

- Desenvolver um circuito eletrônico utilizando Arduino.
- Realizar medições de distância com um sensor ultrassônico.
- Configurar LEDs e buzzer para representar diferentes níveis de proximidade.
- Utilizar o Raspberry Pi para receber os dados enviados pelo Arduino.
- Implementar a comunicação MQTT para transmitir as informações.
- Desenvolver uma API utilizando Python e FastAPI.
- Armazenar as medições em um banco de dados SQLite.
- Desenvolver uma interface web para apresentar os dados.
- Integrar Hardware e Software em um único sistema.

## 4. Desenvolvimento do projeto

O desenvolvimento começou pela leitura da documentação da atividade, buscando identificar os requisitos solicitados e compreender o funcionamento esperado do sistema.

Logo após, a equipe reuniu suas ideias e realizou pesquisas sobre possíveis projetos, analisando alternativas que pudessem ser desenvolvidas com os conhecimentos adquiridos durante as aulas.

Depois da escolha da proposta, foi realizada a montagem e a simulação do circuito no Tinkercad. Com base nas aulas sobre Arduino, nos estudos realizados e nos testes, foi possível construir o circuito e verificar seu funcionamento.

Com a parte eletrônica desenvolvida, o projeto avançou para a integração com o Raspberry Pi e a programação em Python. Posteriormente, foram implementadas a comunicação MQTT, a API, o banco de dados e a interface web.

Por fim, as partes foram organizadas para permitir que as medições realizadas pelo sensor fossem transmitidas, armazenadas e apresentadas em um painel de monitoramento.

## 5. Componentes utilizados

| Componente | Função |
|---|---|
| Arduino Uno | Realiza o processamento das leituras e controla os componentes eletrônicos. |
| Sensor ultrassônico HC-SR04 | Mede a distância entre o sensor e um objeto. |
| LED vermelho | Indica proximidade crítica. |
| LED azul | Indica proximidade elevada. |
| LED amarelo | Indica nível intermediário de proximidade. |
| LED verde | Indica distância dentro da faixa programada. |
| Buzzer | Emite um alerta sonoro nas situações de maior proximidade. |
| Raspberry Pi | Recebe os dados do Arduino e realiza a comunicação MQTT. |
| Computador | Executa a API e disponibiliza a interface de monitoramento. |

## 6. Tecnologias utilizadas

### Hardware e eletrônica
- Arduino Uno.
- Sensor ultrassônico HC-SR04.
- LEDs.
- Buzzer.
- Raspberry Pi.
- Tinkercad para simulação do circuito.

### Programação e desenvolvimento
- C/C++ para programação do Arduino.
- Python para desenvolvimento do Backend e comunicação com o Hardware.
- HTML para estruturação da interface.
- CSS para estilização da interface.
- JavaScript para comunicação entre a interface e a API.

### Comunicação e armazenamento
- MQTT para transmissão das informações.
- HiveMQ como broker MQTT.
- FastAPI para disponibilização da API REST.
- SQLite para armazenamento das medições.
- PySerial para comunicação serial entre o Raspberry Pi e o Arduino.
- Paho-MQTT para comunicação MQTT utilizando Python.
- uv para gerenciamento do ambiente e das dependências Python.

### Ferramentas
- Visual Studio Code.
- Git e GitHub.
- Arduino CLI.
- PowerShell e terminal Linux.
- Swagger/OpenAPI para documentação e testes da API.

## 7. Arquitetura do sistema

O projeto foi dividido em quatro partes principais: Hardware, comunicação, Backend e Frontend.

### 7.1. Fluxo de funcionamento

O funcionamento acontece da seguinte maneira:

1. O sensor ultrassônico realiza a medição da distância.
2. O Arduino interpreta o resultado e controla os LEDs e o buzzer.
3. O Arduino envia a leitura pela comunicação serial.
4. O Raspberry Pi recebe a informação utilizando Python e PySerial.
5. O Raspberry Pi publica a medição no broker MQTT HiveMQ.
6. O Backend recebe a mensagem MQTT.
7. A API utiliza o SQLite para armazenar as informações.
8. O Frontend consulta a API e apresenta a medição atual e o histórico.

### 7.2. Representação da arquitetura

```text
SENSOR ULTRASSÔNICO
        |
        v
     ARDUINO
        |
        | Comunicação Serial
        v
  RASPBERRY PI
        |
        | Python + PySerial
        |
        | MQTT
        v
    HIVEMQ
        |
        | MQTT
        v
     BACKEND
        |
        | FastAPI
        |
        v
   BANCO SQLITE
        |
        | API REST
        v
     FRONTEND
        |
        v
 PAINEL DE MONITORAMENTO
```

## 8. Funcionamento do Hardware

O Hardware é responsável por realizar as medições e identificar a proximidade de objetos.

O sensor HC-SR04 envia ondas ultrassônicas e recebe o sinal refletido por um objeto. Com base no tempo de retorno desse sinal, o Arduino calcula a distância aproximada em centímetros.

O resultado é utilizado para determinar qual LED será acionado e se o buzzer deverá emitir um alerta.

### 8.1. Ligações utilizadas

| Componente | Pino do Arduino |
|---|---|
| TRIG do sensor | 3 |
| ECHO do sensor | 4 |
| LED vermelho | 8 |
| LED azul | 9 |
| LED amarelo | 10 |
| LED verde | 11 |
| Buzzer | 12 |

### 8.2. Faixas de distância

| Distância identificada | LED | Buzzer |
|---|---|---|
| Até 4 cm | Vermelho | Ligado durante o alerta |
| Acima de 4 até 12 cm | Azul | Ligado durante o alerta |
| Acima de 12 até 22 cm | Amarelo | Desligado |
| Acima de 22 até 32 cm | Verde | Desligado |
| Acima de 32 cm | Todos desligados | Desligado |
| Sem retorno do sensor | Todos desligados | Desligado |

### 8.3. Código do Arduino

Arquivo: `trabalho-iot.ino`

```cpp
int trigPin = 3;
int echoPin = 4;

int ledPin1 = 8;  // Vermelho
int ledPin2 = 9;  // Azul
int ledPin3 = 10; // Amarelo
int ledPin4 = 11; // Verde

int buzzerPin = 12;

long sure;
long mesafe;

// Função para piscar somente um LED
void piscarLED(int pino, int tempo)
{
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
  digitalWrite(ledPin4, LOW);

  digitalWrite(pino, HIGH);
  delay(tempo);
  digitalWrite(pino, LOW);
  digitalWrite(buzzerPin, LOW);
}

void setup()
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);

  pinMode(buzzerPin, OUTPUT);

  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
  digitalWrite(ledPin4, LOW);
  digitalWrite(buzzerPin, LOW);

  Serial.begin(9600);
}

void loop()
{
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
  digitalWrite(ledPin4, LOW);
  digitalWrite(buzzerPin, LOW);

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  sure = pulseIn(echoPin, HIGH, 30000);

  if (sure == 0)
  {
    mesafe = 999;
  }
  else
  {
    mesafe = sure * 0.0343 / 2;
  }

  Serial.print("Distancia: ");
  Serial.println(mesafe);

  if (mesafe <= 4)
  {
    digitalWrite(buzzerPin, HIGH);
    piscarLED(ledPin1, 25);
  }
  else if (mesafe <= 12)
  {
    digitalWrite(buzzerPin, HIGH);
    piscarLED(ledPin2, 60);
  }
  else if (mesafe <= 22)
  {
    digitalWrite(buzzerPin, LOW);
    piscarLED(ledPin3, 120);
  }
  else if (mesafe <= 32)
  {
    piscarLED(ledPin4, 200);
    digitalWrite(buzzerPin, LOW);
  }
  else
  {
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, LOW);
    digitalWrite(ledPin4, LOW);
    digitalWrite(buzzerPin, LOW);
  }

  delay(100);
}
```

## 9. Comunicação entre Arduino e Raspberry Pi

Após a leitura da distância, o Arduino transmite os valores pela porta serial utilizando a velocidade de comunicação de 9600 baud.

O Raspberry Pi recebe essas informações por meio da biblioteca PySerial, que permite a comunicação entre Python e dispositivos conectados às portas seriais.

O arquivo responsável por essa etapa é `dht11_mqtt.py`.

### 9.1. Código Python do Raspberry Pi

Arquivo: `dht11_mqtt.py`

```python
import time
import serial
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "projeto/ultrassonico/distancia"

SERIAL_PORT = "/dev/ttyACM0"
SERIAL_BAUDRATE = 9600

# Compatível com paho-mqtt v2.x
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(MQTT_BROKER, MQTT_PORT, 60)

ser = None

try:
    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1)
    time.sleep(2)
    print("Conectado à Serial! Enviando dados para o MQTT HiveMQ...")

    while True:
        if ser.in_waiting > 0:
            linha = ser.readline().decode('utf-8', errors='ignore').strip()
            if linha:
                print(f"[Raspberry -> MQTT]: {linha}")
                client.publish(MQTT_TOPIC, linha)

except KeyboardInterrupt:
    print("\nExecução encerrada pelo usuário.")

except Exception as e:
    print(f"Erro na comunicação serial: {e}")

finally:
    if ser is not None and ser.is_open:
        ser.close()
    client.disconnect()
```

### 9.2. Configurações MQTT

| Configuração | Valor |
|---|---|
| Broker | broker.hivemq.com |
| Porta | 1883 |
| Tópico | projeto/ultrassonico/distancia |
| Protocolo | MQTT |
| Formato da mensagem | Texto contendo a distância |

O MQTT é um protocolo de comunicação leve, utilizado para transmitir mensagens entre dispositivos por meio de um broker.

Nesse projeto, o HiveMQ recebe as mensagens publicadas pelo Raspberry Pi e permite que o Backend se inscreva no mesmo tópico para receber as medições.

## 10. Desenvolvimento do Backend

O Backend é responsável por receber as informações transmitidas pelo MQTT, processar os valores recebidos, armazenar as medições e disponibilizar os dados por meio de uma API REST.

O desenvolvimento foi realizado utilizando Python e FastAPI.

### 10.1. Estrutura do Backend

```text
backend/
    main.py
    mqtt_sensor.py
    database.py
    banco.db
    pyproject.toml
    uv.lock
    .venv/
```

### 10.2. Comunicação MQTT

Arquivo: `mqtt_sensor.py`

Esse arquivo estabelece a conexão com o HiveMQ, realiza a inscrição no tópico utilizado pelo projeto e recebe as mensagens enviadas pelo Raspberry Pi.

```python
import paho.mqtt.client as mqtt
import database

BROKER = "broker.hivemq.com"
PORTA = 1883
TOPICO = "projeto/ultrassonico/distancia"

def ao_conectar(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conectado ao HiveMQ! Escutando: {TOPICO}")
        client.subscribe(TOPICO)

def ao_receber_mensagem(client, userdata, msg):
    try:
        conteudo = msg.payload.decode("utf-8")
        print(f"[API recebeu via MQTT]: {conteudo}")

        # Extrai apenas o número da leitura
        import re
        numeros = re.findall(r"[-+]?\d*\.\d+|\d+", conteudo)

        if numeros:
            valor = float(numeros[0])
            database.salvar_medicao(valor)

    except Exception as e:
        print(f"Erro ao salvar mensagem: {e}")

def iniciar_mqtt():
    client = mqtt.Client()
    client.on_connect = ao_conectar
    client.on_message = ao_receber_mensagem
    client.connect(BROKER, PORTA, 60)
    client.loop_start()
```

### 10.3. Banco de dados SQLite

Arquivo: `database.py`

O SQLite é responsável por armazenar as medições recebidas pelo Backend.

A tabela `medicoes` possui três campos:

- `id`: identificador único de cada registro.
- `distancia`: valor da distância recebido pelo sistema.
- `data_hora`: data e horário em que a medição foi registrada.

Código:

```python
import sqlite3
from pathlib import Path
from datetime import datetime

# Caminho absoluto para criar/acessar o arquivo do banco de dados na pasta backend
CAMINHO_BANCO = Path(__file__).parent / "banco.db"

def conectar():
    """Cria e retorna uma conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    """Cria a tabela 'medicoes' se ela ainda não existir."""
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS medicoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            distancia REAL NOT NULL,
            data_hora TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def salvar_medicao(distancia: float):
    """Salva uma nova leitura de distância com a data e hora atuais."""
    conexao = conectar()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conexao.execute(
        "INSERT INTO medicoes (distancia, data_hora) VALUES (?, ?)",
        (distancia, data_hora)
    )

    conexao.commit()
    conexao.close()

def listar_medicoes(limite: int = 50):
    """Retorna as últimas medições salvas no banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, distancia, data_hora FROM medicoes ORDER BY id DESC LIMIT ?",
        (limite,)
    )

    linhas = cursor.fetchall()
    conexao.close()

    return [dict(linha) for linha in linhas]
```

### 10.4. API com FastAPI

Arquivo: `main.py`

A API disponibiliza as rotas necessárias para consultar e registrar medições.

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
import mqtt_sensor

database.criar_tabela()
mqtt_sensor.iniciar_mqtt()

app = FastAPI(title="API Medições IoT")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "API rodando com sucesso"}

@app.get("/api/medicoes")
def obter_historico(limite: int = 50):
    return database.listar_medicoes(limite)

@app.post("/api/medicoes")
def registrar_medicao(distancia: float):
    database.salvar_medicao(distancia)
    return {"status": "sucesso", "distancia": distancia}
```

### 10.5. Rotas disponíveis

| Método | Rota | Função |
|---|---|---|
| GET | `/` | Verifica se a API está funcionando. |
| GET | `/api/medicoes` | Consulta o histórico de medições. |
| POST | `/api/medicoes` | Registra uma nova medição. |

A documentação interativa da API é disponibilizada pelo FastAPI através do Swagger, no endereço:

`http://127.0.0.1:8000/docs`

## 11. Desenvolvimento do Frontend

O Frontend é a parte visual do projeto. Sua função é apresentar os dados recebidos pela API de maneira organizada e facilitar o acompanhamento das medições.

A interface foi desenvolvida utilizando HTML, CSS e JavaScript.

### 11.1. Estrutura do Frontend

```text
frontend/
    index.html
    style.css
    script.js
```

### 11.2. Estrutura HTML

Arquivo: `index.html`

O HTML organiza os elementos da página, incluindo o título, o card da última medição e a tabela de histórico.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel de Segurança Industrial - IoT</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Painel de Monitoramento Industrial</h1>
            <p>Leitura em tempo real e histórico de medições</p>
        </header>

        <section class="card-status">
            <h2>Última Medição</h2>
            <div id="valor-atual" class="medicao-destaque">--</div>
            <span id="data-atual" class="status-tempo">
                Aguardando dados da API...
            </span>
        </section>

        <section class="historico-container">
            <h2>Histórico do Banco de Dados</h2>

            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Medição / Distância</th>
                        <th>Data e Hora</th>
                    </tr>
                </thead>

                <tbody id="tabela-corpo">
                    <tr>
                        <td colspan="3">Carregando histórico...</td>
                    </tr>
                </tbody>
            </table>
        </section>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### 11.3. JavaScript e integração com a API

Arquivo: `script.js`

O JavaScript realiza as requisições para a API, recebe os dados em formato JSON, atualiza a última medição e preenche a tabela de histórico.

A consulta é executada automaticamente a cada dois segundos.

```javascript
// URL da API REST criada no FastAPI
const API_URL = "http://127.0.0.1:8000/api/medicoes";

async function buscarMedicoes() {
    try {
        const resposta = await fetch(API_URL);

        if (!resposta.ok) {
            throw new Error(`Erro na API: ${resposta.status}`);
        }

        const medicoes = await resposta.json();

        // Atualizar o card com a última medição
        if (medicoes.length > 0) {
            const ultima = medicoes[0];

            document.getElementById("valor-atual").innerText =
                `${ultima.distancia} cm`;

            document.getElementById("data-atual").innerText =
                `Registrado em: ${ultima.data_hora}`;
        } else {
            document.getElementById("valor-atual").innerText = "Sem dados";

            document.getElementById("data-atual").innerText =
                "Nenhuma leitura salva no banco ainda.";
        }

        // Preencher a tabela de histórico
        const tabelaCorpo = document.getElementById("tabela-corpo");
        tabelaCorpo.innerHTML = "";

        medicoes.forEach(m => {
            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td>${m.id}</td>
                <td><strong>${m.distancia} cm</strong></td>
                <td>${m.data_hora}</td>
            `;

            tabelaCorpo.appendChild(linha);
        });

    } catch (erro) {
        console.error("Falha ao buscar medições do SQLite:", erro);

        document.getElementById("data-atual").innerText =
            "Erro de conexão com o servidor Back-end!";
    }
}

buscarMedicoes();
setInterval(buscarMedicoes, 2000);
```

### 11.4. Estilização CSS

Arquivo: `style.css`

O CSS é responsável pela apresentação visual da interface, organizando os elementos, definindo cores, espaçamentos, tamanhos e a aparência dos cards e da tabela.

O arquivo é carregado pelo `index.html` por meio da seguinte referência:

```html
<link rel="stylesheet" href="style.css">
```

## 12. Estrutura geral dos arquivos

A organização principal do projeto no computador é:

```text
projeto-iot/
│
├── backend/
│   ├── main.py
│   ├── mqtt_sensor.py
│   ├── database.py
│   ├── banco.db
│   ├── pyproject.toml
│   ├── uv.lock
│   └── .venv/
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

No Raspberry Pi, a pasta utilizada para a comunicação com o Arduino contém:

```text
trabalho-iot/
│
├── dht11_mqtt.py
└── trabalho-iot.ino
```

O arquivo `.ino` contém o programa carregado no Arduino. O arquivo Python é responsável por receber as informações pela serial e publicá-las no MQTT.

## 13. Testes e validação

Os testes têm como objetivo verificar se cada parte do sistema realiza corretamente sua função e se a comunicação entre os componentes acontece conforme esperado.

### 13.1. Teste do Hardware

Foi verificado o funcionamento do sensor ultrassônico, dos LEDs e do buzzer, observando as mudanças de comportamento conforme a distância dos objetos.

### 13.2. Teste da comunicação serial

Foi verificada a identificação do Arduino pelo Raspberry Pi através da porta:

`/dev/ttyACM0`

A comunicação utiliza a velocidade de 9600 baud.

### 13.3. Teste MQTT

Foi utilizada a comunicação com o broker HiveMQ, configurando o mesmo tópico no programa publicador do Raspberry Pi e no programa receptor do Backend.

Tópico utilizado:

`projeto/ultrassonico/distancia`

### 13.4. Teste do Backend

A inicialização da API foi realizada pelo comando:

```powershell
uv run uvicorn main:app --reload
```

Foi possível verificar a inicialização do servidor e a conexão do receptor MQTT com o HiveMQ.

### 13.5. Teste do banco de dados

O banco SQLite foi configurado para armazenar o identificador, a distância e a data e hora de cada medição recebida.

### 13.6. Teste do Frontend

A interface foi configurada para consultar a rota `/api/medicoes`, apresentar a última medição e atualizar o histórico automaticamente.

## 14. Resultados esperados

Com todas as partes funcionando em conjunto, o sistema deve permitir:

- Identificar a distância de objetos utilizando o sensor ultrassônico.
- Acionar os LEDs conforme as faixas de proximidade.
- Emitir alertas sonoros nas situações programadas.
- Transmitir as leituras do Arduino para o Raspberry Pi.
- Publicar as informações no broker MQTT.
- Receber as mensagens no Backend.
- Armazenar as medições no banco de dados SQLite.
- Consultar as informações por meio da API.
- Visualizar a última medição e o histórico no painel web.

O projeto demonstra a integração entre Hardware e Software e a utilização de tecnologias de IoT para coleta, transmissão, armazenamento e visualização de dados.

## 15. Conclusão

O desenvolvimento do projeto permitiu aplicar, de forma prática, conhecimentos adquiridos durante as aulas de Desenvolvimento de Sistemas e atividades relacionadas à eletrônica e à Internet das Coisas.

Durante a construção, foram trabalhados conceitos de programação, montagem de circuitos, comunicação serial, protocolo MQTT, desenvolvimento de APIs, banco de dados e desenvolvimento de interfaces web.

A integração entre Arduino, Raspberry Pi e as tecnologias utilizadas possibilitou estruturar um sistema de monitoramento no qual as informações coletadas pelo sensor podem ser transmitidas, armazenadas e consultadas em uma interface.

Além do resultado técnico, o desenvolvimento também proporcionou experiência com pesquisa, planejamento, testes, identificação de erros e integração de diferentes tecnologias em um único projeto.

# 16. Tutorial de instalação e inicialização em outro computador

Este tutorial apresenta como preparar um computador novo para executar o projeto, mesmo que ele ainda não possua os arquivos do repositório.

## 16.1. Requisitos

Antes de iniciar, é necessário ter:

- Windows 10 ou 11.
- Git instalado.
- Python instalado.
- uv instalado.
- Visual Studio Code.
- Navegador de internet.
- Raspberry Pi configurado.
- Arduino conectado ao Raspberry Pi.
- Conexão com a internet.

## 16.2. Instalar as ferramentas

Instale o Git, Python e uv no computador.

Após as instalações, abra o PowerShell e confira:

```powershell
git --version
python --version
uv --version
```

Os comandos devem apresentar as versões instaladas.

## 16.3. Baixar o repositório

Escolha uma pasta para guardar o projeto e abra o PowerShell nela.

Execute:

```powershell
git clone URL_DO_REPOSITORIO
```

Substitua `URL_DO_REPOSITORIO` pelo endereço real do repositório no GitHub.

Entre na pasta:

```powershell
cd projeto-iot
```

Abra no Visual Studio Code:

```powershell
code .
```

## 16.4. Configurar o Backend

Acesse a pasta:

```powershell
cd backend
```

Instale as dependências registradas no projeto:

```powershell
uv sync
```

Esse comando prepara o ambiente virtual e instala as dependências definidas nos arquivos `pyproject.toml` e `uv.lock`.

## 16.5. Inicializar a API

No terminal, ainda dentro de `backend`, execute:

```powershell
uv run uvicorn main:app --reload
```

A API deverá ficar disponível em:

`http://127.0.0.1:8000`

Para acessar a documentação interativa:

`http://127.0.0.1:8000/docs`

Mantenha o terminal aberto.

## 16.6. Inicializar o Raspberry Pi

Em outro terminal, conecte-se ao Raspberry Pi:

```bash
ssh pi@rpi010.local
```

Entre na pasta:

```bash
cd ~/trabalho-iot
```

Verifique as bibliotecas:

```bash
python3 -c "import serial, paho.mqtt.client; print('Bibliotecas instaladas corretamente')"
```

Verifique se o Arduino está conectado:

```bash
ls /dev/ttyACM*
```

Com o Arduino conectado, execute:

```bash
python3 dht11_mqtt.py
```

O programa deverá receber as leituras seriais e publicá-las no HiveMQ.

Mantenha o terminal aberto.

## 16.7. Inicializar o Frontend

Abra a pasta `frontend` no Visual Studio Code.

Execute o arquivo `index.html` utilizando o Live Server ou outro servidor local.

A interface deverá acessar a API pelo endereço:

`http://127.0.0.1:8000/api/medicoes`

## 16.8. Ordem de inicialização

Para executar o sistema completo, siga esta ordem:

1. Conecte o Arduino ao Raspberry Pi.
2. Verifique a porta serial do Arduino.
3. Inicie o Backend no computador.
4. Inicie o programa `dht11_mqtt.py` no Raspberry Pi.
5. Abra o Frontend no navegador.
6. Aproxime e afaste um objeto do sensor para gerar novas medições.
7. Verifique se os dados aparecem no painel e no histórico.

## 16.9. Encerrar o sistema

Para encerrar os programas, utilize `Ctrl + C` nos terminais em que o Backend e o programa MQTT estão sendo executados.

Depois, feche o navegador e desconecte os componentes eletrônicos, quando necessário.

## 16.10. Observações

- O computador precisa ter acesso à internet para se comunicar com o broker público HiveMQ.
- O Raspberry Pi deve estar ligado e conectado ao Arduino.
- O tópico MQTT deve ser o mesmo no publicador e no receptor.
- O Backend e o Frontend utilizam o endereço local `127.0.0.1`.
- O arquivo `banco.db` é criado automaticamente pelo Backend caso ainda não exista.
- O Raspberry Pi e o computador precisam conseguir acessar a internet.
- O tópico utilizado no HiveMQ é público e não deve ser considerado privado.
- O arquivo `uv.lock` deve acompanhar o `pyproject.toml` no repositório para permitir a instalação das mesmas versões de dependências.

---

**Desenvolvido por:**

- Daniel Barreto de Paula
- Vinicius Araujo de Sousa
- Joao Marcos Marinho Baron

**Turma:** ADS2 — SENAI

**Instituição:** SENAI Conde José Vicente de Azevedo

**Projeto:** Monitoramento de Segurança Industrial — IoT

**Ano:** 2026
