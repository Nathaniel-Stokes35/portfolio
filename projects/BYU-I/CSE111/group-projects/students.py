import csv
import re

def main():
    index_column = 0
    student_dict = read_dictionary("portfolio/projects/BYU-I/CSE111/group-projects/students.csv", index_column)
    
    student_number_raw = input('What is the student Number of the individual you are looking up? ')
    student_number_clean = student_number_raw.replace('-', '').strip()

    characters = r'[^0-9-]'
    length = len(student_number_clean)
    invalid = re.search(characters, student_number_raw)

    if invalid is not None or length != 9:
        if invalid != None:
            print('Invalid I-Number')
        elif length > 9:
            print("Invalid I-Number: too many digits")
            pass
        elif length < 9:
            print("Invalid I-Number: too few digits")
            pass
        return
    try:
        student_name = " ".join(student_dict[student_number_clean][1:])
    except KeyError:
        student_name = 'No such student'
    
    print(student_name)

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    rows = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for words in reader:
            if len(words) != 0:
                key = words[key_column_index]
                rows[key] = words
    return rows
if __name__ == "__main__":
  main()