import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

df = pd.DataFrame(data)

nato_dict = {row.letter: row.code for (i, row) in df.iterrows()}

is_on = True
while is_on:
    name = input("Enter your name: ").upper()

    if name == "exit()":
        is_on = False
    else:
        phonetic_spelling = [nato_dict[letter] for letter in name]
        print(phonetic_spelling)
