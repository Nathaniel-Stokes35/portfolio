def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f'reversed: {fruit_list}')
    fruit_list.append("orange")
    print(f'append orange: {fruit_list}')
    fruit_list.insert(fruit_list.index('apple'), "cherry")
    print(f'insert cherry: {fruit_list}')
    fruit_list.remove('banana')
    print(f'remove bannana: {fruit_list}')
    fruit_list.pop(-1) 
    print(f'pop orange: {fruit_list}')
    fruit_list.sort()
    print(f'sorted: {fruit_list}')
    fruit_list.clear()
    print(f'cleared: {fruit_list}')
if __name__ == "__main__":
    main()