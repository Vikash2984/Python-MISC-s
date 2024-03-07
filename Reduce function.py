def myfunct(year_value):
    if (year_value % 400 == 0): return True
    if (year_value % 4 == 0 and year_value % 100 != 0): return True
    return False
print (list(filter(myfunct, [1800, 2000, 1900, 2024, 2020])))
