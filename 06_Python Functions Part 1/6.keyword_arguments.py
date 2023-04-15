# ------------------------------------------------------------
# ------------**## Keyword Arguments (**kwargs) ##**----------


# ***************------------ Example 12
def employee(**info):
    print(info)

# employee(name="Clint", last_name="Johnson", age=34, skill_set="Developer")


# ***************------------ Example 13
def to_do(**to_do_status):
    return to_do_status


to_do_status_result = to_do(
    get_coffee="Done", exercise="Pending", watch_tv="In Progress")

print(to_do_status_result)
