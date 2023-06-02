from flask import Flask,request,render_template


app=Flask(__name__)

products=[{
 'id':'1',
 'name':'Kavir CDI 200',
 'img_link': 'https://kavirmotor.com/wp-content/uploads/2022/08/CDI-200.jpg',  
 'price':'150',
 'details':'dkjjdj jvqejop jojojjodwdq jd2dojwdjwoqd'

 },
 {
  'id':'2',
  'name':'Kavir 125',
  'img_link':'https://images.khabaronline.ir/images/2014/11/14-11-30-11555motor.jpg',
  'price':'100',
   'details':'dkjjdjxxxxxxxxxxxxxxxxxxxwdq jd2dojwdjwoqd'

  }
]

users={
       'pourya':'p1382',
       'erfan':'e1381',
       }
L=[]
status=0
@app.route("/")
def home():       
    if status==0:
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

app.run()


