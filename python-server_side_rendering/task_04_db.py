import sqlite3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    error_message = None
    products = []

    if source == "json":
        with open("products.json", "r") as file:
            products = json.load(file)
    elif source == "csv":
        with open("products.csv", "r") as file:
            products = list(csv.DictReader(file))
    elif source == "sql":
        products, error_message = fetch_products()
    else:
        error_message = "Wrong source"
    
    if product_id and not error_message:
        matching_products = []

        for product in products:
            if str(product["id"]) == product_id:
                matching_products.append(product)
    
        if not matching_products:
            error_message = "Product not found"
        else:
            products = matching_products
    
    return render_template(
        "product_display.html",
        products=products,
        error_message=error_message
    )


def fetch_products():
    conn = None
    products = []
    error_message = None

    try:
        conn = sqlite3.connect("products.db")
        # Makes returns from db behave like dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()


        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()

        products = [dict(row) for row in products]

    except sqlite3.Error as e:
        error_message = f"Database error: {e}"
    finally:
        if conn:
            conn.close()

    return products, error_message

if __name__ == "__main__":
    app.run(debug=True, port=5000)