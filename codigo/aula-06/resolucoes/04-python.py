# Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/04 - Resoluções/resolucoes-aula-06.md (linha 122).
# Seção: Python
# Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
# Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resolucoes/04-python.py
# A saída deve conter: x eh <class 'int'> | y eh <class 'str'> | w eh <class 'float'> | TypeError

x = 10
y = "20"
w = 10.2
print("x eh", type(x))
print("y eh", type(y))
print("w eh", type(w))
try:
    z = x + y + w
    print("Resultado(x+y+w):", z)
except TypeError as erro:
    print("TypeError:", erro)              # Python recusa int + str
print("Resultado com conversao:", x + int(y) + w)   # 40.2
