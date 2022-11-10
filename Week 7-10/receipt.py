import pandas as pd

def main():

    products = pd.read_csv("https://byui-cse.github.io/cse111-course/lesson09/products.csv")
    request = pd.read_csv("https://byui-cse.github.io/cse111-course/lesson09/request.csv")

    all_products = create_dict(products)
    print(all_products)
    print()

    all_requests = create_requests(request, all_products)
    for x in all_requests:
        print(x)

def create_dict(products):

    y = 0
    products_dict = {}

    for x in products.iterrows():   
        products_dict[products["Product #"][y]] = [products["Product #"][y], products["Name"][y], format(float(products["Price"][y]),'.2f')]
        y += 1
    return products_dict

def create_requests(request, products):
    y= 0
    request_quantity = []
    for x in range(len(request)):
        key = request["Product #"][y]
        request_name = products[key][1]
        request_count = request["Quantity"][y]
        request_price = products[key][2]
        request_statement =  str(request_name) + ": " + str(request_count) + " @ $" + str(request_price)
        y += 1

        request_quantity.append(request_statement)

    return request_quantity

main()
