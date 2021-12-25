from guitar import Guitar


def main():
    guitar_list = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

    print("My guitars")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitar_list.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print(f"{guitar_name} ({guitar_year}) : ${guitar_cost} added.")
        guitar_name = input("Name: ")

    print("* * * snip * * *")

    print("These are my guitars: ")
    for i, guitar in enumerate(guitar_list):
        if guitar.is_vintage():
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:>10.2f} (vintage)")
        else:
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:>10.2f}")

main()