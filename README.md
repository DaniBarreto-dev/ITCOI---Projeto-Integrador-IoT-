# Monitoramento de Segurança Industrial — IoT

## 1. Sobre o Projeto

O projeto **Monitoramento de Segurança Industrial** tem como objetivo desenvolver um sistema capaz de detectar a aproximação de pessoas ou objetos de áreas de risco em ambientes industriais, utilizando sensores, alertas visuais e sonoros e recursos de Internet das Coisas (IoT) como evolução futura.

O protótipo utiliza um Arduino Uno e um sensor ultrassônico HC-SR04 para medir a distância de obstáculos. Conforme a distância detectada, LEDs verdes, amarelos e vermelhos indicam diferentes níveis de risco, enquanto um buzzer emite alertas sonoros.

O projeto também prevê a integração com uma aplicação em Python, comunicação MQTT e um banco de dados, permitindo registrar e consultar o histórico das ocorrências por meio de uma interface web ou aplicativo.

## 2. Objetivo

Desenvolver uma solução de baixo custo para auxiliar no monitoramento de áreas industriais, melhorar a sinalização de situações de risco e possibilitar o acompanhamento das ocorrências registradas.

## 3. Problemas Identificados e Soluções

### 3.1. Aproximação de pessoas ou objetos de áreas perigosas

**Problema:** Pessoas podem se aproximar de máquinas ou áreas industriais perigosas sem perceber o risco de acidentes.

**Solução:** Utilizar um sensor ultrassônico para detectar obstáculos próximos e acionar alertas conforme a distância medida.

### 3.2. Falta de sinalização imediata de perigo

**Problema:** A ausência de uma sinalização clara pode dificultar a identificação de situações de risco pelo operador.

**Solução:** Utilizar LEDs para indicar diferentes níveis de alerta e um buzzer para emitir sinais sonoros quando um obstáculo estiver próximo.

Os níveis de sinalização previstos são:

- **Verde:** condição normal.
- **Amarelo:** atenção — obstáculo em uma faixa intermediária de distância.
- **Vermelho:** perigo — obstáculo dentro da distância crítica.
- **Buzzer:** alerta sonoro em situações de atenção ou perigo.

As distâncias de cada nível serão configuradas e validadas durante os testes do circuito.

### 3.3. Ausência de histórico das ocorrências

**Problema:** Sem o registro dos alertas, fica difícil analisar a frequência das aproximações perigosas e identificar quando ocorreram.

**Solução:** Integrar o sistema a uma aplicação em Python e a um banco de dados para armazenar informações como data, horário, distância medida e nível do alerta.

Essa funcionalidade faz parte das etapas futuras do projeto.

## 4. Componentes do Protótipo

| Componente | Função |
|---|---|
| Arduino Uno | Controlar o circuito e processar as medições |
| Sensor ultrassônico HC-SR04 | Medir a distância dos obstáculos |
| LEDs verdes | Indicar condição normal |
| LEDs amarelos | Indicar condição de atenção |
| LEDs vermelhos | Indicar situação de perigo |
| Resistores | Limitar a corrente dos LEDs |
| Buzzer | Emitir alertas sonoros |
| Protoboard | Facilitar as conexões do circuito |
| Jumpers | Realizar as ligações entre os componentes |

## 5. Arquitetura do Projeto

A arquitetura planejada possui quatro camadas principais, responsáveis pela captura, comunicação, processamento e visualização dos dados.

### 5.1. Captura — Arduino / Edge

O Arduino recebe as informações do sensor ultrassônico, calcula a distância aproximada do obstáculo e executa as ações locais de acordo com as condições programadas.

Responsabilidades:

- Realizar a leitura do sensor ultrassônico.
- Calcular a distância do obstáculo.
- Classificar o nível de alerta.
- Controlar os LEDs.
- Acionar o buzzer conforme a condição detectada.

### 5.2. Comunicação — Raspberry Pi 3B / MQTT

A Raspberry Pi 3B será utilizada como central de comunicação, executando um broker MQTT, como o Mosquitto.

