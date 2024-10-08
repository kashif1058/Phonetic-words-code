import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# {"A" : "ALpha", "B", :"Bail"}

# print(data.to_dict())
# create a dictionary  in this format
# phonetic_dict = {Newkey:newvalue for (key, value) ind data}

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# craete a list of ten phonetic code words from a word that the user inputs
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)
