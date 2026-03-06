from collections import UserDict

class Field:
    def __init__(self, value):
        if self.validate(value):
            self.value = value

    def validate(self, value):
        return True

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    # реалізація класу
    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Value Error: Phone number must be 10 digits long")
        return True
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
        else:
            raise ValueError(f"Value Error: Phone number {old_phone} isn`t exists")

    def find_phone(self, phone) -> Phone | None:
        phones = list(filter(lambda p: p.value == phone, self.phones))
        return phones[0] if len(phones) > 0 else None 

    def remove_phone(self, phone):
        self.phones.remove(self.find_phone(phone))

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)  
    
    def delete(self, name: str):
        self.data.pop(name)  
        # del self.data[name]  
        

    def __str__(self):
        lines = "  Address Book\nName    Phones\n" 
        for name, numbers in self.data.items():
            lines += f"{name}: {'; '.join(p_n.value for p_n in numbers.phones)}\n"

        return lines


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# # Видалення запису Jane
book.delete("Jane")
# print(book)