O MQTT permitirá transmitir os dados do monitoramento entre os dispositivos e a aplicação responsável pelo processamento.

**Fluxo planejado:** Arduino com conectividade de rede → MQTT → Raspberry Pi 3B.

O Arduino Uno convencional não possui Wi-Fi integrado. Será necessário utilizar um módulo de comunicação, uma placa compatível com rede ou um dispositivo intermediário para enviar os dados.

### 5.3. Processamento — Python / API / Banco de Dados

Uma aplicação desenvolvida em Python receberá os dados publicados no MQTT, processará as informações e armazenará as ocorrências em um banco de dados.

A API permitirá que a interface consulte os dados registrados.

Responsabilidades planejadas:

- Receber mensagens MQTT.
- Processar as medições e os níveis de alerta.
- Registrar o histórico de ocorrências.
- Disponibilizar os dados por meio de rotas de API.

### 5.4. Visualização — Front-end / Aplicativo

Uma interface web ou aplicativo permitirá acompanhar as informações do sistema de maneira organizada.

Funcionalidades planejadas:

- Visualização da distância medida.
- Identificação do nível de risco atual.
- Consulta ao histórico de alertas.
- Apresentação de gráficos e indicadores.
- Possibilidade de enviar comandos remotos, caso essa funcionalidade seja implementada.

## 6. Fluxo de Funcionamento

O funcionamento atual do protótipo segue estas etapas:

1. O sensor ultrassônico mede a distância de um obstáculo.
2. O Arduino calcula a distância a partir do tempo de retorno do sinal ultrassônico.
3. O programa verifica em qual faixa de distância o obstáculo se encontra.
4. Os LEDs indicam a condição detectada.
5. O buzzer emite sinais sonoros quando as condições programadas exigem um alerta.
6. A distância medida é enviada ao Monitor Serial para acompanhamento durante os testes.

Nas próximas etapas, os dados poderão ser enviados via MQTT, processados por uma aplicação Python, armazenados em um banco de dados e apresentados em uma interface web.

## 7. Código do Arduino

O programa foi desenvolvido em C++ para Arduino e utiliza a função `pulseIn()` para medir a duração do sinal recebido pelo sensor ultrassônico.

A lógica implementada controla os LEDs de acordo com a distância e utiliza as funções `tone()` e `noTone()` para gerar os alertas sonoros.

O código original utilizado na simulação está disponível abaixo.

```cpp
void setup()
{
  Serial.begin(9600);

  pinMode(7, OUTPUT);
  pinMode(6, INPUT);

  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);
}

void loop()
{
  digitalWrite(7, HIGH);
  delayMicroseconds(2);
  digitalWrite(7, HIGH);
  delayMicroseconds(10);
  digitalWrite(7, LOW);

  long time = pulseIn(6, HIGH);
  float distancia = (time * 0.0001 * 349) / 2;

  if (distancia > 50) {
    digitalWrite(9, HIGH);
    digitalWrite(8, HIGH);
    digitalWrite(5, LOW);
    digitalWrite(4, LOW);
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
  }
  else if (distancia >= 30 && distancia <= 70) {
    digitalWrite(5, HIGH);
    digitalWrite(4, HIGH);
    digitalWrite(9, LOW);
    digitalWrite(8, LOW);
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);

    tone(11, 500);
    delay(500);
    noTone(11);
    delay(100);
  }
  else {
    digitalWrite(3, HIGH);
    digitalWrite(2, HIGH);
    digitalWrite(5, LOW);
    digitalWrite(4, LOW);
    digitalWrite(9, LOW);
    digitalWrite(8, LOW);

    tone(11, 2000);
    delay(500);
    noTone(11);
    delay(100);
  }

  Serial.println(distancia);
}
```

### Observações sobre o código

