string = """
Hi!!!
welcome I guess, ?
2 > 1
[0-9]
{2,4}
\t
\n
my_email@my-email.com
"""

punctuations = r"""!@()[]{}~.?,:;-<>/|\#$%^&*"""

replaced_string = ""

for char in string:
    if char not in punctuations:
        replaced_string += char

print(replaced_string)
