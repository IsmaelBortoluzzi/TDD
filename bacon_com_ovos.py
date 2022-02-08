"""
1 - receber um número inteiro

2 - saber se o número é múltiplo de 3 e 5:
    bacon com ovos

3 - saber se o número é múltiplo de 3 apenas:
    bacon

4 - saber se o número é múltiplo de 5 apenas:
    ovos

5 - saber se o número não é múltiplo de 3 ou de 5:
    passa fome
"""

def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser inteiro'

    if n % 3 == 0 and n % 5 == 0:
        return 'bacon com ovos'

    if n % 3 == 0:
        return 'bacon'

    if n % 5 == 0:
        return 'ovos'

    return 'passar fome'
