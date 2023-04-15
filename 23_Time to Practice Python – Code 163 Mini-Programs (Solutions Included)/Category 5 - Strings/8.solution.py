str_list = ["Emma", "John", "", "Kelly", None, "Eric", ""]

new_str_list = list(filter(None, str_list))
print(new_str_list)
