from random import *
from string import *
from os import *

kasutajad = []
paroolid = []

def generate_passwords():
    """
    Genereerib juhusliku, tugeva 12-tähemärgilise parooli, mis sisaldab numbreid, tähti ja sümboleid.
    """
    chars = ascii_letters + digits + ".,:;!_*-+()/#%&"
    ls = list(chars)
    shuffle(ls)
    return ''.join([choice(ls) for x in range(12)])

def is_valid_password(parool: str):
    """
    Nad kontrollivad, kas parool vastab kõigile nõuetele.
    - Kas parool siseldab numbrit?
    - Kas parool siseldab väikest tähte?
    - Kas parool siseldab suurt tähte?
    - Kas parool siseldab erimärki?
    """
    on_numbrit = False
    on_väikset = False
    on_suured = False
    on_erimärk = False

    for ch in parool:
        if ch.isdigit():
            on_numbrit = True
        elif ch.islower():
            on_väikset = True
        elif ch.isupper():
            on_suured = True
        else:
            on_erimärk = True

    return on_numbrit and on_väikset and on_suured and on_erimärk

def register_user():
    """
    Registreeri uus kasutaja kasutajanime ja parooliga.
    Kasutaja saab valida, kas parool genereeritakse automaatselt või saab selle ise luua.
    Kasutajanimi peab olema unikaalne.
    """
    kasutaja = str(input("Siseta uus kasutajanimi: "))
    
    if kasutaja in kasutajad:
        print("Kasutajanimi on juba olemas!")
        return

    print("Vali parooli loomise viis:")
    print("1 - Automaatne parooli genereerimine")
    print("2 - Loon ise parooli")
    valik = input("Valik: ")

    if valik == "1":
        parool = generate_passwords()
        print("Sinu parool: ", parool)
    elif valik == "2":
        parool = str(input("Siseta parool: "))
        if not is_valid_password(parool):
            print("Sinu parool ei vasta nõutele!")
            return
    else:
        print("Tundmatu valik!")
        return

    kasutajad.append(kasutaja)
    paroolid.append(parool)
    print("Kasutaja on edukalt lootud!")

def authorize():
    """
    Võimaldab kasutajal sisse logida, sisestades oma sisselogimise ja parooli
    """
    kasutaja = str(input("Sisesta kasutajanimi: "))
    parool = str(input("Sisesta parool: "))

    if kasutaja in kasutajad:
        idx = kasutajad.index(kasutaja)
        if paroolid[idx] == parool:
            print("Sisselogimine õnnestus!")
        else:
            print("Vale parool!")
    else:
        print("Sellist kasutajat pole olemas.")

def change_credentials():
    """
    Võimaldab teil muuta olemasoleva konto nime või parooli.
    Teave peab vastama praeguse konto omale.
    """
    kasutaja = str(input("Sisesta praegune kasutajanimi: "))
    parool = str(input("Sisesta praegune parool: "))

    if kasutaja not in kasutajad:
        print("Kasutajad pole!")
        return

    idx = kasutajad.index(kasutaja)
    if paroolid[idx] != parool:
        print("Vale parool!")
        return

    print("1 - Muuda kasutajanime")
    print("2 - Muuda parooli")
    valik = input("Valik: ")

    if valik == "1":
        uus_kasutajanimi = str(input("Sisesta uus kasutajanimi: "))
        if uus_kasutajanimi in kasutajad:
            print("Selline nimi on juba olemas!")
            return

        kasutajad[idx] = uus_kasutajanimi
        print("Kasutajanimi on muudetud!")

    elif valik == "2":
        uus_parool = str(input("Sisesta uus parool: "))

        if not is_valid_password(uus_parool):
            print("Parool ei vasta nõuetele!")
            return

        paroolid[idx] = uus_parool
        print("Parool on muudetud")
    else:
        print("Tundmatu valik!")

def recover_password():
    """
    Näitab kasutaja määratud konto seotud parooli.
    """
    kasutajanimi = str(input("Sisesta kasutajanimi: "))

    if kasutajanimi in kasutajad:
        idx = kasutajad.index(kasutajanimi)
        print("Sinu parool on ", paroolid[idx])
    else:
        print("Sellist kasutajad pole!")