# pylint: disable=invalid-name
from typing import Final, List, Optional
import ply.lex as lex
import json

from dataclasses import dataclass

@dataclass
class Item:
    codigo: str
    nome: str
    quantidade: int
    preco: float

coins: Final[List[float]] = [
    2.00,
    1.00,
    0.50,
    0.20,
    0.10,
    0.05,
    0.02,
    0.01
]

def calcular_troco(troco: float) -> List[int]:
    resultado = []
    for moeda in coins:
        resultado.append(int(troco // moeda))
        troco %= moeda
    
    return resultado

def imprimir_troco_bonito(troco: List[int]) -> None:
    for i, moeda in enumerate(coins):
        if troco[i] > 0:
            print(f"{troco[i]} moedas de {moeda:.2f}€")

class MaquinaDeVendas:
    tokens = (
        "LISTAR",
        "SAIR",
        "MOEDA",
        "ITEM"
    )

    states = (
        ("INSERIRMOEDAS", "exclusive"),
        ("SELECAODEITEM", "exclusive")
    )

    t_ANY_ignore = " \t\n"
    t_INSERIRMOEDAS_ignore = ", \t\n"

    def __init__(self):
        self.lexer: Optional[lex.Lexer] = None
        self.sair: bool = False
        
        self.total: float = 0.0
        self.items: List[Item] = []

    def configurar(self, **kwargs) -> None:
        self.lexer = lex.lex(module=self, **kwargs)
        self.carregar_items()

    def carregar_items(self) -> None:
        with open("items.json", encoding="utf-8") as arquivo:
            self.items = [Item(**item) for item in json.load(arquivo)]

    def t_begin_INSERIRMOEDAS(self, t):
        r"MOEDA"
        t.lexer.begin("INSERIRMOEDAS")

    def t_INSERIRMOEDAS_MOEDA(self, t):
        r"2e|1e|50c|20c|10c|5c|2c|1c"
        if t.value[-1] == "c":
            t.value = int(t.value[:-1]) / 100
        elif t.value[-1] == "e":
            t.value = int(t.value[:-1])

        self.total += t.value
        return t
    
    def t_INSERIRMOEDAS_SAIR(self, t):
        r"SAIR"
        print("Total atual: {:.2f}".format(self.total))
        t.lexer.begin("INITIAL")

    def t_begin_SELECAODEITEM(self, t):
        r"PRODUTO"
        t.lexer.begin("SELECAODEITEM")

    def t_SELECAODEITEM_PRODUTO(self, t):
        r"[0-9]{2}"
        t.lexer.begin("INITIAL")

        for item in self.items:
            if item.codigo == t.value:
                if item.quantidade <= 0:
                    print("Produto fora de estoque")
                    return t
                
                if self.total < item.preco:
                    print("Fundos insuficientes")
                    return t
                
                self.total -= item.preco
                item.quantidade -= 1
                print("Produto adquirido: {}".format(item.nome))
                print("Total atual: {:.2f}€".format(self.total))
                return t
            
        print("Produto não encontrado")
        return t
    
    def t_ANY_error(self, t):
        print("Caractere ilegal '{}'".format(t.value[0]))
        t.lexer.skip(1)

    def t_LISTAR(self, t):
        r"LISTAR"
        for item in self.items:
            print(f"{item.codigo} - {item.nome} - {item.preco}€")
        
        return t
    
    def t_SAIR(self):
        r"SAIR"
        self.sair = True

        troco = calcular_troco(self.total)
        imprimir_troco_bonito(troco)

        print("Obrigado por usar nossa máquina de vendas!")

def principal() -> None:
    maquina = MaquinaDeVendas()
    maquina.configurar()

    while not maquina.sair:
        linha = input(">>> ")
        maquina.lexer.input(linha)

        while True:
            token = maquina.lexer.token()
            if not token:
                break


if __name__ == "__main__":
    principal()
