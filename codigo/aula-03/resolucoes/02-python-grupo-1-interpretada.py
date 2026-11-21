# Gerado automaticamente a partir de 01 - Aulas/Aula 03 - Implementação das Linguagens/04 - Resoluções/resolucoes-aula-03.md (linha 87).
# Seção: Python (Grupo 1, interpretada)
# Não edite aqui: altere o Markdown e rode  python3 ferramentas/gerar_codigo.py
# Como executar:  python3 ferramentas/rodar.py codigo/aula-03/resolucoes/02-python-grupo-1-interpretada.py
# Entrada de exemplo: 5 ⏎ 3 ⏎ 9 ⏎ 1 ⏎ 7 ⏎ 2 ⏎ 8 ⏎ 6 ⏎ 4 ⏎ 10
# A saída deve conter: Media: 5.50 | Maior: 10.00 | Menor: 1.00

nums = [float(input()) for _ in range(10)]   # lê 10 valores
print(f"Media: {sum(nums) / len(nums):.2f}")
print(f"Maior: {max(nums):.2f}")
print(f"Menor: {min(nums):.2f}")
