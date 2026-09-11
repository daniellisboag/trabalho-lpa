# 💻 Trabalho Acadêmico — Lógica de Programação e Algoritmos

Este repositório reúne a resolução de quatro questões propostas em um trabalho acadêmico. Cada questão simula uma situação prática, aplicando conceitos fundamentais de lógica de programação e desenvolvimento em Python.

A seguir, cada questão é apresentada separadamente, incluindo **a descrição**, **o objetivo** e **os principais recursos de Python utilizados**.

## 🏥 Questão 01 — Cálculo de Plano de Saúde por Faixa Etária

### 📝 Descrição

Programa responsável por calcular o valor mensal de um plano de saúde com base na idade do cliente. Cada faixa etária possui uma porcentagem aplicada sobre um valor base informado pelo usuário.

### 🛠️ Recursos Utilizados

* `print()` para exibição de mensagens ao usuário
* `input()` para capturar o valor base e a idade
* Estruturas condicionais `if / elif / else`
* Operações matemáticas para aplicação das porcentagens
* Validação das faixas etárias
* Comentários explicativos no código

### 🎯 Objetivo

Simular uma regra de precificação de planos de saúde de acordo com diferentes faixas etárias.

## 🍕 Questão 02 — Sistema de Pedidos de Pizzaria

### 📝 Descrição

Sistema que permite escolher o sabor da pizza, entre doce ou salgado, e o tamanho desejado. Cada combinação possui um preço específico. O cliente pode realizar vários pedidos antes de encerrar o sistema.

### 🛠️ Recursos Utilizados

* `print()` para exibição do menu e das mensagens ao usuário
* `input()` para entrada e validação de dados
* Estruturas condicionais aninhadas `if / elif / else`
* Laços de repetição:
  * `while`
  * `break`
  * `continue`
* Acumulador para calcular o valor total dos pedidos
* Mensagens de erro para entradas inválidas
* Comentários explicativos no código

### 🎯 Objetivo

Simular um sistema simples de pedidos de pizzas, incluindo validação de entradas, cálculo do valor total e possibilidade de realizar múltiplos pedidos.

## 🪵 Questão 03 — Venda de Toras de Madeira

### 📝 Descrição

Sistema de vendas que permite selecionar o tipo de madeira, a quantidade de toras em m³ e o tipo de transporte. O valor final considera descontos e adicionais de acordo com regras predefinidas.

### 🛠️ Recursos Utilizados

* Funções:
  * `escolha_tipo()`
  * `qtd_toras()`
  * `transporte()`
* Uso de `return` para retornar valores, incluindo múltiplos retornos
* Laços de repetição para validação das entradas
* Tratamento de exceções com `try / except`
* Validação de limites numéricos, incluindo o limite máximo de 2000 m³
* Cálculos matemáticos para determinar o valor final da venda
* Comentários explicativos no código

### 🎯 Objetivo

Criar um sistema com regras de negócio, validação de entradas e modularização por meio da utilização de funções.

## 📇 Questão 04 — Sistema de Gerenciamento de Contatos

### 📝 Descrição

Sistema de gerenciamento de contatos que permite cadastrar, consultar e remover contatos. Os dados são armazenados como dicionários dentro de uma lista.

### 🛠️ Recursos Utilizados

* Lista de dicionários (`lista_contatos`)
* Variável incremental `id_global`
* Funções:
  * `cadastrar_contato()`
  * `consultar_contatos()`
  * `remover_contato()`
* Submenus com repetição até o usuário escolher retornar
* Estruturas condicionais e laços de repetição
* Consulta de todos os contatos cadastrados
* Validação de opções inválidas
* Uso de `.copy()` para armazenar os contatos de forma independente
* Busca por:
  * ID
  * Atividade
* Comentários explicativos no código

### 🎯 Objetivo

Criar um sistema de gerenciamento de contatos com funcionalidades de cadastro, consulta e remoção de dados, aplicando estruturas de dados, funções e validações em Python.

## 💻 Tecnologias Utilizadas

* **Python 3**
* **Visual Studio Code**

## 🎓 Conclusão

Este trabalho foi desenvolvido com foco na aplicação prática dos conceitos fundamentais de lógica de programação e Python.

As soluções apresentadas demonstram a utilização de estruturas condicionais, laços de repetição, funções, validação de dados, tratamento de exceções e estruturas de dados para a construção de sistemas funcionais e organizados.
