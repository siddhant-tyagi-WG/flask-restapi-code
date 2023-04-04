import pyodbc


class booksdatabase():

    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAP-55460;DATABASE=books;')
        self.cursor = self.conn.cursor()


    def get_books(self):
        result=[]
        query="select * from booksCollection"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            #here every row is fetched in the form of tuple
            book_dict={}
            book_dict["id"]=row[0]
            book_dict["title"]=row[1]
            book_dict["genre"]=row[2]
            book_dict["author"]=row[3]
            book_dict["available"]=row[4]
            result.append(book_dict)
        return result



    def get_book(self,book_id):
        query = f"select * from booksCollection where id={book_id}"
        self.cursor.execute(query)
        book_dict = {}
        for row in self.cursor.fetchall():

            book_dict["id"] = row[0]
            book_dict["title"] = row[1]
            book_dict["genre"] = row[2]
            book_dict["author"] = row[3]
            book_dict["available"] = row[4]
        return book_dict





    def add_book(self,body):
        query=f"insert into booksCollection(id,title,genre,author,available) values ({body['id']},'{body['title']}','{body['genre']}', '{body['author']}',{body['available']})"
        self.cursor.execute(query)
        self.conn.commit()

    def put_book(self,body):
        query=f"update booksCollection set title='{body['title']}',genre='{body['genre']}', author='{body['author']}', available='{body['available']}' where id='{body['id']}'"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_book(self,book_id):
        query=f"DELETE FROM booksCollection WHERE id={book_id}"
        self.cursor.execute(query)
        self.conn.commit()

    def filter_books(self,title=None, genre=None, author=None):
        query = "SELECT * FROM booksCollection WHERE 1=1"
        params = []

        if title:
            query += " AND title LIKE ?"
            params.append('%' + title + '%')
        if genre:
            query += " AND genre LIKE ?"
            params.append('%' + genre + '%')
        if author:
            query += " AND author LIKE ?"
            params.append('%' + author + '%')

        self.cursor.execute(query, params)
        results = self.cursor.fetchall()
        results = [tuple(row) for row in results]
        res=[]
        for row in results:
            book_dict={}
            book_dict["id"] = row[0]
            book_dict["title"] = row[1]
            book_dict["genre"] = row[2]
            book_dict["author"] = row[3]
            book_dict["available"] = row[4]
            res.append(book_dict)
        return res



class users(booksdatabase):
    def __init__(self):
        booksdatabase.__init__(self)

    def get_users(self):
        result = []
        query = "select * from userCollection"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            # here every row is fetched in the form of tuple
            book_dict = {}
            book_dict["id"] = row[0]
            book_dict["username"] = row[1]
            book_dict["password"] = row[2]
            result.append(book_dict)
        return result

    def add_users(self,body):
        query = f"insert into userCollection(user_id,username,password) values ({body['user_id']},'{body['username']}','{body['password']}')"
        self.cursor.execute(query)
        self.conn.commit()

    def update_user(self,user_id,body):
        query = f"update userCollection set username='{body['username']}', password='{body['password']}' where user_id={user_id}"
        self.cursor.execute(query)
        self.conn.commit()
    def delete_user(self,user_id):
        query = f"DELETE FROM userCollection WHERE user_id={user_id}"
        self.cursor.execute(query)
        self.conn.commit()

    def user_logins(self,body):

        query = "select * from userCollection"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            if(row[1]==body['username'] and row[2]==body['password']):
                return True
        return False






    def get_user(self,user_id):
        query = f"select * from userCollection where user_id={user_id}"
        self.cursor.execute(query)
        user_dict = {}
        for row in self.cursor.fetchall():
            user_dict["user_id"] = row[0]
            user_dict["username"] = row[1]
            user_dict["password"] = row[2]

        return user_dict

class admin(booksdatabase):
    def __init__(self):
        booksdatabase.__init__(self)

    def get_admins(self):
        result = []
        query = "select * from adminCollection"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            book_dict = {}
            book_dict["id"] = row[0]
            book_dict["username"] = row[1]
            book_dict["password"] = row[2]
            result.append(book_dict)
        return result

    def update_admin(self,admin_id,body):
        query = f"update adminCollection set admin_name='{body['admin_name']}', password='{body['password']}' where admin_id={admin_id}"
        self.cursor.execute(query)
        self.conn.commit()
    def get_admin(self,admin_id):
        query = f"select * from adminCollection where admin_id={admin_id}"
        self.cursor.execute(query)
        admin_dict = {}
        for row in self.cursor.fetchall():
            admin_dict["admin_id"] = row[0]
            admin_dict["admin_name"] = row[1]
            admin_dict["password"] = row[2]

        return admin_dict


class Checkout(booksdatabase):
    def __init__(self):
        booksdatabase.__init__(self)

    def add_data(self,checkout_date,due_date,body):
        sql_query = """
        INSERT INTO checkout (user_id, book_id, checkout_date, due_date)
        VALUES (?, ?, ?, ?)
        """

        # Execute the query with the values as parameters
        self.cursor.execute(sql_query,body['user_id'],body['book_id'], checkout_date.strftime('%Y-%m-%d'), due_date.strftime('%Y-%m-%d'))
        self.conn.commit()
        return {"message":"data added successfully"} ,201

    def get_data_of_checkout(self,user_id):
        result = []
        query = f"select * from checkout where user_id={user_id}"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            transaction_dict = {}
            transaction_dict["checkout_id"] = row[0]
            transaction_dict["user_id"] = row[1]
            transaction_dict["book_id"] = row[2]
            transaction_dict["checkout_date"]=row[3]
            transaction_dict["due date"]=row[4]
            result.append(transaction_dict)
        return result

    def get_all_data(self):
        result=[]
        query=f"select * from checkout"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            transaction_dict = {}
            transaction_dict["checkout_id"] = row[0]
            transaction_dict["user_id"] = row[1]
            transaction_dict["book_id"] = row[2]
            transaction_dict["checkout_date"] = row[3]
            transaction_dict["due date"] = row[4]
            result.append(transaction_dict)
        return result

    def delete_data(self,checkout_id):
        query=f"delete from checkout where checkout_id={checkout_id}"
        self.cursor.execute(query)
        self.conn.commit()

    def fine_amount(self,checkout_id):
        query = f"SELECT DATEDIFF(day,checkout_date, GETDATE()) AS days_diff FROM checkout WHERE checkout_id = {checkout_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        result=int(result)
        if(result<=7):
            return 0
        else:
            return (result-7)*5


















dbsk=booksdatabase()
dbsk.get_books()