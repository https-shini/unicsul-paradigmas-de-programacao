# Gerado automaticamente a partir de 01 - Aulas/Aula 06 - Sistema de Tipos/02 - Resumo Teórico/resumo-aula-06.md (linha 105).
# Seção: 5. Tipagem estática × dinâmica (p.9–14)
# Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
# Como executar:  python3 ferramentas/rodar.py codigo/aula-06/resumo/03-5-tipagem-estatica-dinamica-p-9-14.py
# A saída deve conter: x eh <class 'int'> | x eh <class 'float'> | x eh <class 'str'>

x = 10
print("x eh", type(x))     # <class 'int'>
x = 10.2
print("x eh", type(x))     # <class 'float'>
x = "Universidade Cruzeiro do Sul"
print("x eh", type(x))     # <class 'str'>
z = x
print(z)
print("z eh", type(x))     # [Atenção] no slide está type(x); o esperado seria type(z)
