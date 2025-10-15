def calculator():
    while True:
        num_1 = input("Numarul 1 (sau C / Q): ")

        if num_1.upper() == "Q":
            break
        if num_1.upper() == "C":
            print("Resetat.\n")
            continue

        num_2 = input("Numarul 2 (sau C / Q): ")

        if num_2.upper() == "Q":
            break
        if num_2.upper() == "C":
            continue

        op = input("Operatia (+-/*) (sau C / Q): ")

        if op.upper() == "Q":
            break
        if op.upper() == "C":
            continue

        if op == "/" and num_2 == "0":
            print("Nu poti imparti la 0\n")
            continue

        try:
            rez = eval(f"{num_1}{op}{num_2}")
            print("Rezultat:", rez, "\n")
        except:
            print("Eroare\n")

calculator()
