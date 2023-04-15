def first_and_last_same(list):
    print("Given List:", list)

    first_el = list[0]
    last_el = list[-1]

    if first_el == last_el:
        return True

    else:
        return False


# test_list = [10, 20, 30, 40, 10]
test_list = [10, 20, 30, 40, 50]
print("Result:", first_and_last_same(test_list))
