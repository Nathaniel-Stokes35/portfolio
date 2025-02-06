import random
def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    numbers = append_random_numbers(numbers)
    print(numbers)
    numbers = append_random_numbers(numbers, 5)
    print(numbers)
def append_random_numbers(list, quantity=1):
    for _ in range(quantity):
        list.append(round(random.uniform(0, 100), 1))
    return list
if __name__ == "__main__":
    main()