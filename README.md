# Basketball player tracking

## Opis okruženja potrebnog za build
 Za izgradnju projekta potrebno je sledeće okruženje: 
 - **Python** (preporučena verzija: Python 3.12.0) 
 - **Pip** (Python paket menadžer) 
 ## Postavljanje projekta  
 1. Klonirajte repozitorijum na lokalni računar: 
 **```bash git clone [url do repozitorijuma] ```** 
2. Instalirajte neophodnih zavisnosti koristeći pip:
	 **```pip install "fastapi" ```**
	 **```pip install "uvicorn[standard]"```** 
	 **```pip install pydantic ```**

## Postavljanje željenog .csv fajla

 - U folderu **../basketball-player-tracking/data** je zamišljeno da se
   postavi csv fajl iz kog će biti učitani podaci 
 - U fajlu **config.ini** pozicioniranom u **../basketball-player-tracking** direkotrijumu
   postavlja se odgovarajuća putanja do csv fajla iz kog se učitavaju
   podaci. (primer: data/input_file_1.csv)

## Primer kako se aplikacija pokreće 
Pozicionirajte se u **../basketball-player-tracking** direkotrijumu (u njemu se nalazi main.py) i pokrenite uvicorn server iz terminala:
**```uvicorn main:app --host 0.0.0.0 --port 8000```**

*(ukolite želite pokrenuti aplikaciju pomoću nekog IDE-a potrebno je proveriti da sadrži sve potrebne zavisnosti)*

## Primer kako se testovi pokreću
Pozicionirajte se u **../basketball-player-tracking** direktorijumu i pokrenite testove iz terminala koristeći komandu:
**```python -m tests.test_suite```**

*(ukolite želite pokrenuti testove pomoću nekog IDE-a potrebno je proveriti da sadrži sve potrebne zavisnosti)*

## Korišćene tehnologije
Ova aplikacija koristi sledeće tehnologije:

 - **Python**: Programski jezik u kom je implementiran celokupan direkotrijum.
 - **FastAPI**: Moderan web framework za izradu API-ja sa brzim izvršavanjem u Pythonu.
 - **Uvicorn**: ASGI server koji se koristi za pokretanje FastAPI aplikacije
 - **Pydantic**: Biblioteka za validaciju podataka i deklarativno definisanje podatkovnih modela.
 - **Unittest**: Ugrađeni Python okvir za pisanje i izvršavanje testova.
 - **ConfigParser**: Python modul za parsiranje konfiguracionih fajlova.