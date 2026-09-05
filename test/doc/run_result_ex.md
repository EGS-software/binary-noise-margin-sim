# Resultados da Simulação: Arquitetura Binária vs. Decimal

Este documento apresenta os resultados da simulação computacional desenvolvida para validar a superioridade da arquitetura binária sobre a decimal em sistemas eletrônicos de computação.

A simulação testou três cenários principais: a tolerância ao ruído elétrico, o custo de componentes físicos e a viabilidade lógica de produção.

---

## 1. O Experimento da Margem de Ruído (Tolerância a Falhas)

Foi simulado um ambiente de hardware operando a **5.0V**, submetido a um estresse de "ruído térmico" que causou uma queda de tensão aleatória de **-0.8V**.

*   **Computador Decimal (Alvo: Número 8 / 4.0V):**
    *   Tensão enviada: 4.0V
    *   Impacto do ruído: -0.8V
    *   Tensão recebida: 3.2V
    *   **Resultado:** O hardware leu o valor "6". **O dado foi corrompido.**

*   **Computador Binário (Alvo: Bit 1 / 5.0V):**
    *   Tensão enviada: 5.0V
    *   Impacto do ruído: -0.8V
    *   Tensão recebida: 4.2V
    *   **Resultado:** O hardware continuou lendo perfeitamente o "1". **O dado sobreviveu ao ruído.**

> **Conclusão 1:** O sistema binário possui uma margem de ruído brutalmente superior, tornando-o indestrutível contra variações elétricas comuns que destruiriam a informação em um sistema decimal.

---

## 2. O Paradoxo do ENIAC (Custo Físico)

Para provar o custo físico de forçar a "mecânica decimal" na eletrônica, comparamos o armazenamento do número **395** em ambas as arquiteturas.

*   **Arquitetura Decimal (Modelo ENIAC):** Exigiu **30 válvulas** configuradas em anel para armazenar os 3 dígitos decimais.
*   **Arquitetura Moderna (Binária):** Exigiu apenas **9 componentes** físicos (transistores) para armazenar a cadeia de bits correspondente (`110001011`).

> **Conclusão 2:** A conversão para binário reduz drasticamente o número de componentes físicos necessários, diminuindo a geração de calor e a taxa de falhas do hardware.

---

## 3. Custo Lógico vs. Viabilidade Física (Gargalo da Fotolitografia)

A conversão de bases numéricas gera um *trade-off* (custo-benefício) claro:

*   Tamanho da informação em Decimal: **3 dígitos**
*   Tamanho da informação em Binário: **9 bits**

Embora o sistema binário gere cadeias lógicas mais longas (maior custo lógico de processamento), a viabilidade física compensa. 

> **Conclusão Final:** A engenharia aceitou trabalhar com códigos longos de 0s e 1s porque fabricar **9 micro-transistores** em paralelo (via fotolitografia em wafers de silício, operando por saturação e corte) é infinitamente mais viável e eficiente do que tentar miniaturizar **30 macro-componentes** decimais complexos.