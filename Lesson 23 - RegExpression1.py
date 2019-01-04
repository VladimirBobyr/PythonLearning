
import re

mytext = "Vasya aaaaaaa 1972, Koly - 1972: Olesya 1981, aaaaaaaa@intel.com," \
         "bbbbbbbbbb@intel.com, Petya gggggggg, 1992, ccccccccc@yahoo.com, " \
         "Vladimir 1977, Irina , 2001, annnnnnn@intel.com, eeeeeeee@yandex.com," \
         "oooooooo@hotmail.gov, ggggggggggg@gov.gov, tututut@giv.hot"

# =========== Look for word(s) ============== #
textlookfor = r"yandex"
allresults = re.findall(textlookfor, mytext)
print(allresults)


"""
\d        = Any digit 0-9
\D        = Any non-digit
\w        = Any alphabet symbol (a-z, A-Z)
\W        = Any non-alphabet symbol
\s        = Space
\S        = Any non-space

[0-9]{3}    = 3 digits
\w{6}\s     = all words with 6 symbols and space after
[A-Z][a-z]+ = 1st sybmol Upercase, 2nd symbol and next (+) is lowercase
\w+\.\w+    = word -> . -> word


"""

#textlookfor = r"\d\d\d"  # 3 digits
#textlookfor = r"[0-9]{3}"  # 3 digits too
#textlookfor = r"\w{6}\s"  # words with space after
#textlookfor = r"[A-Z][a-z]+"  # words with space after
textlookfor = r"@\w+.\w+"  # words with space after
allresults = re.findall(textlookfor, mytext)
print(allresults)

