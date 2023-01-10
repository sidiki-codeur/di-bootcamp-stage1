words=input("enter sequence of words the words separated by commas : ")

words_liste=words.split(",")

words_liste.sort()

result= ",".join(words_liste)

print(result)