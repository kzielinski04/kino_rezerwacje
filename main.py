seats = [None, None, "Kacper", "Jan", None, None, "Aleksandra", None, None, "Wioletta"] #Przykładowa lista do sprawdzania, czy dana funkcja działa prawidłowo
#Funkcja, która pozwala na wyświetlenie aktualnego stanu rezerwacji miejsc
def print_seats(seats:list):
    for i in range(len(seats)):
        if seats[i] == None:
            print(f"Miejsce nr {i + 1} jest wolne")
        else:
            print(f"Miejsce nr {i + 1} jest już zarezerwowane przez {seats[i]}")
print_seats(seats)