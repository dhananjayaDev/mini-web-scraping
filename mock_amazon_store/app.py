from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# products = [
#     {
#         "name": "Echo Dot (4th Gen)",
#         "price": 49.99,
#         "image": "https://images-na.ssl-images-amazon.com/images/I/714Rq4k05UL._AC_SL1500_.jpg",
#         "rating": "4.6",
#         "delivery": "Free delivery by tomorrow"
#     },
#     {
#         "name": "Kindle Paperwhite",
#         "price": 129.99,
#         "image": "https://images-na.ssl-images-amazon.com/images/I/61Iz2yy2CKL._AC_SL1000_.jpg",
#         "rating": "4.8",
#         "delivery": "Free delivery by Friday"
#     },
#     {
#         "name": "Amazon Luna Controller",
#         "price": 69.99,
#         "image": "https://m.media-amazon.com/images/I/61RNOxTPxuL._AC_SX679_.jpg",
#         "rating": "4.7",
#         "delivery": "Free delivery by Saturday"
#     },
#     {
#         "name": "Amazon Basics LED Light Bulbs (16-pack)",
#         "price": 19.99,
#         "image": "https://m.media-amazon.com/images/I/71TePRdtdHL._AC_SX679_.jpg",
#         "rating": "4.3",
#         "delivery": "Free delivery by Sunday"
#     },
# ]

products = [
    {
        "id": 0,
        "name": "Echo Dot (4th Gen)",
        "price": 49.99,
        "image": "https://images-na.ssl-images-amazon.com/images/I/714Rq4k05UL._AC_SL1500_.jpg",
        "rating": "4.6",
        "delivery": "Free delivery by tomorrow"
    },
    {
        "id": 1,
        "name": "Kindle Paperwhite",
        "price": 129.99,
        "image": "https://images-na.ssl-images-amazon.com/images/I/61Iz2yy2CKL._AC_SL1000_.jpg",
        "rating": "4.8",
        "delivery": "Free delivery by Friday"
    },
    {
        "id": 2,
        "name": "Amazon Luna Controller",
        "price": 69.99,
        "image": "https://m.media-amazon.com/images/I/61RNOxTPxuL._AC_SX679_.jpg",
        "rating": "4.7",
        "delivery": "Free delivery by Saturday"
    },
    {
        "id": 3,
        "name": "Amazon Basics LED Light Bulbs (16-pack)",
        "price": 19.99,
        "image": "https://m.media-amazon.com/images/I/71TePRdtdHL._AC_SX679_.jpg",
        "rating": "4.3",
        "delivery": "Free delivery by Sunday"
    },
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/update_price", methods=["POST"])
def update_price():
    product_id = int(request.form["product_id"])
    new_price = float(request.form["new_price"])
    products[product_id]["price"] = new_price
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)