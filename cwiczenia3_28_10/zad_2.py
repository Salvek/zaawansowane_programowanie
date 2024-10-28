from datetime import date

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Library in {self.city}, {self.street}, ZIP: {self.zip_code}, "
                f"Open Hours: {self.open_hours}, Phone: {self.phone}")

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee: {self.first_name} {self.last_name}, Hired: {self.hire_date}, "
                f"Birth Date: {self.birth_date}, Address: {self.city}, {self.street}, ZIP: {self.zip_code}, "
                f"Phone: {self.phone}")

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book by {self.author_name} {self.author_surname}, Published: {self.publication_date}, "
                f"Pages: {self.number_of_pages}, Library: [{self.library}]")

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join([str(book) for book in self.books])
        return (f"Order Date: {self.order_date}\nEmployee: [{self.employee}]\n"
                f"Student: [{self.student}]\nBooks Ordered:\n{books_str}\n")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

library1 = Library("Warsaw", "Main St 1", "00-001", "9:00-18:00", "123-456-789")
library2 = Library("Krakow", "Old Town 5", "30-001", "10:00-16:00", "987-654-321")

book1 = Book(library1, date(2001, 5, 21), "Adam", "Mickiewicz", 300)
book2 = Book(library2, date(1995, 8, 15), "Henryk", "Sienkiewicz", 450)
book3 = Book(library1, date(2010, 11, 3), "Juliusz", "Slowacki", 320)
book4 = Book(library2, date(2018, 2, 28), "Boleslaw", "Prus", 280)
book5 = Book(library1, date(2021, 7, 14), "Maria", "Konopnicka", 220)

employee1 = Employee("Jan", "Kowalski", date(2020, 6, 15), date(1985, 4, 10), "Warsaw", "Street 1", "00-001", "123-000-123")
employee2 = Employee("Anna", "Nowak", date(2018, 9, 20), date(1990, 7, 22), "Krakow", "Street 2", "30-002", "321-111-321")
employee3 = Employee("Piotr", "Zalewski", date(2021, 1, 5), date(1995, 1, 12), "Warsaw", "Street 3", "00-003", "456-222-456")

student1 = Student("Adam Majewski", [70, 80, 90])
student2 = Student("Ewa Kozlowska", [50, 40, 60])
student3 = Student("Tomasz Nowak", [30, 45, 55])

order1 = Order(employee1, student1, [book1, book2], date(2023, 10, 10))
order2 = Order(employee2, student2, [book3, book4, book5], date(2023, 10, 15))

print(order1)
print(order2)
