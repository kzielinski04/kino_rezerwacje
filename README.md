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