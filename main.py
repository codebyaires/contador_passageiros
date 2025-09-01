buss_list = []

with open('out.csv', 'r') as arquivo:
    for linha in arquivo:
        
        str_arr = linha.strip().split(",")
        
        valores = [int(item.split(':')[0]) for item in str_arr[1:]]

        soma = sum(valores)

        
        found = False 
        for linha in buss_list:
            if linha["line"] == str_arr[0]:
                found = True
   
                linha["pass"] += soma

        if not found:
            buss_list.append({"line": str_arr[0], "pass": soma})

buss_list = sorted(buss_list, key=lambda x: x["pass"], reverse=True) 

print(buss_list)