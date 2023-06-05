from flask import Flask,request,render_template
from database.database import create_database, get_products, add_product_from_dict, add_to_cart_from_dict, delete_from_cart, edit_quantity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
create_database(app)

users={
       'pourya':'p1382',
       'erfan':'e1381',
       }
L=[]
status=0

@app.route("/")
def home():       
    if status==0:
        products = get_products()
        return render_template('products-user.html' , products=products)
    else:
        return render_template('products-admin.html' , products=products)

@app.route('/about us')
def about_us():
    if status==0:
        return render_template('about-user.html')
    else:
        return render_template('about-admin.html')
    
@app.route('/sign in')
def sign_in():
    return render_template('login.html')

@app.route('/logged in', methods=['POST'])
def log_in():
        if request.method == 'POST':
            global user
            user=request.form['username']
            password=request.form['password']
            if users[user]==password:
                global status
                status=1
                return render_template('welcome.html',admin=user)
            else :
                return render_template('login.html')
            
@app.route('/add product')
def add_product():
    return render_template('add-product.html')

@app.route('/logout', methods=['POST'])
def log_out(): 
    global status
    status=0
    return render_template('logout.html', admin=user)

@app.route('/detail', methods=['POST'])
def show_detail():
    product_id=request.form['product id']
    product=products[int(product_id)-1]
    return render_template('details-user.html' , product=product)

@app.route('/product added', methods=['POST'])
def product_added():
        price = request.form['Price']
        name = request.form['Name']
        img_link = request.form['Picture_link']
        data = {
        'name': name,
        'image_path': img_link,
        'price': price}
        
        add_product_from_dict(data)
        
        return render_template('add-product.html')
        
app.run()


