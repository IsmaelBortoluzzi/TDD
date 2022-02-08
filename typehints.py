from typing import List, Union


num: int = 10

lista: List[List[int]] = [
    [1, 2, 3],
    [1, 2, 3]
]

lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'Ola')

