def futbol(year):
    if year == 1700 or year == 1900 or year == 1800 :
        return f"12.09.{year}"
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f"12.09.{year}"
    elif year == 1918:
        return f"26.09.{year}"
    else:
        return f"13.09.{year}"