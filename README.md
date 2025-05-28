# gui-biljeznica
Jednostavna desktop aplikacija za spremanje i pregledavanje bilješki, izrađena u Pythonu korištenjem Tkinter GUI biblioteke.
OPIS APLIKACIJE
Aplikacija omogućuje korisniku da:

unese tekstualnu bilješku,

spremi bilješku u lokalnu datoteku (biljeske.txt),

pregleda sve prethodno spremljene bilješke.

KAKO RADI

Kada korisnik unese bilješku u polje za unos i klikne "Spremi bilješku", tekst se dodaje na kraj datoteke biljeske.txt.

Klikom na "Prikaži sve bilješke", aplikacija učitava sadržaj datoteke i prikazuje ga u prozoru ispod.

Ako nema spremljenih bilješki ili datoteka ne postoji, korisnik dobiva odgovarajuću poruku.

STRUKTURE KODA

dodaj_biljesku(): Sprema uneseni tekst u datoteku ako polje nije prazno.

otvori_biljeske(): Prikazuje sadržaj datoteke ako postoji.

napravi_gui(): Postavlja i pokreće grafičko sučelje.

POKRETANJE APLIKACIJE

Pokreni Python datoteku:

bash
Kopiraj
Uredi
python ime_datoteke.py
Otvorit će se prozor aplikacije.

DATOTEKE
biljeske.txt: Automatski se stvara kad korisnik spremi prvu bilješku.

.py datoteka: Glavna aplikacija (Tkinter GUI + funkcionalnost).


Idealna je kao osnovni projekt za početnike koji uče rad s GUI-em i datotekama u Pythonu.
