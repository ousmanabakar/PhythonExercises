import re

words =["BBC","Cat","Bit","Cow","Doubt","man","Git","Does","About"]

new_words=[word for word in words if re.match(".*t$",word)]

for w in new_words:
    print(w)
