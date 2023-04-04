
from flask import Flask,request,jsonify
from db import booksdatabase,users,admin,Checkout
from flask_swagger_ui import get_swaggerui_blueprint
import datetime





app = Flask(__name__)

dbs = booksdatabase()
user_obj=users()
admin_obj=admin()
checkout_obj=Checkout()


# Call factory function to create our blueprint


SWAGGER_URL='/swagger'
API_URL='/static/swagger.yaml'
SWAGGER_BLUEPRINT=get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app.name':"Library management system"
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

# dbs=booksdatabase()
#
#
# @app.get("/books")
# def get_books():
#
#     return {"books": dbs.get_books()}
#
#
#
#
#
# @app.route('/book', methods=['GET'])
# def get_item():
#
#     book_id = request.args.get('id')
#     book_id=int(book_id)
#     return dbs.get_book(book_id)


class Booksdatas():




    @app.get("/books")
    def get_books():


        return {"books": dbs.get_books()}

    @app.route('/book', methods=['GET'])
    def get_book():
        try:
            book_id = request.args.get('id')
            book_id=int(book_id)
            return {"book" :dbs.get_book(book_id)} ,200
        except:
            return {"message":"error"} , 404

    @app.post('/add-book')
    def add_book():
        try:
            request_data = request.get_json()
            dbs.add_book(request_data)
            return {"message":"book added successfully"}, 200
        except:
            return {'message': 'error'} ,404

    @app.put('/update-book')
    def update():
        request_data=request.get_json()
        dbs.put_book(request_data)
        return {"message":"book updated successfully"} , 201

    @app.delete('/delete-book')
    def delete():

        try:
            book_id = request.args.get('id')
            dbs.delete_book(book_id)
            return {'success':'book deleted succesfully'} , 200
        except:
            return {"error": "can't do the operation right now"} ,404

    @app.get('/books/filter')
    def filter_title():
        try:
            title = request.args.get('title')
            genre = request.args.get('genre')
            author = request.args.get('author')
            b = dbs.filter_books(title=title, genre=genre, author=author) ,200
            return {'books': b}
        except:
            return {"error": "can't do the operation right now"}, 404




class Userdatas():
    @app.get("/users")
    def get_users():
        try:
            return {"users": user_obj.get_users()},200
        except:
            return {"message": "error"} ,404

    @app.post('/user/signup')
    def signup():
        try:
            request_data = request.get_json()
            user_obj.add_users(request_data)
            return "user added successfully", 201
        except:
            return {'error': 'id already taken,try some different id'} ,404

    @app.put('/user/update')
    def update_user():
        try:
           user_id = request.args.get('user_id')
           request_data = request.get_json()
           user_obj.update_user(int(user_id),request_data)
           return {"message":"user updated successfully"} ,200
        except:
            return {"error":"unable to perform the operation"} ,404

    @app.delete('/user/delete')
    def delete_user():
        try:
            user_id = request.args.get('user_id')
            user_obj.delete_user(int(user_id))
            return {"message":"user deleted successfully"} ,200
        except:
            return {"error":"unable to perform the operation"} ,404

    @app.get('/user')
    def get_user():
        try:
            user_id = request.args.get('user_id')
            user_id = int(user_id)
            return user_obj.get_user(user_id)
        except:
            return {"message":" error"} ,404

    @app.post('/user/login')
    def user_login():
        request_data = request.get_json()
        checker=user_obj.user_logins(request_data)
        if(checker):
            return {"msg":"log in successfully"} ,200
        else:
            return {"msg": "log in unsuccessfull"} ,404








class Admindatas():
    @app.get("/admins")
    def get_admins():
        try:
            return {"Admins": admin_obj.get_admins()} ,200
        except:
            return {'message':'error'} ,404

    @app.put('/admin/update')
    def update_admin():
        try:
            admin_id = request.args.get('admin_id')
            request_data = request.get_json()
            admin_obj.update_admin(int(admin_id), request_data)
            return {"message": "admin updated successfully"}, 200
        except:
            return {"error": "unable to perform the operation"}, 404

    @app.get("/admin")
    def get_admin():
        try:
            admin_id = request.args.get('admin_id')
            return {"Admin": admin_obj.get_admin(int(admin_id))},200
        except:
            return {'message': 'error'},404


class Checkout_datas():
    @app.post('/checkout/add')
    def add_datas():
        try:
            request_data = request.get_json()
            today = datetime.date.today()
            one_week_later = today + datetime.timedelta(days=7)

            checkout_obj.add_data(today, one_week_later, request_data)
            return {"message": "data added successfully"}, 200
        except:
            return {"message":"can't perform the operation"}

    @app.get('/checkout/get-data')
    def get_data():
        try:
            user_id=request.args.get('user_id')
            return {"data": checkout_obj.get_data_of_checkout(int(user_id))} ,201
        except:
            return {'message': 'error'} ,404

    @app.get('/checkout/Data')
    def get_datas():
        try:
            return {"data": checkout_obj.get_all_data()} ,200
        except:
            return {'message': 'error'} ,404


    @app.delete('/checkout/delete-data')
    def delete_data():
        checkout_id=request.args.get('checkout-id')
        checkout_obj.delete_data(checkout_id)
        return {"message":"success: data deleted"} ,200

    @app.get('/checkout/fine')
    def get_fine_amount():
        try:
            checkout_id=request.args.get('checkout-id')
            return {"fine amount" :checkout_obj.fine_amount(checkout_id)},200
        except:
            return {"message":"error"} ,400























obj=Booksdatas()












