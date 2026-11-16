import letter_counter

text = input("text: ")
letter = input("letter: ")
print(f"The letter '{letter}' appears {letter_counter.count_letter(text,letter)} times in the text")
