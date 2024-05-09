# TPC6: Gramática LL(1) para GIC
## 2024-05-9
## Escrito por:
- A95338
- Maurício Miranda Pereira

# Gramática Livre de Contexto LL(1)

## Terminais

- **Números**: `0 | 1 | 2 | ...`
- **Variáveis**: `a | b | c | ...`
- **Operadores Aritméticos**: `+ | - | * | /`
- **Parênteses**: `( | )`
- **Sinal de Igualdade**: `=`
- **Símbolos de Leitura e Impressão**: `? | !`

## Não-Terminais

- **Programa**: `P`
- **Declaração**: `D`
- **Expressão**: `E`
- **Termo**: `T`
- **Fator**: `F`

## Produções

1. `P -> D P | ε`
2. `D -> ? var | var = E | ! E`
3. `E -> E + T | E - T | T`
4. `T -> T * F | T / F | F`
5. `F -> ( E ) | num | var`

## Conjuntos Lookahead

- **LA(P → D P)**: `?`, `var`, `!`
- **LA(P → ε)**: `EOF` (fim do ficheiro)
- **LA(D → ? var)**: `?`
- **LA(D → var = E)**: `var`
- **LA(D → ! E)**: `!`
- **LA(E → E + T)**: `+`, `-`, `(`, `num`, `var`
- **LA(E → E - T)**: `+`, `-`, `(`, `num`, `var`
- **LA(E → T)**: `(`, `num`, `var`
- **LA(T → T * F)**: `*`, `/`, `(`, `num`, `var`
- **LA(T → T / F)**: `*`, `/`, `(`, `num`, `var`
- **LA(T → F)**: `(`, `num`, `var`
- **LA(F → ( E ))**: `(`
- **LA(F → num)**: `num`
- **LA(F → var)**: `var`

Esta descrição define uma gramática livre de contexto para uma linguagem que respeita a prioridade dos operadores aritméticos e é determinística LL(1), garantindo que, para qualquer símbolo de entrada, há sempre apenas uma produção aplicável, conforme determinado pelo conjunto lookahead.