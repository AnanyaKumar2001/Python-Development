speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44,
         'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

speed_list = list()

for item in speed.values():
    if item not in speed_list:
        speed_list.append(item)

print(speed_list)
