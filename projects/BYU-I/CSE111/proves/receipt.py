import csv
import datetime
 
def read_dictionary(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except PermissionError:
        print(f"Error: You do not have permission to read {filename}.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    return dictionary

def print_receipt(products):
    print("Store Name: Example Store")
    print("-" * 40)
    print("Receipt")
    print("-" * 40)
    
    total_count = 0
    subtotal = 0.0
    coupon_product = None
    try:
        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                if product_number not in products:
                    raise KeyError(f"Product number {product_number} not found.")
                
                product_info = products[product_number]
                product_name = product_info[1]
                price = float(product_info[2])
                total_count += quantity
                if product_number == "D083" and quantity >= 2:
                    itm_at_full = (quantity + 1) // 2
                    itm_at_half = quantity // 2
                    subtotal = itm_at_full * price + itm_at_half * (price * 0.5)
                else:
                    subtotal += quantity * price
                print(f"{product_name}: {quantity} @ {price:.2f}")

                if not coupon_product:
                    coupon_product = product_name

    except FileNotFoundError:
        print("Error: request.csv file not found.")
    except PermissionError:
        print("Error: You do not have permission to read request.csv.")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"Error: {e}")

    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    total_due = subtotal + sales_tax
 
    print("-" * 40)
    print(f"Number of Items: {total_count}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax (6%): {sales_tax:.2f}")
    print(f"Total Amount Due: {total_due:.2f}")
    print("\nRequested Items")

    current_time = datetime.datetime.now(tz=None)
    print("-" * 40)
    print(f"Date & Time: {current_time:%A %I:%M %p}")
    print("-" * 40)
    
    print("Thank you for your purchase!")
    print("-" * 40)

    ROD = current_time + datetime.timedelta(days=30)
    ROD = ROD.replace(hour=21, minute=0, second=0, microsecond=0)
    FoROD = ROD.strftime('%A %I:%M %p')
    print(f"Return By: {FoROD}")

    new_year = datetime.datetime(current_time.year + 1, 1, 1)
    days_until_sale = (new_year - current_time).days
    print(f"Days until New Year's Sale: {days_until_sale} days")

    print(f"\nCoupon: Save 10% on {coupon_product} on your next purchase!")
 
def main():
    products_dict = read_dictionary('products.csv', 0)
    if not products_dict:
        return
    print_receipt(products_dict)

if __name__ == "__main__":
    main()