import math
"""
Funkcija koja rounduje uvek na vecu cifru.
"""
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

"""
Funkcija koja vrsi ispis jedne stranice.
"""
def ispisiStranicu(tekucaStranica,brPrikaza,setPod):
    print("\t\t\t\t\t ------------------------------------------------------------------------------------- stranica " + str(tekucaStranica) + " --------------------------------------------------------------------------------------")
    print("\n")
    for i in range(brPrikaza):
        j = (brPrikaza) * (int(tekucaStranica) - 1) + i
        if j < len(setPod.elements):
            print("\t\t\t\t\t  " + setPod.elements[j] + " pojavljivanja reci: " + str(setPod.brPojavljivanjaReci[j]))
        else:
            break

    print("\n")
    print("\t\t\t\t\t ------------------------------------------------------------------------------------- stranica " + str(tekucaStranica) + " --------------------------------------------------------------------------------------")


"""
Funkcija koja vrsi paginaciju.
"""
def paginacija(setPod):
    # Default vrednosti broja entiteta na stranici i broja stranica
    brPrikaza = 5
    ukupnoStranica = round_up(len(setPod) / brPrikaza)
    stranicaN = 1               # promenljiva koja cuva koliko stranica prikazujemo
    tekucaStranica = 1

    meniUnos=''
    while meniUnos != 'x':
        print("\n\n")
        print("\t\t\t\t\t ---------------------------------- MENI ----------------------------------")
        print("\t\t\t\t\t Parametri - tekucaStranica: " +str(tekucaStranica)+ " , brojEntitetaPoStrani: " + str(brPrikaza) + " , N: "+str(stranicaN))
        print("\t\t\t\t\t N - broj stranica za prikaz, pomeranje")
        print("\t\t\t\t\t --------------------------------------------------------------------------")
        print("\t\t\t\t\t Unesite jednu od sledecih ponudjenih stavki.")
        print("\t\t\t\t\t 1 - Podesavanje  parametara.")
        print("\t\t\t\t\t 2 - Pomeri N stranica unapred.")
        print("\t\t\t\t\t 3 - Pomeri N stranica unazad.")
        print("\t\t\t\t\t 4 - Prikazi od trenutno pozicionirane stranice.")
        print("\t\t\t\t\t x - Kraj.")
        print("\t\t\t\t\t --------------------------------------------------------------------------")
        meniUnos = input()
        if meniUnos == str(1):

            unos2 = ''
            while unos2 == '':
                print("Unesite koliko entiteta zelite prikazati na jednoj stranici[1-" + str(len(setPod)) + "]: ")
                unos2 = input()
                if int(unos2) < 1 or int(unos2) > len(setPod):
                    print("Error: Molim vas da unesete validan broj entiteta po stranici.")
                    unos2 = ''

            brPrikaza = int(unos2)
            ukupnoStranica = round_up(len(setPod) / brPrikaza)

            unos = ''
            while unos == '':
                print("Pozicionirajte se odnosno unesite broj stranice koju zelite prikazati[1-" + str(ukupnoStranica) + "]: ")
                unos = input()
                if int(unos) < 1 or int(unos) > ukupnoStranica:
                    print("Error: Ta stranica nije u opticaju.")
                    unos = ''
            tekucaStranica = int(unos)

            unosN = ''
            while unosN == '':
                print("Unesite N[1-"+str(ukupnoStranica)+"]")
                unosN = input()
                if int(unosN) < 1 or int(unosN) > int(ukupnoStranica):
                    print("Error: Izabrano N nije u opsegu validnih vrednosti N-a")
                    unosN =''
                else:
                    stranicaN=int(unosN)

        elif meniUnos == str(2):
            tekucaStranica += stranicaN
            if tekucaStranica > ukupnoStranica:
                tekucaStranica -= stranicaN
                print("Error: Nije moguce ovoliko pomeranje napred")

        elif meniUnos == str(3):
            tekucaStranica -= stranicaN
            if tekucaStranica < 1:
                tekucaStranica += stranicaN
                print("Error: Nije moguce ovoliko pomeranje nazad")

        elif meniUnos == str(4):
            print("\t\t\t\t\t --------------------------------------------------------------------------------- REZULTAT PRETRAGE -----------------------------------------------------------------------------------")
            for i in range(stranicaN):
                brStrane = tekucaStranica + i
                if brStrane <= ukupnoStranica:
                    ispisiStranicu(brStrane,brPrikaza,setPod)
            print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



