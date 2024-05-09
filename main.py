import modul

def main():
    # Inicialitzem la puntuació
    puntuacio = 0

    # Executem les funcions de modul.py amb diferents casos de prova i comparem resultats
    result_exercici1 = modul.exercici1()
    expected_exercici1 = "Modul fet" # Aquí posarem el resultat esperat per a l'exercici 
    if result_exercici1 == expected_exercici1:
        puntuacio += 1

    result_exercici2 = modul.salut()
    expected_salut = "Hola, món!" 
    if result_exercici2 == expected_salut:
        puntuacio += 1

    result_exercici3_1 = modul.suma(3, 4)
    expected_suma1 = 7
    if result_exercici3_1 == expected_suma1:
        puntuacio += 1
    result_exercici3_2 = modul.suma(12, 8)
    expected_suma2 = 20
    if result_exercici3_2 == expected_suma2:
        puntuacio += 1
    
    result_exercici4_1 = modul.multiplica(8,5,2)
    expected_multiplica1 = 80
    if result_exercici4_1 == expected_multiplica1:
        puntuacio += 1
    result_exercici4_2 = modul.multiplica(9,2,6)
    expected_multiplica2 = 108
    if result_exercici4_2 == expected_multiplica2:
        puntuacio += 1

    result_exercici5_1 = modul.informacio_persona("Alex", 24, "Barcelona")
    expected_informacio_persona1 = "Nom: Alex, Edat: 24, Ciutat: Barcelona"
    if result_exercici5_1 == expected_informacio_persona1:
        puntuacio += 1
    result_exercici5_2 = modul.informacio_persona("Juan", 30, "Valencia")
    expected_informacio_persona2 = "Nom: Juan, Edat: 30, Ciutat: Valencia"
    if result_exercici5_2 == expected_informacio_persona2:
        puntuacio += 1

    result_exercici6 = modul.suma_llista([3,8,0,4])
    expected_suma_llista = 15
    if result_exercici6 == expected_suma_llista:
        puntuacio += 1

    result_exercici7 = modul.nota(8, 10)
    expected_nota = 8
    if result_exercici7 == expected_nota:
        puntuacio += 1
   
    result_exercici16_1 = modul.exercici16(4,12)
    expected_exercici16_1 = "Aquesta funció està implementada amb dos paràmetres 4, i 12. S'ha cridat a la funció amb dos arguments: 4, 12"
    print(modul.exercici16(4,12))
    if result_exercici16_1 == expected_exercici16_1:
        puntuacio += 1
    result_exercici16_2 = modul.exercici16("castell",5)
    expected_exercici16_2 = "Aquesta funció està implementada amb dos paràmetres castell i 5. S'ha cridat a la funció amb dos arguments: castell, 5"
    print(modul.exercici16("castell",5))
    if result_exercici16_2 == expected_exercici16_2:
        puntuacio += 1

    result_exercici17_1 = modul.informacio_persona_2("Maria",20,"Madrid")
    expected_informacio_persona2_1 = "Nom: Maria, Edat: 20, Ciutat: Madrid"
    if result_exercici17_1 == expected_informacio_persona2_1:
        puntuacio += 1
    result_exercici17_2 = modul.informacio_persona_2("Maria",20)
    expected_informacio_persona2_2 = "Nom: Maria, Edat: 20, Ciutat: Barcelona"
    if result_exercici17_2 == expected_informacio_persona2_2:
        puntuacio += 1

    result_exercici18_1 = modul.pesca(4)
    expected_pesca_1 = "48"
    result_exercici18_2 = modul.pesca(12,"molt_profund")
    expected_pesca_2 = "516"
    result_exercici18_3 = modul.pesca(37,"rentadora")
    expected_pesca_3 = "Profunditat no vàlida"
    print(modul.pesca(4), modul.pesca(12,"molt profund"), modul.pesca(37,"rentadora"))
    if result_exercici18_1 == expected_pesca_1 and result_exercici18_2 == expected_pesca_2 and result_exercici18_3 == expected_pesca_3:
        puntuacio += 1
    

    result_exercici19_1 = modul.qualificacio("Pedro Perez",7)
    expected_qualificacio_1 = {'alumne': 'Pedro Perez', 'nota': 7, 'aprovat': True}
    result_exercici19_2 = modul.qualificacio("Juan García",3)
    expected_qualificacio_2 = {'alumne': 'Juan García', 'nota': 3, 'aprovat': False}
    result_exercici19_3 = modul.qualificacio("Ivan Sanchez",4)
    expected_qualificacio_3 = {'alumne': 'Ivan Sanchez', 'nota': 4, 'aprovat': False}
    result_exercici19_4 = modul.qualificacio("Maria Unpajote",4,True)
    expected_qualificacio_4 = {'alumne': 'Maria Unpajote', 'nota': 4, 'aprovat': True}
    if result_exercici19_1 == expected_qualificacio_1 and result_exercici19_2 == expected_qualificacio_2 and result_exercici19_3 == expected_qualificacio_3 and result_exercici19_4 == expected_qualificacio_4:
        puntuacio += 1

    result_exercici20_1 = modul.informacio_persona_3("Maria", 30)
    expected_informacio_persona_3_1 = {'Nom': 'Maria', 'Edat': 30, 'Ciutat': 'Barcelona'}
    result_exercici20_2 = modul.informacio_persona_3("Juan", 25, ocupacio="Enginyer", idioma="Català", casat=True)
    expected_informacio_persona_3_2 = {'Nom': 'Juan', 'Edat': 25, 'Ciutat': 'Barcelona', 'ocupacio': 'Enginyer', 'idioma': 'Català', 'casat': True}
    if result_exercici20_1 == expected_informacio_persona_3_1 and result_exercici20_2 == expected_informacio_persona_3_2:
        puntuacio += 1
     

    result_exercici22 = modul.exercici22()
    expected_exercici22 = "1"
    if result_exercici22 == expected_exercici22:
        puntuacio += 1

    result_exercici23 = modul.exercici23()
    expected_exercici23 = "1"
    if result_exercici23 == expected_exercici23:
        puntuacio += 1

    result_exercici24 = modul.exercici24()
    expected_exercici24 = "1"
    if result_exercici24 == expected_exercici24:
        puntuacio += 1

    # Mostra la puntuació final i converteix-la a una nota del 1 al 10
    total_problemes = 18 #Hay algunos que he "quitado", como calcular la nota (justo debajo), o los de llamar las funciones (he hecho el 8 y el 2 en 1, por ejemplo) 
    nota = (puntuacio / total_problemes) * 10
    print(f"Problemes resolts correctament: {puntuacio} de {total_problemes}")
    print(f"Nota: {nota}")

if __name__ == "__main__":
    main()
