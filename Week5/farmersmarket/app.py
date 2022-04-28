from flask import Flask

from flask import request

app = Flask(__name__)

@app.route("/home")
@app.route("/index")
@app.route("/")
def home():
    return "Welcome to the Farmer's Market"

@app.route("/about")
def about():
    return"About the Farmers Market"

@app.route("/products")
def about():
    return"Products at the Farmers Market"

@app.route("/products/<int:product_id>")
def getProduct(product_id):
    return f"Here are the details on product with an ID of {product_id}"

@app.route('/cart', methods=['GET', 'POST'])
def shoppingCart():
    if request.method == 'POST':
        product_id = request.form.get('productid')
        quantity = request.form.get('qnty')
        

if __name__ == "__main__":
    app.run()