#Funkcja, która pozwala na wyświetlenie aktualnego stanu rezerwacji miejsc
def print_seats(seats:list):
    for i in range(len(seats)):
        if seats[i] == None:
            print(f"Miejsce nr {i + 1} jest wolne")
        else:
            print(f"Miejsce nr {i + 1} jest już zarezerwowane przez {seats[i]}")
    print('\n')

#Funkcja, która pozwala na dodanie nowej rezerwacji
def add_reservation(seats:list):
    name = input("Podaj swoje imię: ")
    try:
        seat_number = int(input("Podaj numer miejsca, które chcesz zarezerwować (miejsce musi być wolne): "))
    except ValueError:
        print("Wprowadzono nieprawidłową wartość!\n")
        exit()
    if seat_number - 1 < 0 or seat_number - 1 > len(seats):
        print("Wprowadzono nieprawidłową wartość!\n")
        exit()
    elif seats[seat_number - 1] != None:
        print("Wybrane miejsce jest już zajęte!\n")
        exit()
    else:
        seats[seat_number - 1] = name
        print("Rezerwacja zakończona pomyślnie!\n")

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
        if seat_number_new - 1 < 0 or seat_number_new > len(seats):
            print("Wprowadzona wartość nie mieści się w zakresie!\n")
        elif seats[seat_number_new - 1] != None:
            print("Wybrane miejsce jest już zajęte!\n")
        else:
            seats[seat_number_new - 1] = seats[seat_number_previous - 1]
            seats[seat_number_previous - 1] = None
            print("Modyfikacja rezerwacji zakończona pomyślnie!\n")

#Funkcja, która pozwala na sprawdzenie dostępności wielu miejsc
def check_availability(seats:list[int]):
    seats_numbers = []
    seats_numbers = input("Podaj numery miejsc, których dostępność chcesz sprawdzić: ").split()
    for i in range(len(seats_numbers)):
        seats_numbers[i] = int(seats_numbers[i])
        seats_numbers[i] -= 1
    for j in seats_numbers:
        if seats[j] == None:
            print(f"Miejsce nr {j + 1} jest wolne")
        else:
            print(f"Miejsce nr {j + 1} jest już zarezerwowane przez {seats[j]}")
    print('\n')

#Funkcja, która pozwala na rezerwację wielu miejsc na raz
def add_multiple_reservations(seats:list):
    name = input("Podaj swoje imię: ")
    seats_numbers = []
    seats_numbers = input("Podaj numery miejsc, które chcesz zarezerwować: ").split()
    for i in range(len(seats_numbers)):
        if seats_numbers[i].isnumeric() == False:
            print("Wprowadzono nieprawidłową wartość!\n")
            exit()
        seats_numbers[i] = int(seats_numbers[i])
    for j in range(len(seats_numbers)):
        if seats_numbers[j] < 1 or seats_numbers[j] > len(seats):
            print("Wprowadzono wartość, która nie mieści się w zakresie!\n")
            exit()
    for k in seats_numbers:
        if seats[k - 1] != None:
            print("Wybrano miejsce, które jest już zajęte!\n")
            exit()
        seats[k - 1] = name
    print("Rezerwacja miejsc zakończona pomyślnie!\n")

#Funkcja, która pozwala na anulowanie wszystkich rezerwacji
def cancel_all_reservations(seats:list):
    name = input("Podaj swoje imię: ")
    for i in range(len(seats)):
        if seats[i] == name:
            seats[i] = None
    print("Anulowanie wszystkich rezerwacji zakończone pomyślnie!\n")

#Funkcja, która zapisuje stan miejsc do pliku
def save_seats_to_file(seats:list):
    file = open("kino.csv", "w")
    for i in range(len(seats)):
        if i == len(seats) - 1:
            file.write(str(seats[i]))
        else:
            file.write(str(seats[i]) + ',')
    print(seats[len(seats) - 1])
    file.close()

#Funkcja, która odczytuje stan miejsc z pliku
def load_seats_from_file(seats:list):
    file = open("kino.csv", "r")
    content = file.read().split(',')
    for i in content:
        seats.append(i)
    file.close()
    for j in range(len(seats)):
        if seats[j] == "None":
            seats[j] = None

#Proste menu
def menu():
    seats = []
    load_seats_from_file(seats)
    while True:
        print("1 - WYŚWIETL STAN REZERWACJI MIEJSC")
        print("2 - DODAJ REZERWACJĘ")
        print("3 - USUŃ REZERWACJĘ")
        print("4 - ZMODYFIKUJ REZERWACJĘ")
        print("5 - SPRAWDŹ DOSTĘPNOŚĆ DLA WIELU MIEJSC")
        print("6 - ZAREZERWUJ WIELE MIEJSC")
        print("7 - ANULUJ WSZYSTKIE SWOJE REZERWACJE")
        print("8 - WYJDŹ")
        print("-----------------------------------")
        try:
            choice = int(input("Co chcesz zrobić?: "))        
        except ValueError:
            print("Wprowadzona wartość jest nieprawidłowa!")
        match choice:
            case 1:
                print_seats(seats)
            case 2:
                add_reservation(seats)
            case 3:
                remove_reservation(seats)
            case 4:
                modify_reservation(seats)
            case 5:
                check_availability(seats)
            case 6:
                add_multiple_reservations(seats)
            case 7:
                cancel_all_reservations(seats)
            case 8:
                save_seats_to_file(seats)
                exit()

#menu()
seats = [] #Tworzymy listę, w której będziemy przechowywać stan miejsc
print_seats(seats) #Sprawdzamy początkowy stan miejsc z naszej listy za pomocą funkcji print_seats
load_seats_from_file(seats) #Importujemy z pliku stan miejsc do listy seats
print_seats(seats) 