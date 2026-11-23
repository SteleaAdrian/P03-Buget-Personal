from logica import adauga_tranzactie
from logica import calculeaza_sold
from logica import filtreaza_cheltuieli
from logica import calculeaza_medie_lunara
from stocare import incarca_tranzactii
from stocare import salveaza_tranzactii


def main():
    tranzactii = incarca_tranzactii()

    if len(tranzactii) == 0:
        adauga_tranzactie(tranzactii, "venit", 2000, "Salariu", 10, 2026)
        adauga_tranzactie(tranzactii, "cheltuiala", 800, "Chirie", 10, 2026)
        adauga_tranzactie(tranzactii, "cheltuiala", 400, "Transport", 10, 2026)
        adauga_tranzactie(tranzactii, "cheltuiala", 600, "Transport", 11, 2026)
        salveaza_tranzactii(tranzactii)

    sold = calculeaza_sold(tranzactii)
    print("Sold total:", sold, "lei")

    lista_transport, sold_transport = filtreaza_cheltuieli(tranzactii, "Transport", 0, 0)
    print("Cheltuieli Transport:", lista_transport)
    print("Sold Transport:", sold_transport, "lei")

    medie = calculeaza_medie_lunara(tranzactii)
    print("Media lunară a cheltuielilor:", medie, "lei")

    try:
        adauga_tranzactie(tranzactii, "cheltuiala", -100, "Mancare", 11, 2026)
    except ValueError as eroare:
        print("Eroare prinsă corect:", eroare)


if __name__ == "__main__":
    main()