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

#Funkcja, która pozwala na usunięcie istniejącej rezerwacji
def remove_reservation(seats:list):
    try:
        seat_number = int(input("Podaj numer miejsca, którego rezerwację chcesz anulować: "))
    except ValueError:
        print("Wprowadzono nieprawidłową wartość!\n")
        exit()
    if seat_number - 1 < 0 or seat_number - 1 > len(seats):
        print("Wprowadzona wartość nie mieści się w zakresie!\n")
    elif seats[seat_number - 1] == None:
        print("Wybrane miejsce nie zostało wcześniej zarezerwowane!\n")  
    else:
        seats[seat_number - 1] = None
        print("Anulowanie rezerwacji zakończone pomyślnie!\n")

#Funkcja, która pozwala na zmodyfikowanie istniejącej rezerwacji
def modify_reservation(seats:list):
    try:
        seat_number_previous = int(input("Podaj numer miejsca, którego rezerwację chcesz zmodyfikować: "))
    except ValueError:
        print("Wprowadzono nieprawidłową wartość!\n")
        exit()
    if seat_number_previous - 1 < 0 or seat_number_previous > len(seats):
        print("Wprowadzona wartość nie mieści się w zakresie!\n")
        exit()
    elif seats[seat_number_previous - 1] == None:
        print("Wybrane miejsce nie zostało wcześniej zarezerwowane!\n")
        exit()
    else:
        try:
            seat_number_new = int(input("Podaj numer nowego miejsca, na które chcesz przenieść rezerwację: "))
        except ValueError:
            print("Wprowadzono nieprawidłową wartość!\n")
            exit()
        if seat_number_new - 1 < 0 or seat_number_new > len(seats):
            print("Wprowadzona wartość nie mieści się w zakresie!\n")
            exit()
        elif seats[seat_number_new - 1] != None:
            print("Wybrane miejsce jest już zajęte!\n")
            exit()
        else:
            seats[seat_number_new - 1] = seats[seat_number_previous - 1]
            seats[seat_number_previous - 1] = None
            print("Modyfikacja rezerwacji zakończona pomyślnie!\n")

print_seats(seats)
print('\n')
add_reservation(seats)
print('\n')
print_seats(seats)