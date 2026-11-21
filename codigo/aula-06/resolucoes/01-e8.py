# Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/04 - Resoluções/resolucoes-aula-06.md (linha 61).
# Seção: E8
# Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
# Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resolucoes/01-e8.py
# A saída deve conter: TypeError

try:
    print(10 + "20")
except TypeError as e:
    print("TypeError:", e)   # unsupported operand type(s) for +: 'int' and 'str'
