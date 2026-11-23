def adauga_tranzactie(tranzactii, tip, suma, categorie, luna, an):
    tip = tip.strip().lower()
    if tip != "venit" and tip != "cheltuiala":
        raise ValueError("Tipul trebuie să fie 'venit' sau 'cheltuiala'.")

    suma = float(suma)
    if suma <= 0:
        raise ValueError("Suma trebuie să fie mai mare decât 0.")

    categorie = categorie.strip()
    if categorie == "":
        raise ValueError("Categoria nu poate fi goală.")

    luna = int(luna)
    an = int(an)
    if luna < 1 or luna > 12:
        raise ValueError("Luna trebuie să fie între 1 și 12.")

    id_maxim = 0
    for t in tranzactii:
        if t["id"] > id_maxim:
            id_maxim = t["id"]

    tranzactie_noua = {
        "id": id_maxim + 1,
        "tip": tip,
        "suma": suma,
        "categorie": categorie,
        "luna": luna,
        "an": an
    }

    tranzactii.append(tranzactie_noua)
    return tranzactie_noua


def calculeaza_sold(tranzactii):
    total_venituri = 0.0
    total_cheltuieli = 0.0

    for t in tranzactii:
        if t["tip"] == "venit":
            total_venituri = total_venituri + t["suma"]
        else:
            total_cheltuieli = total_cheltuieli + t["suma"]

    sold = total_venituri - total_cheltuieli
    return sold


def filtreaza_cheltuieli(tranzactii, categorie, luna, an):
    rezultat = []

    for t in tranzactii:
        if t["tip"] == "cheltuiala":
            potrivire_categorie = True
            potrivire_luna = True
            potrivire_an = True

            if categorie != "" and t["categorie"].lower() != categorie.lower():
                potrivire_categorie = False

            if luna != 0 and t["luna"] != luna:
                potrivire_luna = False

            if an != 0 and t["an"] != an:
                potrivire_an = False

            if potrivire_categorie == True and potrivire_luna == True and potrivire_an == True:
                rezultat.append(t)

    sold_filtrat = calculeaza_sold(rezultat)
    return rezultat, sold_filtrat


def calculeaza_medie_lunara(tranzactii):
    luni_unice = []
    total_cheltuieli = 0.0

    for t in tranzactii:
        if t["tip"] == "cheltuiala":
            total_cheltuieli = total_cheltuieli + t["suma"]
            luna_an = str(t["luna"]) + "/" + str(t["an"])

            if luna_an not in luni_unice:
                luni_unice.append(luna_an)

    if len(luni_unice) == 0:
        return 0.0

    medie = total_cheltuieli / len(luni_unice)
    return medie