- O pino 7 deve gerar um pulso de disparo correto para o sensor ultrassônico. No código original, o sinal é colocado em `HIGH` duas vezes; a sequência deve ser revisada para iniciar em `LOW`, gerar o pulso e retornar a `LOW`.
- As condições de distância se sobrepõem entre 50 e 70 cm. É necessário definir faixas sem sobreposição para garantir o funcionamento esperado dos três níveis de alerta.
- Os pinos dos LEDs foram configurados como `OUTPUT`, pois o Arduino precisa controlar seu estado.
- O código utiliza o pino 11 para o buzzer, que deve estar conectado de acordo com essa configuração.
- A fórmula de distância deve ser validada durante os testes para garantir que o resultado esteja em centímetros.
- O código acima documenta a versão original da simulação; os ajustes indicados ainda precisam ser validados.

## 8. Tecnologias e Ferramentas

| Tecnologia | Finalidade |
|---|---|
| Arduino Uno | Leitura do sensor e controle dos alertas |
| C++ / Arduino IDE | Programação do microcontrolador |
| Sensor ultrassônico HC-SR04 | Medição de distância |
| Tinkercad Circuits | Simulação do circuito eletrônico |
| Raspberry Pi 3B | Hospedagem planejada do broker MQTT |
| MQTT / Mosquitto | Comunicação entre dispositivos |
| Python | Processamento e integração dos dados |
| API REST | Disponibilização dos dados |
| Banco de dados | Armazenamento do histórico |
| Front-end web / Mobile | Visualização das informações |

As tecnologias de comunicação, processamento, armazenamento e interface fazem parte da arquitetura planejada. Sua implementação será documentada conforme o desenvolvimento avançar.

## 9. Simulação do Circuito

O circuito eletrônico está sendo desenvolvido e testado no Tinkercad.

[Acessar o projeto no Tinkercad](https://www.tinkercad.com/things/lWQVKVolQns/editel?returnTo=%2Fclassrooms%2FdTqchefUguY%2Factivities%2F17xV0nT7JVv)

## 10. Referências de Estudo

Os vídeos abaixo foram utilizados como materiais de estudo para a montagem, configuração e programação do circuito.

- [Vídeo 1 — Referência para o funcionamento do sensor ultrassônico](https://www.youtube.com/watch?v=J8F0scG1r64)
- [Vídeo 2 — Material complementar de estudo](https://www.youtube.com/watch?v=C_RopzWOPgc)
- [Vídeo 3 — Material complementar de estudo](https://www.youtube.com/watch?v=vEdYjAbzrAE)

## 11. Resultados Esperados

- Detectar obstáculos próximos de áreas monitoradas.
- Sinalizar diferentes níveis de risco visualmente.
- Emitir alertas sonoros em condições críticas.
- Criar um histórico de ocorrências para análise posterior.
- Permitir o monitoramento dos dados por uma interface digital.
- Demonstrar a integração entre eletrônica, programação e IoT.

## 12. Próximas Etapas

- [x] Montar o circuito no Tinkercad.
- [ ] Testar e validar o funcionamento do circuito.
- [ ] Corrigir a lógica de disparo e medição do sensor ultrassônico.
- [ ] Definir limites de distância sem sobreposição entre os alertas.
- [ ] Validar a sinalização dos LEDs e o funcionamento do buzzer.
- [ ] Definir o hardware e a comunicação de rede.
- [ ] Configurar o broker MQTT na Raspberry Pi 3B.
- [ ] Desenvolver a aplicação de recebimento dos dados em Python.
- [ ] Integrar o banco de dados.
- [ ] Criar a API para consulta das informações.
- [ ] Desenvolver a interface web ou aplicativo.
- [ ] Realizar testes integrados e documentar os resultados.

## 13. Limitações de Segurança

Este projeto é um protótipo educacional destinado a demonstrar conceitos de monitoramento industrial e IoT. Ele não substitui dispositivos de segurança industrial certificados, como cortinas de luz, scanners de segurança ou sistemas de parada de emergência.

A aplicação em ambientes industriais reais exige avaliação de riscos, validação técnica e utilização de equipamentos adequados por profissionais qualificados.

## 14. Status do Projeto

**Em desenvolvimento.**

O protótipo encontra-se na fase de simulação e implementação do circuito com Arduino, sensor ultrassônico, LEDs e buzzer. A integração com MQTT, Python, banco de dados e interface digital está prevista para as próximas etapas.
