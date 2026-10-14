#!/usr/bin/env python3

def verifier_imei(imei):
    if len(imei) != 15 or not imei.isdigit():
        return False, "L'IMEI doit contenir exactement 15 chiffres."

    chiffres = [int(c) for c in imei]
    total = 0

    for i, chiffre in enumerate(chiffres):
        if i % 2 == 1:
            chiffre *= 2
            if chiffre > 9:
                chiffre -= 9
        total += chiffre

    if total % 10 == 0:
        return True, "IMEI mathématiquement valide."

    return False, "IMEI invalide : clé de contrôle incorrecte."


def main():
    print("=" * 35)
    print("       IMEI-TRACKER09")
    print("=" * 35)

    while True:
        imei = input("\nEntrez un IMEI (q pour quitter) : ").strip()

        if imei.lower() == "q":
            print("Fermeture du programme.")
            break

        valide, message = verifier_imei(imei)
        statut = "[OK] " if valide else "[ERREUR] "
        print(statut + message)
        print("Ce contrôle ne vérifie pas si le téléphone est volé ou bloqué.")


if __name__ == "__main__":
    main()
