# 🏭 Monitoramento de Segurança Industrial — IoT

## 📌 Sobre o Projeto

O projeto **Monitoramento de Segurança Industrial** tem como objetivo desenvolver um sistema capaz de detectar a aproximação de pessoas ou objetos de áreas de risco em ambientes industriais, utilizando sensores, alertas visuais e sonoros e, futuramente, recursos de Internet das Coisas (IoT).

O sistema utiliza um sensor ultrassônico para medir a distância de obstáculos. Conforme a distância detectada, LEDs indicam o nível de risco e um buzzer pode emitir alertas sonoros.

Além disso, a proposta prevê o registro das ocorrências em um banco de dados, permitindo consultar o histórico de eventos por meio de uma interface web ou aplicativo.

## 🎯 Objetivo

Desenvolver uma solução de baixo custo para auxiliar no monitoramento de áreas industriais, melhorar a sinalização de situações de risco e permitir o acompanhamento das ocorrências registradas.

## ⚠️ Problemas Identificados e Soluções

### 1. Aproximação de pessoas ou objetos de áreas perigosas

**Problema:** Pessoas podem se aproximar de máquinas ou áreas industriais perigosas sem perceber o risco de acidentes.

**Solução:** Utilizar um sensor ultrassônico para detectar obstáculos próximos e acionar alertas conforme a distância medida.

### 2. Falta de sinalização imediata de perigo

**Problema:** A ausência de uma sinalização clara pode dificultar a identificação de situações de risco pelo operador.

**Solução:** Utilizar LEDs para indicar diferentes níveis de alerta e um buzzer para emitir sinais sonoros quando um obstáculo estiver próximo.

- 🟢 **Verde:** condição normal.
- 🟡 **Amarelo:** atenção — obstáculo se aproximando.
- 🔴 **Vermelho:** perigo — obstáculo dentro da distância crítica.
- 🔊 **Buzzer:** alerta sonoro em situações de risco.

*As distâncias que definem cada nível de alerta serão configuradas durante o desenvolvimento.*

### 3. Ausência de histórico das ocorrências

**Problema:** Sem o registro dos alertas, fica difícil analisar a frequência das aproximações perigosas e identificar os momentos em que ocorreram.

**Solução:** Integrar o sistema a uma aplicação em Python e a um banco de dados para armazenar informações como data, horário, distância medida e nível do alerta.

## 🗺️ Arquitetura do Projeto

O projeto foi planejado em quatro camadas principais:

### 1. Captura — Arduino / Edge

O Arduino recebe as informações dos sensores e executa as ações locais de acordo com as regras programadas.

**Componentes e funções:**

- Sensor ultrassônico: mede a distância de obstáculos.
- LEDs: indicam o nível de risco.
- Buzzer: emite alertas sonoros.

### 2. Comunicação — Raspberry Pi 3B / MQTT

A Raspberry Pi 3B será utilizada como central de comunicação, executando o broker MQTT, por exemplo, o Mosquitto.

O MQTT permite transmitir mensagens entre os dispositivos de forma leve, facilitando a integração entre o sistema físico e a aplicação.

**Fluxo:** Arduino com conectividade de rede → MQTT → Raspberry Pi 3B.

> A comunicação direta com MQTT depende do hardware utilizado. Se o Arduino não possuir Wi-Fi ou Ethernet, será necessário utilizar um módulo de comunicação ou outro dispositivo intermediário.

### 3. Processamento — Python / API / Banco de Dados

Uma aplicação desenvolvida em Python receberá os dados publicados no MQTT, processará as informações e armazenará as ocorrências em um banco de dados.

A API permitirá que outros sistemas consultem os dados registrados.

**Responsabilidades:**

- Receber mensagens MQTT.
- Processar as medições e os níveis de alerta.
- Registrar o histórico de ocorrências.
- Disponibilizar dados por meio de rotas de API.

### 4. Visualização — Front-end / Aplicativo

Uma interface web ou aplicativo permitirá acompanhar as informações do sistema de maneira organizada.

**Funcionalidades planejadas:**

- Visualização da distância medida.
- Identificação do nível de risco atual.
- Consulta ao histórico de alertas.
- Apresentação de gráficos e indicadores.
- Possibilidade de enviar comandos remotos, caso essa funcionalidade seja implementada.

## 🔄 Fluxo de Funcionamento

1. O sensor ultrassônico mede a distância de um obstáculo.
2. O Arduino compara a distância com os limites configurados.
3. Os LEDs e o buzzer sinalizam a condição detectada.
4. Os dados são enviados pela comunicação MQTT, quando essa integração estiver implementada.
5. A aplicação Python recebe e processa os dados.
6. As ocorrências são armazenadas no banco de dados.
7. A interface web ou aplicativo apresenta as informações para consulta.

## 🧰 Tecnologias e Ferramentas

| Tecnologia             | Finalidade                                  |
| ---------------------- | ------------------------------------------- |
| Arduino                | Leitura dos sensores e controle dos alertas |
| Sensor ultrassônico    | Medição de distância                        |
| LEDs                   | Sinalização visual                          |
| Buzzer                 | Sinalização sonora                          |
| Tinkercad Circuits     | Simulação do circuito eletrônico            |
| Raspberry Pi 3B        | Hospedagem do broker MQTT                   |
| MQTT / Mosquitto       | Comunicação entre dispositivos              |
| Python                 | Processamento e integração dos dados        |
| API REST               | Disponibilização dos dados                  |
| Banco de dados         | Armazenamento do histórico                  |
| Front-end web / Mobile | Visualização das informações                |

*As tecnologias de comunicação, processamento, armazenamento e interface representam a arquitetura planejada. A implementação de cada uma será documentada conforme o desenvolvimento avançar.*

## 🔧 Simulação do Circuito

O circuito eletrônico está sendo desenvolvido e testado no Tinkercad.

🔗 [Acessar o projeto no Tinkercad](https://www.tinkercad.com/things/lWQVKVolQns/editel?returnTo=%2Fclassrooms%2FdTqchefUguY%2Factivities%2F17xV0nT7JVv)

## 🎥 Referência de Estudo

Vídeo utilizado como referência para aprender a configurar e testar o sensor:

🔗 [Assistir ao vídeo no YouTube](https://www.youtube.com/watch?v=J8F0scG1r64)

## 📈 Resultados Esperados

- Detectar obstáculos próximos de áreas monitoradas.
- Sinalizar diferentes níveis de risco visualmente.
- Emitir alertas sonoros em condições críticas.
- Criar um histórico de ocorrências para análise posterior.
- Permitir o monitoramento dos dados por uma interface digital.
- Demonstrar a integração entre eletrônica, programação e IoT.

## 🚀 Próximas Etapas

- [ ] Montar e testar o circuito no Tinkercad.
- [ ] Configurar os limites de distância para cada alerta.
- [ ] Implementar a lógica dos LEDs e do buzzer no Arduino.
- [ ] Definir o hardware e a comunicação de rede.
- [ ] Configurar o broker MQTT na Raspberry Pi 3B.
- [ ] Desenvolver a aplicação de recebimento dos dados em Python.
- [ ] Integrar o banco de dados.
- [ ] Criar a API para consulta das informações.
- [ ] Desenvolver a interface web ou aplicativo.
- [ ] Realizar testes integrados e documentar os resultados.

## 👨‍💻 Status do Projeto

**Em desenvolvimento.**

O projeto está na fase de estudo, simulação e implementação gradual das funcionalidades de monitoramento e comunicação.

---

