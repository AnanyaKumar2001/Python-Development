# ------------------------------------------------------------
# -----------------**## Logical Operators ##**----------------

"""
1- and
2- or
3- not
"""

# Example 1 ->>> Processing Loans ->>>> and LO
# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print("Eligible For Loan")
# else:
#     print("Not Eligible For Loan")


# Example 2 ->>> Processing Loans ->>>> or LO
# high_income = False
# good_credit = False

# if high_income or good_credit:
#     print("Eligible For Loan")
# else:
#     print("Not Eligible For Loan")


# Example 3 ->>> Processing Loans ->>>> not LO
# high_income = True
# good_credit = True
# student = True
student = False

if not student:
    print("Eligible For Loan")
else:
    print("Not Eligible For Loan")
