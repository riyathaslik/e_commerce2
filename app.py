from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'ecommerce_secret_key' # Required to encrypt session data

# Sample product list
PRODUCTS = [
    {"id": 1, "name": "Minimalist Watch", "price": 120, "img": "https://picsum.photos/id/175/200/200"},
    {"id": 2, "name": "Leather Bag", "price": 85, "img": "https://picsum.photos/id/209/200/200"},
    {"id": 3, "name": "Wireless Earbuds", "price": 150, "img": "https://picsum.photos/id/434/200/200"},
    {"id": 4, "name": "Smart Speaker", "price": 95, "img": "https://picsum.photos/id/160/200/200"}
]

@app.route('/')
def index():
    # Initialize cart if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []
    return render_template('index.html', products=PRODUCTS)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    # Find the product details by ID
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        session['cart'].append(product)
        session.modified = True # Tells Flask the session data changed
    return redirect(url_for('index'))

@app.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('checkout.html', cart=cart, total=total)

@app.route('/clear')
def clear_cart():
    session['cart'] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)