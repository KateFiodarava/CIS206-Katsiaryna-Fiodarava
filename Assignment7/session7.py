file_path = r"C:\Users\1416274\Documents\CIS206_Katsiaryna_Fiodarava\Assignment7\names.txt"
with open(file_path, "r") as file:
    existing_names = {line.strip().lower() for line in file}

with open("nofound.txt", "a") as nofound_file:
    while True:
        name = input("Enter a name (or type 'exit' to quit): ").strip()

        if name.lower() == "exit":
            print("Exiting the program.")
            break
        if name.lower() in existing_names:
            print(f"{name} is in the list.")
        else:
            print(f"{name} was not found. Writing to nofound.txt.")
            nofound_file.write(name + "\n")
