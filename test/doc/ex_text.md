# Documentação Técnica: Classe `ComputingArchitectureSim`

Esta documentação detalha os métodos, lógicas de cálculo e regras de negócio implementadas no simulador de arquiteturas computacionais em Python. O objetivo do código é demonstrar a resiliência a ruídos elétricos do sistema binário em comparação ao decimal e avaliar o custo físico-lógico entre ambas as arquiteturas.

---

## 1. Construtor: `__init__(self, voltage_max=5.0, thermal_noise=-0.8)`
**Objetivo:** Inicializa as variáveis base para o ambiente de simulação elétrica.
- **`voltage_max` (5.0V):** Representa a tensão máxima do circuito de transmissão (comum em padrões de hardware clássicos, como no padrão TTL - *Transistor-Transistor Logic*).
- **`thermal_noise` (-0.8V):** Simula a perda de energia, interferência externa ou degradação do sinal (ruído térmico/atenuação). O valor negativo representa a queda estática de tensão que afetará o sinal transmitido durante os testes.

---

## PARTE 1: O Experimento de Margem de Ruído
Esta etapa verifica a viabilidade de se ler com precisão sinais fracionados versus sinais polares.

### Método: `simulate_decimal_hardware(self, target_number)`
**Objetivo:** Simular a tentativa de transmitir um dígito decimal (0 a 9) através de um único fio de cobre variando a tensão elétrica.
- **Regra de Cálculo (Fracionamento):** `voltage_step = self.voltage_max / 10`. O espectro de 5V é dividido em 10 degraus de 0.5V. Assim, a representação elétrica do numeral 0 é 0.0V, a do 1 é 0.5V, a do 2 é 1.0V, até o 9 que é 4.5V.
- **Transmissão e Ruído:** `received_voltage = transmitted_voltage + self.noise`. O sinal transmitido sofre a degradação física estática definida pelo construtor (-0.8V).
- **Regra de Leitura:** `round(received_voltage / voltage_step)`. O hardware receptor tenta deduzir qual foi o número enviado dividindo a tensão recebida pelo tamanho do degrau e arredondando para o inteiro mais próximo.
- **Tratamento de Exceção:** `max(0, read_number)` atua como uma barreira física que impede que a leitura resulte em índices de hardware negativos na simulação.
- **Por que usar essas regras?** Esse cálculo evidencia de forma prática a **fragilidade do sistema decimal em hardware**. Se um sistema transmitir o número 9 (4.5V) e ele sofrer o ruído de -0.8V, chegará 3.7V ao destino. O receptor fará o cálculo `3.7 / 0.5 = 7.4` e, ao arredondar, lerá o número `7`. A interferência causa uma corrupção crítica e direta da informação.

### Método: `simulate_binary_hardware(self, bit_value)`
**Objetivo:** Simular a transmissão de um único bit (0 ou 1) utilizando o mesmo fio e tensão máxima.
- **Regra de Cálculo (Polaridade Base):** O bit 1 é transmitido com tensão máxima (5.0V) e o bit 0 com ausência total de sinal (0.0V).
- **Transmissão e Ruído:** O mesmo ruído de -0.8V afeta a linha de transmissão, reduzindo a tensão que chega ao destino.
- **Regra de Leitura (Margem de Tolerância):**
  - Se a tensão recebida for **>= 3.0V**, a Unidade de Controle a interpreta como bit `1`.
  - Se a tensão recebida for **<= 2.0V**, interpreta-se como bit `0`.
  - Valores na faixa intermediária resultam em `None` (estado indefinido/erro).
- **Por que usar essas regras?** Esta lógica espelha matematicamente o funcionamento de transistores e portas lógicas no mundo real, que possuem faixas de imunidade a ruídos (Margem de Ruído). Ao transmitir um bit `1` (5.0V), o ruído de -0.8V diminui o sinal para 4.2V. Diferente da arquitetura decimal, 4.2V continua acima da margem de 3.0V, sendo lido de maneira íntegra e imaculada como `1`.

---

## PARTE 2: O Paradoxo do ENIAC (Custo Físico)
Esta seção calcula empiricamente as exigências de hardware para se montar os sistemas.

### Método: `calculate_eniac_valves(self, number)`
**Objetivo:** Calcular o número de componentes físicos necessários para armazenar um número decimal na abordagem mecânico/eletrônica adotada pelos pioneiros como o ENIAC.
- **Regra de Cálculo:** O código converte o número recebido em uma *string* (`str(number)`), mede seu comprimento em casas decimais (`len`) e multiplica essa contagem por 10.
- **Por que usar esse cálculo?** O ENIAC utilizava "contadores em anel" (*ring counters*) que exigiam estruturalmente cerca de 10 válvulas termiônicas dedicadas por casa decimal para armazenar com sucesso um único dígito em formato de base-10.

### Método: `calculate_binary_transistors(self, number)`
**Objetivo:** Calcular a quantidade de espaços em bits (equivalente conceitual a transistores em registradores primários) exigida para representar o mesmo número na arquitetura binária.
- **Regra de Cálculo:** Converte o número para binário `bin(number)`, corta o prefixo referencial `0b` criado nativamente pelo Python usando fatiamento `[2:]`, e retorna a quantidade exata de caracteres dessa nova *string*.
- **Por que usar esse cálculo?** No modelo binário moderno, elementos como *Flip-Flops* armazenam 1 bit de informação. Assim, contar o comprimento da representação binária fornece diretamente a densidade teórica de armazenamento exigida pelo hardware.

---

## PARTE 3: Custo Lógico vs Viabilidade Física

### Método: `compare_costs(self, number)`
**Objetivo:** Consolidar e expor os resultados das lógicas analisadas anteriormente para formular a conclusão.
- **Regra do Print/Output:** O método calcula os comprimentos da cadeia decimal e da cadeia binária e as exibe de forma comparativa.
- **Qual a importância desta função?** Ela estabelece o ponto alto da sua metodologia: provar o **Trade-off Lógico-Físico**. O texto de saída enfatiza que a representação binária é logicamente muito mais extensa (o que exige "cadeias de processamento mais extensas", como dito em sua metodologia). Porém, do ponto de vista de viabilidade e engenharia, imprimir e agrupar centenas de micro-componentes de apenas dois estados lógicos é muito mais eficiente, seguro e barato do que gerenciar macro-componentes altamente suscetíveis a distúrbios para processar dados em base dez.