from src.calculadora import soma


try:
    print(soma(15, 15))
except AssertionError as e:
    print(e)

print('conta' + soma(20, 20))
