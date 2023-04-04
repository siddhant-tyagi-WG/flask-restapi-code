


from admin import admin
from user import User
from library import Library

if __name__=="__main__":
    lc=Library()
    lc.check()
    lc.print_my_list()
    print('----------------')
    ad=admin()
    lc.print_my_list()
    user_obj = User()
    print('----------------')
    #ad.generate_report_of_all_books(lc)
    print('-----------------------')
    print('check complete')
    print('---------------------------------------------\n\n')
    print('                                          Welcome to my library\n\n')
    print('please Login/Signup for the account')
    while 1:
        admin_person=input('press 1 if you want to log in for admin else press any key :')
        if(admin_person=='1'):
            input1=input('Enter your email')
            input2=input('enter your password')
            check_admin=ad.verify(input1,input2)
            if(check_admin==True):
                print('admin login successfully\n')
                while 1:
                    admin_input=input('press 1 for add a book a database \npress 2 to generate a report of all books \npress 3 to see details of a particular user \npress 4 to generate report of all users \npress 5 to see the status of the book \npress 6 to add admin \npress 7 to log out\n')
                    if(admin_input=='1'):
                        ad.add_to_database(lc)
                    elif(admin_input=='2'):
                        ad.generate_report_of_all_books(lc)
                    elif(admin_input=='3'):
                        email_input=input('enter the email of the user that you want the info for :')
                        ad.details_of_particular_user(email_input)
                    elif(admin_input=='4'):
                        ad.generate_report_of_all_users()

                    elif(admin_input=='5'):
                        book_title=input('enter the book name that you want the details of :')
                        ad.check_status_of_the_book(book_title)
                    elif(admin_input=='6'):
                        ad.add_new_member_to_admins()
                    elif(admin_input=='7'):
                        break
            else:
                print('Incorrect Details\n')
        else:

            k = ad.login_signup(lc)
            if(k=='NA' or k=='fk'):
                continue
            kk = k.split()
            if (kk[0] == 'NAC'):
                print('user portal shown up\n')
                user_obj = User()
                while True:
                    user_input = input(
                        'press 1 for seeing the available books : \npress 2 for filter: \npress 3 for show my data \npress 4 to add book \npress 5 for end portal\n')
                    if (user_input == '1'):
                        user_obj.print_my_list()
                    elif (user_input == '2'):
                        user_obj.filter_functionality(lc)
                    elif (user_input == '3'):
                        # print(kk[1])
                        user_obj.show_my_data(ad, kk[1])
                    elif (user_input == '4'):
                        key_to_add_in_database = int(input('Enter the key number of book to add in database'))
                        title_of_the_book=input('Enter the title of the book')
                        ad.change_in_database(lc, kk[1], key_to_add_in_database)
                        ad.book_issue_reissue_status(title_of_the_book)
                    elif (user_input == '5'):
                        break
            elif (kk[0] == 'v'):
                print('user portal shown up\n')

                while True:
                    user_input = input(
                        'press 1 for seeing the available books : \n press 2 for filter: \n press 3 for show my data \n  press 4 to add book \n press 5 for end portal')
                    if (user_input == '1'):
                        user_obj.print_my_list()
                    elif (user_input == '2'):
                        user_obj.filter_functionality(lc)
                    elif (user_input == '3'):
                        # print(kk[1])
                        user_obj.show_my_data(ad, kk[1])
                    elif (user_input == '4'):
                        key_to_add_in_database = int(input('Enter the key number of book to add in database'))
                        ad.change_in_database(lc, kk[1], key_to_add_in_database)
                    elif (user_input == '5'):
                        break
