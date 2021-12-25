from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(gibson)
    print(f"{gibson.name} get_age() - Expected {gibson.get_age()}. Got {gibson.get_age()}")
    print(f"{gibson.name} get_age() - Expected {gibson.is_vintage()}. Got {gibson.is_vintage()}")
    another_guitar = Guitar("Another Guitar", 2013, 500)
    print(f"{another_guitar.name} get_age() - Expected {another_guitar.get_age()}. Got {another_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {another_guitar.is_vintage()}. Got {another_guitar.is_vintage()}")

main()
