# Gerado automaticamente a partir de 01 - Aulas/Aula 11 - Paradigma Imperativo III/02 - Resumo Teórico/resumo-aula-11.md (linha 96).
# Seção: 4. Parâmetros (p.8–12)
# Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
# Como executar:  python3 ferramentas/rodar.py codigo/aula-11/resumo/02-4-parametros-p-8-12.py
# A saída deve conter: Nome: Maria | Cidade:  Lages | Nome: João | Cidade:  Florianópolis

def mostrar_usuario(nome, idade, cidade):
    print("Nome:", nome)
    print("Idade: ", idade)
    print("Cidade: ", cidade)

# Utilizando parâmetros posicionais
mostrar_usuario("Maria", 25, "Lages")

# Utilizando parâmetros nomeados 1
mostrar_usuario(nome="João", idade=30, cidade="Florianópolis")

# Utilizando parâmetros nomeados 2 (ordem livre)
mostrar_usuario(cidade="Florianópolis", nome="João", idade=30)
