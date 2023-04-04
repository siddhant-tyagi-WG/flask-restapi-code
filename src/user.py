from library import Library
class User(Library):
    def filter_functionality(self,library):
        """

        :param library:
        :return: none
        """

        filter_input=input('Enter the basis on which you want the filter \n press 1 for title \n press 2 for author \n press 3 for genre')
        if(filter_input=='1'):
            title_filter_input=input('enter the title you want to filter for')
            kp=False
            for obj in library.my_list:
                if (obj.count>0 and obj.title==title_filter_input):
                    print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}\n')
                    kp=True
            if (kp == False):
                library.print_my_list()

        elif (filter_input == '2'):
            author_filter_input = input('enter the author you want to filter for')
            kp=False
            for obj in library.my_list:
                if (obj.count>0 and obj.author == author_filter_input):
                    print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}\n')
                    kp=True
            if (kp == False):
                library.print_my_list()
        elif(filter_input=='3'):
            genre_filter_input=input('enter the genre you want to filter for\n')
            kp=False
            for obj in library.my_list:
                if (obj.count>0 and obj.genre == genre_filter_input):
                    print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}\n')
                    kp=True
            if (kp == False):
                library.print_my_list()


    def show_my_data(self,admin,email):
        """

        :param admin:
        :param email:
        :return: None
        """
        flag = False
        for obj in admin.user_data_dict.get(email, []):
            flag = True
            print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author}\n')
        if flag==False:
            print('NO books are issued  for this user\n')