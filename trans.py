def trans(n):
    zone = n % 10
    id = n // 10 + 1
    if(zone == 0):
        id -= 1
        return f"D1{id:02d}"
    elif(zone == 1):
        return f"A1{id:02d}"
    elif(zone == 2):
        return f"A2{id:02d}"
    elif(zone == 3):
        return f"A3{id:02d}"
    elif(zone == 4):
        return f"A4{id:02d}"
    elif(zone == 5):
        return f"B1{id:02d}"
    elif(zone == 6):
        return f"B2{id:02d}"
    elif(zone == 7):
        return f"B3{id:02d}"
    elif(zone == 8):
        return f"C1{id:02d}"
    elif(zone == 9):
        return f"C2{id:02d}" 
    

for i in range(1, 31):
    print(trans(i))