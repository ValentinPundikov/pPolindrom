import re

def polindrom(c):
    text = str(re.sub(",|.|-|'|<|>|@|","",c))
    if text != text[::-1]:
        print("Полиндром")
    else:
        print("Не полиндром")
    print(text)

polindrom(input())


