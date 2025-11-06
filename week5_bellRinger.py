# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
# a. Retrieve the 5th character.
fifth_char = print(magic[4])
# b. Retrieve the second to last character.
second_to_last_char = print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
first_c_index = print(magic.index('r'))
# find the last occurrence of the letter
last_a_index = print(magic.rindex('a'))
# rindex finds the last occurrence of a specified value.

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
# hij = print(alphabet[7:10])
hij = print(alphabet.index('hij')) # output: 7
hij2 = print(alphabet[7:10]) # output: hij
# b. Extract every second letter starting from 'a' to 'm'.
# get the letter m
m_index = print(alphabet.index('m')) # output: 12
every_second = print(alphabet[0:13:2]) # output: acegikm

# c. Reverse the entire string using slicing.
reversed_alphabet = print(alphabet[ : :-1])

# i have a dream speech
i_have_a_dream = "And when this happens, and when we allow freedom ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual"

# reverse the i have a dream speech
reversed_speech = print(i_have_a_dream[ : :-1])


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
famous_quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
john_f_kennedy = print(famous_quote.find("John F. Kennedy"))
# output: 83
extracted_name = print(famous_quote[83:])



# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the letter 'subjective' without knowing its exact position.
print(info.rfind("subjective"))
extracted_letter = print(info[36:])
# b. Extract every third word.
third_letter = print(info[:3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
words = info.split() # Split the string into words
print(words) # Output: ['Python', 'is', 'fun', 'fun', 'is', 'good', 'is', 'subjective.' ]
reversed_words = ' '.join(reversed(words)) # reverse the list of words back into a string
print(reversed_words) # Output: suibjective. is Good good. fun is 


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU."
lowercase = print(text.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
joined_motto = ' '.join(motto)
print(joined_motto) # Output: Make haste slowly.
# b. Now, split the string at every occurrence of the letter 'a'.
joined_motto_split = joined_motto.split('a')
print(joined_motto_split)





# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

sentence = "Life is what happens when you are busy making other plans."
replaced_sentence = print(sentence.replace("busy", "distracted").replace("plans", "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repeated_word = print("Iteration " * 7)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.