"""Given a year, return the century it is in.

examples :
			centuryFromYear(1705)  returns (18)
			centuryFromYear(1900)  returns (19)
			centuryFromYear(1601)  returns (17)
			centuryFromYear(2000)  returns (20)
"""
import math

def century(year):
    result = math.ceil(year/100)  #ceil function makes it easy
    return result
print(century(1705))


"""Output :
18
[Finished in 0.2s]
"""
