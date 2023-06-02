from flask import Flask,request,render_template


app=Flask(__name__)

users={
       'pourya':'p1382',
       'erfan':'e1381',
       }
L=[]
status=0
@app.route("/")
def home():       
    if status==0:
        return render_template('products-user.html')
    else:
        return render_template('products-admin.html')

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


app.run()


