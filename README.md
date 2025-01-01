# Sistema Bancário

Este é um sistema bancário simples desenvolvido em Python que permite ao usuário realizar operações como depósito, saque e visualização de extrato. O sistema possui limitações para os saques diários, onde o usuário pode realizar no máximo 3 saques por dia, com um limite de R$ 500 por saque.

## Funcionalidades

- **Saque**: O usuário pode sacar um valor até R$ 500, sendo permitido no máximo 3 saques por dia.
- **Depósito**: O usuário pode realizar depósitos em sua conta, desde que o valor seja maior que zero.
- **Extrato**: O usuário pode visualizar o saldo atual, os depósitos realizados e os saques realizados.

## Requisitos

- Python 3.x

## Como usar

1. **Baixe ou clone o repositório**:
    - Você pode clonar o repositório utilizando o comando:
    ```bash
    git clone https://github.com/seu-usuario/sistema-bancario.git
    ```

2. **Execute o código**:
    - Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo `sistema_bancario.py` está localizado.
    - Execute o script com o comando:
    ```bash
    python sistema_bancario.py
    ```

3. **Opções do Menu**:
    - **[1] Saque**: Permite realizar um saque, respeitando o limite diário de R$ 500.
    - **[2] Depósito**: Permite realizar um depósito na conta.
    - **[3] Extrato**: Exibe o saldo atual, os depósitos e os saques realizados.
    - **[0] Sair**: Encerra o sistema.

## Limitações

- O sistema permite realizar no máximo 3 saques por dia.
- O valor máximo de cada saque é de R$ 500.
- Apenas depósitos maiores que zero são aceitos.

## Exemplos de Entrada e Saída

**Entrada:**
Digite a opção desejada: 1
Digite o valor do Saque: R$100

**Saída:**
Saque de R$100.00 realizado com sucesso!

**Entrada:**
Digite a opção desejada: 3

**Saída:**
Seu saldo atual é: R$100.00

Depósitos realizados: R$100.00

Saques realizados: R$100.00

## Contribuições

Sinta-se à vontade para contribuir com melhorias neste projeto. Se você encontrar algum erro ou tiver sugestões de melhorias, crie uma issue ou um pull request.

