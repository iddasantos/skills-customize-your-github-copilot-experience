

# 📘 Assignment: Jogos em Python

## 🎯 Objetivo

Você irá criar jogos interativos em Python para praticar manipulação de strings, loops, condicionais e entrada do usuário.

## 📝 Tarefas

### 🛠️ Jogo da Forca (Hangman)

#### Description
Implemente o clássico jogo da forca, onde o jogador tenta adivinhar uma palavra secreta letra por letra antes de acabar as tentativas.

#### Requirements
Completed program should:

- Selecionar aleatoriamente uma palavra de uma lista pré-definida
- Aceitar palpites de letras do usuário e mostrar o progresso atual (ex: _ _ _ a _)
- Exibir o número de tentativas restantes para erros
- Encerrar o jogo quando a palavra for adivinhada ou as tentativas acabarem
- Exibir mensagens de vitória ou derrota

Exemplo de entrada/saída:
```python
Palavra secreta: abacate
_ _ _ _ _ _ _
Digite uma letra: a
a _ a _ a _ _
```

### 🛠️ Jogo de Adivinhação de Números

#### Description
Crie um jogo onde o computador escolhe um número aleatório e o jogador deve adivinhar, recebendo dicas se o palpite está acima ou abaixo do valor correto.

#### Requirements
Completed program should:

- Gerar um número aleatório dentro de um intervalo definido (ex: 1 a 100)
- Permitir que o usuário faça palpites sucessivos
- Informar se o palpite está acima ou abaixo do número correto
- Encerrar o jogo quando o número for adivinhado
- Exibir o número de tentativas realizadas
