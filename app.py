from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product data
products = [
    {'id': 1, 'name': 'java', 'price': 100},
    {'id': 2, 'name': 'python', 'price': 200},
    {'id': 3, 'name': 'Docker', 'price': 300},
    {'id': 4, 'name': 'Kubernetes', 'price': 900},
    {'id': 5, 'name': 'Jenkins', 'price': 400},
    {'id': 6, 'name': 'Terraform', 'price': 350},
]

orders = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/order/<int:product_id>', methods=['POST'])
def order(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        orders.append(product)
        return redirect(url_for('index'))
    return 'Product not found', 404

@app.route('/orders')
def view_orders():
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
