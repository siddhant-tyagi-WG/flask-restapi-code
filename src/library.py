
from book import Book




class Library:

    def __init__(self):
        self.my_list=[]
        self.key_val=0
        self.user_dict={}
        self.my_unique_books = set()
    def check(self):
        """

        :return: none
        """
        self.my_list.append(Book(self.key_val,'fundamentals of wavelets','goswami','signal_processing',1))
        self.my_unique_books.add('fundamentals of wavelets'+'goswami')
        self.key_val=self.key_val+1

        self.my_list.append(Book(self.key_val,'data smart','foreman','data_science',1))
        self.my_unique_books.add('data smart'+'foreman')
        self.key_val = self.key_val + 1

        self.my_list.append(Book(self.key_val, 'birth of theorm', 'vilani', 'mathematics',1))
        self.my_unique_books.add('birth of theorm'+'vilani')
        self.key_val = self.key_val + 1



    def print_my_list(self):
        """

        :return: none
        """
        for obj in self.my_list:
            if (obj.count > 0):
                print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}')
        print('---------------------------------------------------------------------------------------------')
        print('\n\n')
