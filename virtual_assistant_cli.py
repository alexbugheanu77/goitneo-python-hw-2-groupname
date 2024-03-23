from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # class' realisation

class Phone(Field):
    # class' realisation

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # class' realisation

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # class' realisation

    # Creation of a new address book 
    book = AddressBook()

    # Creation of a entry for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add a John entry to the address book
    book.add_record(john_record)

    # Creating and adding a new entry for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Displaying all entries in the contact list
    for name, record in book.data.items():
        print(record)

    # Find and edit a phone number for John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Displaying: Contact name: John, phones: 1112223333; 5555555555

    # Searching for a specific phone number in John's entry
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  
    # Deletion: 5555555555

    # Deletion Jane's entry
    book.delete("Jane")