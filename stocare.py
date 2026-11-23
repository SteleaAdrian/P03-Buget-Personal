import json
import os

NUME_FISIER = "tranzactii.json"


def incarca_tranzactii():
    if os.path.exists(NUME_FISIER) == False:
        return []

    fisier = open(NUME_FISIER, "r", encoding="utf-8")
    date = json.load(fisier)
    fisier.close()
    return date


def salveaza_tranzactii(tranzactii):
    fisier = open(NUME_FISIER, "w", encoding="utf-8")
    json.dump(tranzactii, fisier, indent=4)
    fisier.close()