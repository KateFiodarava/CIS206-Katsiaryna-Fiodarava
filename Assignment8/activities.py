import csv

filename = "C:/Users/1416274/Documents/CIS206_Katsiaryna_Fiodarava/Assignment8/Northwind.csv"


# Function to read customers from a CSV file
def read_customers(filename):
    customers = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if len(row) >= 10:  # Enough columns
                    company = row[1].strip()  # Company is in column 1
                    contact = row[2].strip()  # Contact is in column 2
                    phone = row[9].strip()  # Phone is in column 9
                    customers.append((company, contact, phone))  # Add customer
    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
    return customers

# Function to display sorted customers
def display_sorted(customers, sort_by):
    sorted_customers = sorted(customers, key=lambda x: x[sort_by])
    for customer in sorted_customers:
        print(f"Company: {customer[0]}, Contact: {customer[1]}, Phone: {customer[2]}")

# Function to search customers by company or contact
def search_customers(customers, search_term, search_by):
    matches = [cust for cust in customers if search_term.lower() in cust[search_by].lower()]
    if matches:
        for match in matches:
            print(f"Company: {match[0]}, Contact: {match[1]}, Phone: {match[2]}")
    else:
        print("No matching records found.")

# Main function to interact with the user
def main():
    filename = "C:/Users/1416274/Documents/CIS206_Katsiaryna_Fiodarava/Assignment8/Northwind.csv"  
    customers = read_customers(filename)
    
    if not customers:
        return  # Exit if no customers are found
    
    while True:
        print("\nMenu:")
        print("1. Display customers sorted by company name")
        print("2. Display customers sorted by contact name")
        print("3. Search by company name")
        print("4. Search by contact name")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            display_sorted(customers, 0)  # Sort by company name
        elif choice == "2":
            display_sorted(customers, 1)  # Sort by contact name
        elif choice == "3":
            term = input("Enter company name or part of it: ")
            search_customers(customers, term, 0)  # Search by company
        elif choice == "4":
            term = input("Enter contact name or part of it: ")
            search_customers(customers, term, 1)  # Search by contact
        elif choice == "5":
            print("Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
