
<h1 align = "center" > SearchEngine </h1>
<h1 align = "center" > O programu </h1>

## Funkcionalnost programa
Prilikom pokretanja programa, korisnik bira direktorijum u kojem ce dalje vrsiti pretrazivanje, odnosno, korisnik vrsi ***pozicioniranje*** na zeljeni direktorijum. Nakon toga se pune strukture podataka ***stablo, graf, set*** na osnovu kojih ce se dalje vrsiti pretraga. Aplikacija je zasnovana na tome da korisnik na osnovu izabranog direktorijuma za pretrazivanje, moze da bira kljucne reci koje trazi i da na osnovu toga dobije rangirane fajlove sa svojim putanjama koje zadovoljavaju zeljenu pretragu.

<br>

<p align="center">

  <img width="800" height="250" src="https://user-images.githubusercontent.com/45834270/75245683-81c0d800-57ce-11ea-8ec5-588286b79bdb.png">

</p>

## Kretanje kroz program
Kretanje kroz program je podeljeno u ***glavni meni*** i ***meni***(jedna grana glavnog menija). U glavom meniju se vrsi izbor kompleksnosti pretrage, odnosno da li korisnik zeli da koristi logicke operatore **'AND', 'OR', 'NOT'** ili zeli da koristi kompleksniju pretragu sa mogucnoscu vise recnog pretrazivanja uz pomoc operatora '**||**' - or, '**&&**' - and, '**!**' - not .
<br>
Nakon izbora pretrage, unosi se pretraga, odnosno vrsimo trazenje zeljenih reci u ***.html*** fajlovima . U meniju nakon zeljene pretrage imamo mogucnost podesavanja parametara prikaza zeljene pretrage ili jednostavnim izborom ***stavke 4*** biramo prikaz po ***default*** parametrima. 
<p align="center">

  <img width="800" height="500" src="https://user-images.githubusercontent.com/45834270/75247148-92bf1880-57d1-11ea-8108-70125aec7aee.png">

</p>

## Requirements
Trenutna verzija ne zahteva nikakvo dodatno instaliranje vise od jedne biblioteke, stoga sve sto je potrebno je instalacija biblioteke [parglare](https://github.com/igordejanovic/parglare) i program se dalje pokrece modula **'pokretac.py'**
```sh
$ pip install parglare
```



## Ideje za sledece verzije
  - Graficko korisnicki interfejs, u kome se interakcija sa korisnikom vrsi preko GUI-a
  - ...

<h1 align = "center" > Ispod haube </h1>

## Uvod
  - **Trie** ~ struktura koja cuva parsirane reci iz svih fajlova unetog direktorijuma i na kraju reci( u listu stabla) cuva i stranice koje imaju tu rec. ( vise o [stablu](https://www.geeksforgeeks.org/trie-insert-and-search/))
  - **Graph** ~ struktura u kojoj se cuvaju veze izmedju stranica, odnosno koja stranica pokazuje na koju stranicu, i na koju stranicu pokazuju koje stranice, kako bi posle mogli vrsiti delotvornije rangiranje. ( vise o [grafu](https://www.tutorialspoint.com/python_data_structure/python_graphs.htm))
  - **Set** ~ struktura podataka u kojem se cuvamo stranice odredjene reci, a kasnije koristimo kako bi vrsili **uniju, presek, komplement** nad setom pretrazivane reci. ( vise o [setu](https://www.geeksforgeeks.org/internal-working-of-set-in-python/))
## Osnovna pretraga

Osnovna pretraga se vrsi tako sto u zavisnosti od unetog logickog operatora vrsimo odredjene operacije nad ***setovima*** unetih reci. Odnosno, uneti string je dekomponovan na vise reci, i za svaku rec imamo set odnosno skup stranica u kojem se ta rec pojavljuje, nakon toga vrsimo operacije nad setovima ( ***unija, presek, komplement*** ) i dobijamo rezultujuci set stranica koje predstavljaju rezultat pretrage.

## Kompleksna pretraga
Kao i osnovna pretraga, samo sto sada koristimo biblioteku [parglare](https://github.com/igordejanovic/parglare) . Potrebno je bilo napraviti IR (intermediate representation) u obliku Python klasa. Gde su prilikom redukcije, parglare akcije zadužene za instanciranje klasa IR-a i izgradnju stabla parsiranja. A nakon toga se vrsi evaluiranje stabla parsiranja.
<br>
<br>
Primeri na osnovu koga funkcionise nasa kompleksna pretraga : [primer kalkulatora](https://github.com/igordejanovic/parglare/blob/master/examples/calc/calc.py) i po ugledu na gramatiku za +,-,*,/
```sh
 E -> E + T | E - T | T
 T -> T * F | T / F | F
 F -> F ^ X | B
 B -> i | (E)
 X -> i | (E)
```
<br>

Pravimo nasu gramatiku:

```sh
E: E "||" T
   | T
   ;

T : T "&&" F
  | F
  ;

F : "!" X
  | X
  ;

X: reci
  | "(" E ")"
  ;
```

## Rangiranje rezultata pretrage
Rangiranje rezultata pretrage se vrši tako što imamo više faktora koji utiču na rang, najbitnije stavke su:
  - broj linkova iz drugih stranica na pronađenu stranicu
  - broj pojavljivanja traženih reči na stranici
  - broj traženih reči u stranicama koje sadrže link na traženu stranicu

Težine ovih faktora su skalirane, tj. broj traženih reči na stranici nema isti uticaj na rangiranje kao broj linkova iz drugih stranica na pronađenu stranicu.
Konkretno najveci uticaj na rangiranje imaju "beklinkovi" tj broj linkova iz drugih stranica na pronađenu stranicu.

![image](https://user-images.githubusercontent.com/49925421/75282639-adb17d00-5811-11ea-8fd8-30e2bad27a2e.png)

Formula po kojoj se odredjuje broj bodova za rangiranje izgleda ovako: 
  rang = (beklinkovi * 1) + (brojPojavljivanjaTrazenihReciNaTojStranici * 0.7) + (brojponavljanjatrazenihReciNaStranicamaKojeLinkuju * 0.4)
  
Iz formule jasno vidimo da najveci uticaj na rang imaju beklinkovi, zatim broj pojavljivanja traženih reči na stranici i na kraju 
najmanji uticaj ima broj traženih reči u stranicama koje sadrže link na traženu stranicu, baš iz tog razloga imamo mnozenje tj skaliranje tog faktora sa 0.4. Na osnovu izracunatuh bodova tj ranga svake stranice vršimo paginaciju rezultata, osim putanja stranica prikazujemo korisniku i bodove rangiranja.

![image](https://user-images.githubusercontent.com/49925421/75283804-cde23b80-5813-11ea-84fe-0e8d91e9a1cd.png)
