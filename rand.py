from  random import randint

def create_buss(bus_len, min_points, max_points, min_viagens, max_viagens, max_passageiros_buss):
    filed = open("out.csv", "w")
    for buss in range(bus_len):
        points = randint(min_points, max_points)
        for viagens in range(min_viagens, max_viagens):
            current = 0
            filed.write(f"{buss},")
            for point in range(points):
                up = randint(0, max_passageiros_buss - current)
                current += up
                down = randint(0, current)
                current -= down
                filed.write(f"{up}:{down},")
            filed.write(f"0:{current}\n")
    

create_buss(bus_len = 30,  min_points = 10, max_points = 30, min_viagens = 5, max_viagens = 15, max_passageiros_buss = 50)