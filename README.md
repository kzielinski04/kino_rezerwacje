# Dokumentacja do programu rezerwacji miejsc w kinie w Pythonie
## Wprowadzenie
Jest to program stworzony w języku Python, pozwalający na zarządzanie przez użytkownika rezerwacjami miejsc w kinie. Możliwe jest m.in. dodawanie rezerwacji, usuwanie rezerwacji czy przenoszenie rezerwacji.
## Instalacja Pythona
Aby uruchomić ten program, musisz najpierw zainstalować Pythona. Możesz to zrobić w następujący sposób:
### Windows
- Pobierz instalator Pythona ze strony [python.org](https://www.python.org)
- Uruchom instalator i upewnij się, że zaznaczyłeś/zaznaczyłaś opcję "Add Python to PATH"
- Kliknij "Install Now"
### Linux (Debian/Ubuntu)
Wykonaj poniższe instrukcje w terminalu:
```bash
sudo apt update
sudo apt install python3
```
## Tworzenie wirtualnego środowiska
Zalecane jest korzystanie ze środowisk wirtualnych, aby odizolować swoje zależności od globalnych pakietów Pythona.
```bash
python3 -m venv venv
```
## Aktywacja wirtualnego środowiska:
### Windows
```bash
venv/Scripts/activate
```
### Linux
```bash
source venv/bin/activate
```
## Wymagania
- Python 3.12 lub nowszy w wersji 3
## Funkcja `print_seats`
Funkcja `print_seats` pozwala na wyświetlenie aktualnego stanu wszystkich miejsc w kinie, informując, które z nich są wolne, a które są zarezerwowane i przez kogo.
### Przykładowe użycie:
```python
seats = [None, None, "Kacper", "Jan", None, None, "Aleksandra", None, None, "Wioletta"] #Przykładowa lista przechowująca stany miejsc w kinie
print_seats(seats) #Za pomocą funkcji print_seats wyświetlamy stan miejsc w kinie (dla wartości None dane miejsce jest wolne)
```
### Output:
```
Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta
```

## Funkcja `add_reservation`
Funkcja `add_reservation` pozwala na dodanie nowej rezerwacji. Użytkownik podaje swoje imię oraz numer miejsca, które chce zarezerwować. Sprawdzamy czy numer miejsca jest poprawny (czy mieści się w zakresie) oraz czy miejsce jest wolne (czy wartość w liście jest równe None). Jeżeli warunki są spełnione, zapisujemy imię użytkownika w odpowiednim indeksie naszej listy.
### Przykładowe użycie:
```python
print_seats(seats) #Sprawdzamy początkowy stan miejsc z naszej listy za pomocą funkcji print_seats
add_reservation(seats) #Wybieramy odpowiednie miejsce i rezerwujemy je za pomocą funkcji add_reservation
print_seats(seats) #Sprawdzamy stan miejsc po wywołaniu funkcji add_reservation
```
### Output:
```
Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta

Podaj swoje imię: Grzegorz
Podaj numer miejsca, które chcesz zarezerwować (miejsce musi być wolne): 6
Rezerwacja zakończona pomyślnie!

Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest już zarezerwowane przez Grzegorz
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta
```
## Funkcja `remove_reservation`
Funkcja `remove_reservation` pozwala na usunięcie istniejącej już rezerwacji. Użytkownik podaje numer miejsca, które chce zwolnić. Sprawdzamy, czy numer miejsca jest poprawny (czy mieści się w zakresie) i czy miejsce jest zarezerwowane (czy wartość w naszej liście nie jest `None`). Jeśli miejsce jest zarezerwowane, usuwamy rezerwację, ustawiając wartość `None` w odpowiednim indeksie listy.
### Przykładowe użycie:
```python
print_seats(seats) #Sprawdzamy początkowy stan miejsc z naszej listy za pomocą funkcji print_seats
remove_reservation(seats) #Wybieramy odpowiednie miejsce i usuwamy rezerwację za pomocą funkcji remove_reservation
print_seats(seats) #Sprawdzamy stan miejsc po wywołaniu funkcji remove_reservation
```
### Output:
```
Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta

Podaj numer miejsca, którego rezerwację chcesz anulować: 4
Anulowanie rezerwacji zakończone pomyślnie!

Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest wolne
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta
```
## Funkcja `modify_reservation`
Funkcja `modify_reservation` pozwala na modyfikację istniejącej rezerwacji. Użytkownik podaje numer miejsca, które chce zmodyfikować. Sprawdzamy, czy numer miejsca jest poprawny oraz czy miejsce jest zarezerwowane. Następnie użytkownik podaje nowy numer miejsca, na które chce przenieść rezerwację. Sprawdzamy, czy nowy numer miejsca jest poprawny i czy jest wolny. Jeśli warunki są spełnione, przenosimy rezerwację na nowe miejsce, ustawiając odpowiednie wartości w naszej liście miejsc.
### Przykładowe użycie:
```python
print_seats(seats) #Sprawdzamy początkowy stan miejsc z naszej listy za pomocą funkcji print_seats
modify_reservation(seats) #Modyfikujemy rezerwację za pomocą funkcji modify_reservation
print_seats(seats) #Sprawdzamy stan miejsc po wywołaniu funkcji modify_reservation
```
### Output:
```
Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta

Podaj numer miejsca, którego rezerwację chcesz zmodyfikować: 10
Podaj numer nowego miejsca, na które chcesz przenieść rezerwację: 2
Modyfikacja rezerwacji zakończona pomyślnie!

Miejsce nr 1 jest wolne
Miejsce nr 2 jest już zarezerwowane przez Wioletta
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest wolne
```
## Funkcja `check_availability`
Funkcja `check_availability` pozwala na sprawdzenie dostępności wielu miejsc jednocześnie. Użytkownik podaje listę numerów miejsc oddzieloną spacjami, a program sprawdza i informuje, które z nich są wolne, a które są zarezerwowane.
### Przykładowe użycie:
```python
seats = [None, None, "Kacper", "Jan", None, None, "Aleksandra", None, None, "Wioletta"] #Przykładowa lista przechowująca stany miejsc w kinie
check_availability(seats) #Za pomocą funkcji check_availability wyświetlamy stan kilku miejsc
```
### Output:
```
Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta

Podaj numery miejsc, których dostępność chcesz sprawdzić: 1 5 8 10
Miejsce nr 1 jest wolne
Miejsce nr 5 jest wolne
Miejsce nr 8 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta
```
## Funkcja `add_multiple_reservations`
Funkcja `add_multiple_reservations` pozwala na rezerwację wielu miejsc na raz. Użytkownik podaje swoje imię oraz listę numerów miejsc do rezerwacji. Program sprawdza, czy wszystkie podane miejsca są wolne, a jeśli tak, dokonuje rezerwacji.

### Przykładowe użycie:
```python
print_seats(seats) #Sprawdzamy początkowy stan miejsc z naszej listy za pomocą funkcji print_seats
add_multiple_reservations(seats) #Rezerwujemy kilka miejsc za pomocą funkcji add_multiple_reservations
print_seats(seats) #Sprawdzamy stan miejsc po wywołaniu funkcji add_multiple_reservations
```
### Output:
```
Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta

Podaj swoje imię: Roman
Podaj numery miejsc, które chcesz zarezerwować: 5 6 8
Rezerwacja miejsc zakończona pomyślnie!

Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest już zarezerwowane przez Roman
Miejsce nr 6 jest już zarezerwowane przez Roman
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest już zarezerwowane przez Roman
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta
```
## Funkcja `cancel_all_reservations`
Funkcja `cancel_all_reservations` pozwala na anulowanie przez użytkownika wszystkich swoich rezerwacji. Użytkownik podaje swoje imię, a program usuwa wszystkie miejsca zarezerwowane na to imię.
### Przykładowe użycie:
```python
print_seats(seats) #Sprawdzamy początkowy stan miejsc z naszej listy za pomocą funkcji print_seats
add_multiple_reservations(seats) #Zarezerwujmy kilka miejsc za pomocą funkcji add_multiple_reservations
print_seats(seats) #Sprawdzamy stan miejsc po wywołaniu funkcji add_multiple_reservations
cancel_all_reservations(seats) #Anulujemy wszystkie nasze rezerwacje za pomocą funkcji cancel_all_reservations
print_seats(seats) #Sprawdzamy stan miejsc po wywołaniu funkcji cancel all reservations
```
### Output:
```
Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta

Podaj swoje imię: Daria
Podaj numery miejsc, które chcesz zarezerwować: 1 5 6 9
Rezerwacja miejsc zakończona pomyślnie!

Miejsce nr 1 jest już zarezerwowane przez Daria8

Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest już zarezerwowane przez Daria
Miejsce nr 6 jest już zarezerwowane przez Daria
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest już zarezerwowane przez Daria
Miejsce nr 10 jest już zarezerwowane przez Wioletta

Podaj swoje imię: Daria
Anulowanie wszystkich rezerwacji zakończone pomyślnie!

Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta
```
## Funkcja `save_seats_to_file`
Funkcja `save_seats_to_file` pozwala na zapis aktualnego stanu miejsc do pliku.
### Przykład użycia:
```python
seats = [None, None, "Kacper", "Jan", None, None, "Aleksandra", None, None, "Wioletta"] #Przykładowa lista przechowująca stany miejsc w kinie
save_seats_to_file(seats) #Zapisujemy naszą listę miejsc do pliku
```
### Zawartość pliku po wywołaniu funkcji `save_seats_to_file`:
```
None,None,Kacper,Jan,None,None,Aleksandra,None,None,Wioletta
```
## Funkcja `load_seats_from_file`
Funkcja `load_seats_from_file` pozwala na załadowanie do programu stanu miejsc z pliku.
### Przykładowe użycie:
```python
seats = [] #Tworzymy listę, w której będziemy przechowywać stan miejsc
load_seats_from_file(seats) #Importujemy z pliku stan miejsc do listy seats
print_seats(seats) #Sprawdzamy stan miejsc po wywołaniu funkcji load_seats_from_file  
```
### Zawartość pliku przed zaimportowaniem go do programu:
```
None,None,Kacper,Jan,None,None,Aleksandra,None,None,Wioletta
```
### Output:
```
Miejsce nr 1 jest wolne
Miejsce nr 2 jest wolne
Miejsce nr 3 jest już zarezerwowane przez Kacper
Miejsce nr 4 jest już zarezerwowane przez Jan
Miejsce nr 5 jest wolne
Miejsce nr 6 jest wolne
Miejsce nr 7 jest już zarezerwowane przez Aleksandra
Miejsce nr 8 jest wolne
Miejsce nr 9 jest wolne
Miejsce nr 10 jest już zarezerwowane przez Wioletta
```
## Funkcja `menu`
Funkcja `menu` tworzy w konsoli proste menu, które ułatwia użytkownikowi korzystanie z programu. Użytkownik ma do wyboru 8 opcji i w zależności od tego, co wybierze, zostanie wywołana inna funkcja.
### Przykładowe użycie
```python
menu() #Wywołanie funkcji menu utworzy w konsoli proste menu programu
```
### Output:
```
----------------------------------
---------------KINO---------------
----------------------------------
1 - WYŚWIETL STAN REZERWACJI MIEJSC
2 - DODAJ REZERWACJĘ
3 - USUŃ REZERWACJĘ
4 - ZMODYFIKUJ REZERWACJĘ
5 - SPRAWDŹ DOSTĘPNOŚĆ DLA WIELU MIEJSC
6 - ZAREZERWUJ WIELE MIEJSC
7 - ANULUJ WSZYSTKIE SWOJE REZERWACJE
8 - WYJDŹ
----------------------------------
Co chcesz zrobić?:
```