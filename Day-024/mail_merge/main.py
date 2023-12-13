# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Read them into a list
with open("Input/Names/invited_names.txt", 'r') as file:
    names = file.readlines()

# Read them into a str
with open("Input/Letters/starting_letter.txt", 'r') as file:
    letter = file.read()

for name in names:
    name = name.strip()
    new_letter = letter.strip()
    new_letter = new_letter.replace("[name]", name)
    fileName = f"Output/ReadyToSend/letter_for_{name}.txt"
    with open(fileName, 'w') as file:
        file.write(new_letter)
