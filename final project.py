user_credentials = {
    'jarylkurt': '12345'
    
}
office_database=[]

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        return username
    else:
        return print("Login failed. Please try again.")

def introduction(username):
    if username:
        print(f"Welcome, {username} to the DOJ Prosecutor's Office Database.")
    else:
        print("Login failed. Please try again.")

def add_document():
    Title = input("Enter the Case Title: ")
    kaso = input("Enter the Criminal Case No.: ")
    casecharges = input("Enter the Case Charges: ")
    casesummary = input("Enter the Case Summary: ")
    keydates = input("Enter the Key Dates: ")
    status = input("Enter the latest Status: ")

    document = {
        'Case Title': Title,
        'Criminal Case No': kaso,
        'Case Charges': casecharges,
        'Case Summary': casesummary,
        'Key Dates': keydates,
        'Case Status': status,
    }
    office_database.append(document)
    print("Document Added Successfully!")

def view_document():
    if not office_database:
        print("The Database is Empty. No Documents on Display")
    else:
        for document in office_database:
            print("Case Title:", document['Case Title'])
            print("Criminal Case No:", document['Criminal Case No'])
            print("Case Charges:", document['Case Charges'])
            print("Case Summary:", document['Case Summary'])
            print("Key Dates:", document['Key Dates'])
            print("Case Status:", document['Case Status'])

def update_keydates():
    title = input("Enter the Case Title: ")
    new_keystatus = input("Enter the Latest Key Dates: ")

    updated = False
    for document in office_database:
        if title == document['Case Title']:
            document['Key Dates'] = new_keystatus
            updated = True
            print("Key Dates updated successfully.")
    
    if not updated:
        print("Document not found. Key Dates not updated.")

def update_status():
    title = input("Enter the Case Title: ")
    new_casestatus = input("Enter the Latest Case Status: ")

    updated = False
    for document in office_database:
        if title == document['Case Title']:
            document['Case Status'] = new_casestatus
            updated = True
            print("Case Status updated successfully.")
    
    if not updated:
        print("Document not found. Key Dates not updated.")


def search_document():
    search_term = input("Enter your Case Title or the Case Charges: ")
    found = False
    for document in office_database:
        if search_term in document['Case Title'] or search_term in document ['Case Charges']:
            print("Document Found: ")
            print("Case Title:", document['Case Title'])
            print("Criminal Case No:", document['Criminal Case No'])
            print("Case Charges:", document['Case Charges'])
            print("Case Summary:", document['Case Summary'])
            print("Key Dates:", document['Key Dates'])
            print("Case Status:", document['Case Status'])
            print()
            found = True
    if not found:
        print("The Document are Not Found in the Database.")

def main():
    username = None

    while not username:
        print("Welcome to DOJ Administrator Database System")
        print("Please put your Username and password correctly.")
        username = login()

    introduction(username)

    while True:
        print("Menu:")
        print("1. Add a New Case")
        print("2. View All of the Documents")
        print("3. Search the Documents")
        print("4. Update the Key Dates of the document")
        print("5. Update the Case Status of the document")
        print("6. Exit")
        choice = input("Enter your Choice: ")

        if choice == '1':
            add_document()
        elif choice == '2':
            view_document()
        elif choice == '3':
            search_document()
        elif choice == '4':
            update_keydates()
        elif choice == '5':
            update_status()
        elif choice == '6':
            print("Exiting Process................ Exiting Complete.")
            break
        else:
            print("Invalid Choice, Please Try Again.")

if __name__ == '__main__':
    main()

    