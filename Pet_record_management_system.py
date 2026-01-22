pet_records = []

def add_pet():
    owner = input("Enter owner name: ")
    pet_name = input("Enter pet name: ")
    pet_type = input("Enter pet type: ")
    pet_records.append({
        "owner": owner,
        "pet_name": pet_name,
        "pet_type": pet_type
    })
    print("Pet record added successfully")

def view_pets():
    if not pet_records:
        print("No pet records found")
    else:
        for p in pet_records:
            print("Owner:", p["owner"])
            print("Pet Name:", p["pet_name"])
            print("Pet Type:", p["pet_type"])
            print("------------------")

def main():
    while True:
        print("1. Add Pet Record")
        print("2. View Pet Records")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_pet()
        elif choice == "2":
            view_pets()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
