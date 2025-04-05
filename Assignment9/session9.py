import csv

file_name = "C:/Users/1416274/Documents/CIS206_Katsiaryna_Fiodarava/Assignment9/customers.csv"

# Read the customer data 
def read_customers(file_name):
    customers = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            customers.append(row)
    return customers

# Display the customers sorted by company name
def display_by_company(customers):
    customers.sort(key=lambda x: x['CompanyName'])
    for customer in customers:
        print(f"Company: {customer['CompanyName']} | Contact: {customer['ContactName']} | Phone: {customer['Phone']}")

# Display the customers sorted by contact name
def display_by_contact(customers):
    customers.sort(key=lambda x: x['ContactName'])
    for customer in customers:
        print(f"Contact: {customer['ContactName']} | Company: {customer['CompanyName']} | Phone: {customer['Phone']}")

# Search customers by company name
def search_by_company(customers, search_term):
    print(f"Search results for company containing '{search_term}':")
    for customer in customers:
        if search_term.lower() in customer['CompanyName'].lower():
            print(f"Company: {customer['CompanyName']} | Contact: {customer['ContactName']} | Phone: {customer['Phone']}")

# Search customers by contact name
def search_by_contact(customers, search_term):
    print(f"Search results for contact containing '{search_term}':")
    for customer in customers:
        if search_term.lower() in customer['ContactName'].lower():
            print(f"Contact: {customer['ContactName']} | Company: {customer['CompanyName']} | Phone: {customer['Phone']}")

# Main function 
def main():
    file_name = "C:/Users/1416274/Documents/CIS206_Katsiaryna_Fiodarava/Assignment9/customers.csv"
    customers = read_customers(file_name)

    while True:
        print("\n1. Display customers sorted by Company Name")
        print("2. Display customers sorted by Contact Name")
        print("3. Search customers by Company Name")
        print("4. Search customers by Contact Name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_by_company(customers)
        elif choice == '2':
            display_by_contact(customers)
        elif choice == '3':
            search_term = input("Enter company name or part of it: ")
            search_by_company(customers, search_term)
        elif choice == '4':
            search_term = input("Enter contact name or part of it: ")
            search_by_contact(customers, search_term)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
