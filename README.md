# Dokumentacja do programu rezerwacji miejsc w kinie w Pythonie
## Wprowadzenie
Jest to program stworzony w języku Python, pozwalający na zarządzanie przez użytkownika rezerwacjami miejsc w kinie. Możliwe jest m.in. dodawanie rezerwacji, usuwanie rezerwacji czy przenoszenie rezerwacji.
## Funkcja `print_seats`
Funkcja `print_seats` pozwala na wyświetlenie aktualnego stanu wszystkich miejsc w kinie, informując, które z nich są wolne, a które są zarezerwowane i przez kogo.
### Przykładowe użycie:
```python
seats = [None, None, "Kacper", "Jan", None, None, "Aleksandra", None, None, "Wioletta"] #Przykładowa lista przechowująca stan miejsc w kinie
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
print('\n') #Dla lepszej czytelności przechodzimy do nowej linii
add_reservation(seats) #Wybieramy odpowiednie miejsce i rezerwujemy je za pomocą funkcji add_reservation
print('\n') #Ponownie przechodzimy do nowej linii dla lepszej czytelności
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
print('\n') #Dla lepszej czytelności przechodzimy do nowej linii
remove_reservation(seats) #Wybieramy odpowiednie miejsce i usuwamy rezerwację za pomocą funkcji remove_reservation
print('\n') #Ponownie przechodzimy do nowej linii dla lepszej czytelności
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
print('\n') #Dla lepszej czytelności przechodzimy do nowej linii
modify_reservation(seats) #Modyfikujemy rezerwację za pomocą funkcji modify_reservation
print('\n') #Ponownie przechodzimy do nowej linii dla lepszej czytelności
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