
venituri=[]
cheltuieli=[]

def adauga_venit():
    suma=float(input("Introduceti venitul: "))
    venituri.append(suma)

def adauga_cheltuieli():
    suma=float(input("Introduceti cheltuieli: "))
    cheltuieli.append(suma)

def calcul_sold():
    sold=sum(venituri)-sum(cheltuieli)
    return sold

adauga_venit()
adauga_cheltuieli()

print("Soldul final este de",calcul_sold(),"lei")