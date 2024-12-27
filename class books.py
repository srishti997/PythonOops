class Book:
    def __init__(self):
        self.title = input('Enter the title: ')
        self.author = input('Enter the author: ')
        self.publisher = input('Enter the publisher: ')
        self.isbn_number = input('Enter the ISBN number: ')
    def read_data(self):
        self.title = input('Enter the title: ')
        self.author = input('Enter the author: ')
        self.publisher = input('Enter the publisher: ')
        self.isbn_number = input('Enter the ISBN number: ')
    def display_data(self):
        print('Title: {}'.format(self.title))
        print('Author: {}'.format(self.author))
        print('Publisher: {}'.format(self.publisher))
        print('ISBN number: {}'.format(self.isbn_number))
def main():
    book = Book()
    book.display_data()
    print()
    book.read_data()
    book.display_data()
if __name__ == '__main__':
    main()
