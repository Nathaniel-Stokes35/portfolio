import csv
 
def read_dictionary(filename, key_column_index):

    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary
 
def main():
    products_dict = read_dictionary('./products.csv', 0)
    print("All Products")
    print(products_dict)
 
    print("\nRequested Items")
    with open('./request.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            product_info = products_dict[product_number]
            product_name = product_info[1]
            price = float(product_info[2])
            print(f"{product_name}: {quantity} @ {price:.2f}")
 
if __name__ == "__main__":
    main()