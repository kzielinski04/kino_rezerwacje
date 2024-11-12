seats = [None, None, "Kacper", "Jan", None, None, "Aleksandra", None, None, "Wioletta"] #Przykładowa lista do sprawdzania, czy dana funkcja działa prawidłowo

#Funkcja, która pozwala na wyświetlenie aktualnego stanu rezerwacji miejsc
def print_seats(seats:list):
    for i in range(len(seats)):
        if seats[i] == None:
            print(f"Miejsce nr {i + 1} jest wolne")
        else:
            print(f"Miejsce nr {i + 1} jest już zarezerwowane przez {seats[i]}")

#Funkcja, która pozwala na dodanie nowej rezerwacji
def add_reservation(seats:list):
    name = input("Podaj swoje imię: ")
    try:
        seat_number = int(input("Podaj numer miejsca, które chcesz zarezerwować (miejsce musi być wolne): "))
    except ValueError:
        print("Wprowadzono nieprawidłową wartość!")
        exit()
    if seat_number - 1 < 0 or seat_number - 1 > len(seats):
        print("Wprowadzono nieprawidłową wartość!")
        exit()
    elif seats[seat_number - 1] != None:
        print("Wybrane miejsce jest już zajęte!")
        exit()
    else:
        seats[seat_number - 1] = name
        print("Rezerwacja zakończona pomyślnie!")
print_seats(seats)
print('\n')
add_reservation(seats)
print('\n')
print_seats(seats)