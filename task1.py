# # Завдання: [1.5 points]

# ### Опис:
# Напишіть програму, яка дозволяє працювати зі списком автомобілів у гаражі. Програма повинна працювати в інтерактивному режимі та обробляти наступні команди:

# - **`add <license_plate> <make> <year>`** — додати автомобіль до гаража.  
#   Якщо автомобіль із таким номером (`license_plate`) вже існує, його марка (`make`) та рік випуску (`year`) мають бути оновлені.
#   - `license_plate` — номерний знак автомобіля (рядок).
#   - `make` — марка автомобіля (рядок).
#   - `year` — рік випуску (ціле число).

# - **`view <license_plate>`** — переглянути інформацію про автомобіль із заданим номерним знаком.
# > **Note:** Use argparser here.
# #### Приклад:

# ```plaintext
# > add "AB123CD" "Toyota" 2015  
# > add "XY987ZT" "Honda" 2018  
# > add "AB123CD" "Mazda" 2020  
# > view "AB123CD"  
# < Mazda (2020)
# ```




garage = {}

def add_car(license_plate, make, year):
    garage[license_plate] = {"make": make, "year": year}
    print(f"Автомобіль {license_plate} було додано або оновлено.")

def view_car(license_plate):
    car = garage.get(license_plate)
    if car:
        print(f"{car['make']} ({car['year']})")
    else:
        print(f"Автомобіль із номером {license_plate} не існує.")

def main():

    print("команди для вводу: add <номерний_знак> <марка> <рік>, view <номерний_знак>, exit")

    while True:
        command = input("> ")
        if command == "exit":
            print("Програма завершена.")
            break
        parts = command.split()
        
        if parts[0] == "add" and len(parts) == 4:
            license_plate = parts[1]
            make = parts[2]
            try:
                year = int(parts[3])
                add_car(license_plate, make, year)
            except ValueError:
                print("!! рік повинен бути числом.")
        elif parts[0] == "view" and len(parts) == 2:
            license_plate = parts[1]
            view_car(license_plate)
        else:
            print("некоректний формат.")

if __name__ == "__main__":
    main()