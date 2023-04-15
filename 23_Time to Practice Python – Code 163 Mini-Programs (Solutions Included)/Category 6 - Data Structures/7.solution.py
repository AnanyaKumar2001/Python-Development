roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print(roll_number)

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]

print(roll_number)
