def adunare(num_1, num_2):
    return num_1 + num_2

def scadere(num_1, num_2):
    return num_1 - num_2

def inmultire(num_1, num_2):   
    return num_1 * num_2

def impartire(num_1, num_2):
    if num_2 == 0:
        return "Eroare: Impartire la 0"
    return num_1 / num_2

def calculator():
    case = {
        '+': adunare,
        '-': scadere,
        '*': inmultire,
        '/': impartire
    }
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

        try:
            num_1 = float(num_1)
            num_2 = float(num_2)
            if op in case:
                rez = case[op](num_1, num_2)
                print("Rezultat:", rez, "\n")
            else:
                print("Operatie invalida\n")
        except ValueError:
            print("Eroare: Introduceti numere valide\n")
calculator()

            
