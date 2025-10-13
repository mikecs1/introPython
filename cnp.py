from datetime import date

LOCATII = {
    "01": "Alba",
    "02": "Arad",
    "03": "Argeș",
    "04": "Bacău",
    "05": "Bihor",
    "06": "Bistrița-Năsăud",
    "07": "Botoșani",
    "08": "Brașov",
    "09": "Brăila",
    "10": "Buzău",
    "11": "Caraș-Severin",
    "12": "Cluj",
    "13": "Constanța",
    "14": "Covasna",
    "15": "Dâmbovița",
    "16": "Dolj",
    "17": "Galați",
    "18": "Gorj",
    "19": "Harghita",
    "20": "Hunedoara",
    "21": "Ialomița",
    "22": "Iași",
    "23": "Ilfov",
    "24": "Maramureș",
    "25": "Mehedinți",
    "26": "Mureș",
    "27": "Neamț",
    "28": "Olt",
    "29": "Prahova",
    "30": "Satu Mare",
    "31": "Sălaj",
    "32": "Sibiu",
    "33": "Suceava",
    "34": "Teleorman",
    "35": "Timiș",
    "36": "Tulcea",
    "37": "Vaslui",
    "38": "Vâlcea",
    "39": "Vrancea",
    "40": "București",
    "41": "București - Sector 1",
    "42": "București - Sector 2",
    "43": "București - Sector 3",
    "44": "București - Sector 4",
    "45": "București - Sector 5",
    "46": "București - Sector 6",
    "51": "Călărași",
    "52": "Giurgiu",
}

def read_cnp():
    while True:
        cnp = input("Introduceti CNP : ")
        if len(cnp) != 13:
            print("Invalid, CNP-ul trebuie sa contina 13 cifre")
            continue
        if not cnp.isdigit():
            print("Invalid, CNP-ul trebuie sa contina doar cifre")
            continue
        return cnp

def secol_sex(s_digit: int) -> tuple[int, str]:
    if s_digit in (1, 2):
        secol = 1900
    elif s_digit in (3, 4):
        secol = 1800
    elif s_digit in (5, 6):
        secol = 2000
    elif s_digit in (7, 8, 9):
        secol = 1900
    else:
        raise ValueError("Cifra S invalida")
    
    if s_digit % 2 == 1:
        sex = "masculin"
    else: sex = "feminin"

    return secol, sex

def zi_nastere(cnp: str) -> date:

    s = int(cnp[0])
    aa = int(cnp[1:3])
    ll = int(cnp[3:5])
    zz = int(cnp[5:7])
    
    secol, _ = secol_sex(s)
    an = secol + aa
    return date(an, ll, zz) 

def judet(jj: str) -> str | None:
    if jj in ("00", "47", "48"):
        return None
    return LOCATII.get(jj)


def valideaza_cnp(cnp: str):
    print(f"\n--- Validare CNP: {cnp} ---")


    s_digit = int(cnp[0])
    secol, sex = secol_sex(s_digit)
        
    data_nastere = zi_nastere(cnp)
        
    cod_judet = cnp[7:9]
    nume_judet = judet(cod_judet)
        
    if nume_judet is None:
        print(f" Cod județ invalid: {cod_judet}")
        return
        
    print("\n--- Informații extrase din CNP ---")
    print(f"Sex: {sex}")
    print(f"Data nașterii: {data_nastere.strftime('%d.%m.%Y')}")
    print(f"Locul nașterii: {nume_judet} (cod: {cod_judet})")
        
    if s_digit in (7, 8):
        print("Observație: Persoană străină rezidentă în România")
    elif s_digit == 9:
        print("Observație: Persoană străină")
            
def main():
    print("=== VALIDATOR CNP ROMÂNESC ===")
    cnp = read_cnp()
    valideaza_cnp(cnp)

if __name__ == "__main__":
    main()