# little_things.py
# import AES256 encryption?

def find_the_right_words(text):
    words = text.split(" ")

    if len(words) % 2 == 0:
        return  "404 : words not found"
    else:
        return words[len(words)//2]
    

a_letter =  "just some long rambling words from an old man."

the_right_word = find_the_right_words(a_letter)

print(the_right_word)