def exercici1():
    return("Modul fet")

def salut():
    return("Hola, món!")

def suma(a, b):
    return a + b

def multiplica(*args):
    if len(args) < 2:
        return None
    producte = 1
    for num in args:
        producte *= num
    return producte

def informacio_persona(nom,edat,ciutat):
    return f"Nom: {nom}, Edat: {edat}, Ciutat: {ciutat}"

def suma_llista(llista):
    return sum(llista)

def nota(puntuacio, total_problemes):
    return (puntuacio / total_problemes) * 10

def exercici16(parametre1, parametre2):
    return f"Aquesta funció està implementada amb dos paràmetres {parametre1}, i {parametre2}." f" S'ha cridat a la funció amb dos arguments: {parametre1}, {parametre2}"
def informacio_persona_2(nom, edat, ciutat="Barcelona"):
    return f"Nom: {nom}, Edat: {edat}, Ciutat: {ciutat}"

def pesca(num_peixos, profunditat="profund"):
    relacio_profunditat_pes = {"poc_profund": 1, "profund": 12, "molt_profund": 43}

    if profunditat in relacio_profunditat_pes:
        pes_per_peix = relacio_profunditat_pes[profunditat]
        kilos_total = num_peixos * pes_per_peix
        return kilos_total
    else:
        return "Profunditat no vàlida"

def qualificacio(nom_alumne, nota, aprovat_si_no_arriba=False):
    if nota >= 5:
        aprovat = True
    elif 4 <= nota < 5:
        aprovat = aprovat_si_no_arriba
    else:
        aprovat = False

    if aprovat:
        print(f"La nota de {nom_alumne} és {nota}. {nom_alumne} ha aprovat.")
    else:
        print(f"La nota de {nom_alumne} és {nota}. {nom_alumne} no ha aprovat.")

    return {"alumne": nom_alumne, "nota": nota, "aprovat": aprovat}

def informacio_persona_3(nom, edat, ciutat="Barcelona", **altres_valors):
    informacio = {"Nom": nom, "Edat": edat, "Ciutat": ciutat}
    informacio.update(altres_valors)
    return informacio

def exercici21():
    pass

def exercici22():
    pass

def exercici23():
    pass

def exercici24():
    pass

