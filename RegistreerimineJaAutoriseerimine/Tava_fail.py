from MyModule import *

while True:
    print("\n=== MENÜÜ ===")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime või parooli muutmine")
    print("4 - Parooli taastamine")
    print("5 - Lõpetamine")

    valik = input("Vali tegevus: ")

    if valik == "1":
        register_user()
    elif valik == "2":
        authorize()
    elif valik == "3":
        change_credentials()
    elif valik == "4":
        recover_password()
    elif valik == "5":
        print("Head aega")
        break
    else:
        print("Tundmatu valik")