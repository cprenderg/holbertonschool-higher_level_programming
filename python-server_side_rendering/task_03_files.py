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