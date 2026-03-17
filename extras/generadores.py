habitaciones = [{"numero": 101, "disponible": True}, 
                {"numero": 102,"disponible": False},
                {"numero": 104, "disponible": True}, 
                {"numero": 105,"disponible": False},
                {"numero": 106, "disponible": True}, 
                {"numero": 107,"disponible": False},
                {"numero": 108, "disponible": True}, 
                {"numero": 109,"disponible": False},]


def filtrar(n): 
    text = input("Elige: 1.- Disponible / 2.- Ocupado: ")
    if text not in ["1", "2"]: 
        print("Opcion Inválida")
        return 
    for x in n: 
        if text == "1" and x["disponible"] == True: 
            yield x
        elif text == "2" and  x["disponible"] == False:
            yield x 
    

def search(n): 
    for i in filtrar(habitaciones): 
        print(f"Habitacion numero: {i['numero']}") 


search(habitaciones)