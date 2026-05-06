from flask import Flask, render_template, request, redirect
from db_config import get_db_connection

app = Flask(__name__)

# Dashboard
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM suppliers")
    suppliers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM products")
    products = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM customers")
    customers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM orders")
    orders = cursor.fetchone()[0]

    conn.close()
    return render_template('index.html', suppliers=suppliers, products=products, customers=customers, orders=orders)

# Suppliers
@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        supplier_name = request.form['supplier_name']
        contact_person = request.form['contact_person']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        cursor.execute("""
            INSERT INTO suppliers (supplier_name, contact_person, phone, email, address)
            VALUES (%s, %s, %s, %s, %s)
        """, (supplier_name, contact_person, phone, email, address))
        conn.commit()
        conn.close()
        return redirect('/suppliers')

    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()
    conn.close()
    return render_template('suppliers.html', suppliers=suppliers)

# Products
@app.route('/products', methods=['GET', 'POST'])
def products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        product_name = request.form['product_name']
        category = request.form['category']
        price = request.form['price']
        supplier_id = request.form['supplier_id']
        description = request.form['description']

        cursor.execute("""
            INSERT INTO products (product_name, category, price, supplier_id, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (product_name, category, price, supplier_id, description))
        conn.commit()
        conn.close()
        return redirect('/products')

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()

    conn.close()
    return render_template('products.html', products=products, suppliers=suppliers)

# Warehouses
@app.route('/warehouses', methods=['GET', 'POST'])
def warehouses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        warehouse_name = request.form['warehouse_name']
        location = request.form['location']
        capacity = request.form['capacity']

        cursor.execute("""
            INSERT INTO warehouses (warehouse_name, location, capacity)
            VALUES (%s, %s, %s)
        """, (warehouse_name, location, capacity))
        conn.commit()
        conn.close()
        return redirect('/warehouses')

    cursor.execute("SELECT * FROM warehouses")
    warehouses = cursor.fetchall()
    conn.close()
    return render_template('warehouses.html', warehouses=warehouses)

# Inventory
@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        product_id = request.form['product_id']
        warehouse_id = request.form['warehouse_id']
        stock_quantity = request.form['stock_quantity']
        last_updated = request.form['last_updated']

        cursor.execute("""
            INSERT INTO inventory (product_id, warehouse_id, stock_quantity, last_updated)
            VALUES (%s, %s, %s, %s)
        """, (product_id, warehouse_id, stock_quantity, last_updated))
        conn.commit()
        conn.close()
        return redirect('/inventory')

    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.execute("SELECT * FROM warehouses")
    warehouses = cursor.fetchall()

    conn.close()
    return render_template('inventory.html', inventory=inventory, products=products, warehouses=warehouses)

# Customers
@app.route('/customers', methods=['GET', 'POST'])
def customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        customer_name = request.form['customer_name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        cursor.execute("""
            INSERT INTO customers (customer_name, phone, email, address)
            VALUES (%s, %s, %s, %s)
        """, (customer_name, phone, email, address))
        conn.commit()
        conn.close()
        return redirect('/customers')

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return render_template('customers.html', customers=customers)

# Orders
@app.route('/orders', methods=['GET', 'POST'])
def orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        order_date = request.form['order_date']
        total_amount = request.form['total_amount']
        status = request.form['status']

        cursor.execute("""
            INSERT INTO orders (customer_id, order_date, total_amount, status)
            VALUES (%s, %s, %s, %s)
        """, (customer_id, order_date, total_amount, status))
        conn.commit()
        conn.close()
        return redirect('/orders')

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    conn.close()
    return render_template('orders.html', orders=orders, customers=customers)

# Shipments
@app.route('/shipments', methods=['GET', 'POST'])
def shipments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        order_id = request.form['order_id']
        shipment_date = request.form['shipment_date']
        delivery_date = request.form['delivery_date']
        shipment_status = request.form['shipment_status']

        cursor.execute("""
            INSERT INTO shipments (order_id, shipment_date, delivery_date, shipment_status)
            VALUES (%s, %s, %s, %s)
        """, (order_id, shipment_date, delivery_date, shipment_status))
        conn.commit()
        conn.close()
        return redirect('/shipments')

    cursor.execute("SELECT * FROM shipments")
    shipments = cursor.fetchall()

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    conn.close()
    return render_template('shipments.html', shipments=shipments, orders=orders)

if __name__ == '__main__':
    app.run(debug=True)