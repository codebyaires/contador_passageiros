# Lista de ônibus conhecida (cada item será um dicionário com linha e total de passageiros)
buss_list = []

with open('out.csv', 'r') as arquivo:
    for linha in arquivo:
        # Separa os elementos da linha pelas ',' 
        str_arr = linha.strip().split(",")

        # Pega os valores a partir da segunda coluna e extrai apenas o número antes do ':'
        valores = [int(item.split(':')[0]) for item in str_arr[1:]]

        # Soma os passageiros da linha atual
        soma = sum(valores)

        # Verifica se a linha já existe em buss_list
        found = False #cria uma variável booleana para marcar se a linha já existe
        for linha in buss_list:
            if linha["line"] == str_arr[0]:
                found = True
                # Se existir, acumula o total de passageiros
                linha["pass"] += soma

        # Se não existir, cria um novo dicionário e adiciona à lista
        if not found:
            buss_list.append({"line": str_arr[0], "pass": soma})

# Ordena a lista de dicionários pelo total de passageiros em ordem decrescente
buss_list = sorted(buss_list, key=lambda x: x["pass"], reverse=True) 

print(buss_list)