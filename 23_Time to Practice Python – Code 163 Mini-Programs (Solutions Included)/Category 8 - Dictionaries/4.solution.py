employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

result_dict = dict.fromkeys(employees, defaults)
print(result_dict)

print(result_dict["Emma"])
