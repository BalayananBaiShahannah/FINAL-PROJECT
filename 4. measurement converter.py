def mm_to_cm(value):
    return value / 10

def cm_to_mm(value):
    return value * 10

def ft_to_m(value):
    return value * 0.3048

def m_to_ft(value):
    return value / 0.3048

def kg_to_lb(value):
    return value * 2.20462

def lb_to_kg(value):
    return value / 2.20462

def km_to_mi(value):
    return value * 0.621371

def mi_to_km(value):
    return value / 0.621371

def l_to_gal(value):
    return value * 0.264172

def gal_to_l(value):
    return value / 0.264172

def display_menu():
    print("\nMeasurement Converter")
    print("1. Millimeters to Centimeters")
    print("2. Centimeters to Millimeters")
    print("3. Feet to Meters")
    print("4. Meters to Feet")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Kilometers to Miles")
    print("8. Miles to Kilometers")
    print("9. Liters to Gallons")
    print("10. Gallons to Liters")
    print("0. Exit")

def get_conversion_choice():
    choice = int(input("\nEnter your choice (0-10): "))
    return choice

def get_value():
    value = float(input("Enter the value to convert: "))
    return value

def main():
    while True:
        display_menu()
        choice = get_conversion_choice()

        if choice == 0:
            print("Exiting the Measurement Converter. Until Next Time!")
            break

        value = get_value()
        
        if choice == 1:
            print(f"{value} mm is {mm_to_cm(value)} cm")
        elif choice == 2:
            print(f"{value} cm is {cm_to_mm(value)} mm")
        elif choice == 3:
            print(f"{value} ft is {ft_to_m(value)} m")
        elif choice == 4:
            print(f"{value} m is {m_to_ft(value)} ft")
        elif choice == 5:
            print(f"{value} kg is {kg_to_lb(value)} lb")
        elif choice == 6:
            print(f"{value} lb is {lb_to_kg(value)} kg")
        elif choice == 7:
            print(f"{value} km is {km_to_mi(value)} mi")
        elif choice == 8:
            print(f"{value} mi is {mi_to_km(value)} km")
        elif choice == 9:
            print(f"{value} l is {l_to_gal(value)} gal")
        elif choice == 10:
            print(f"{value} gal is {gal_to_l(value)} l")
        else:
            print("Invalid choice, please select a number from 0 to 10.")

if __name__ == "__main__":
    main()
