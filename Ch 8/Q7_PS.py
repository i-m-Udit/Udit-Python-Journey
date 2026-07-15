word_list=["Hello","Udit","Rohit","Rohan","Virat"]
word=input("Enter the word:")
def func(word,word_list):
    word=word.strip()
    if word in word_list:
        word_list.remove(word)
        return word_list
    else:
        print("Your word is not in the word list")
    return word_list
print(func(word,word_list))