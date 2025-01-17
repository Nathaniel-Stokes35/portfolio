items = int(input('How many items do you have? '))
boxes = int(input('How many items can fit in a box? '))

complete_boxes = items % boxes
if complete_boxes > 0:
    total = (items // boxes) + 1
else:
    total = items // boxes

print(f'You need {total} boxes.')