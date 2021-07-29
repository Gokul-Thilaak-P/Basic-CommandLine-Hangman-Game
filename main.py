# Hangman
import random
import Hangman_Art

words = ["apple", "orange", "banana"]
lives = 5
chosen_word = words[random.randrange(len(words))]
print(chosen_word)

print("Find the extraction code to save your partner...\nHis life lies in ur hands...\n5 Wrong letters will hang him")

display_list = []
chosen_word_list = []
for letter in chosen_word:
    display_list.append("_ ")
    chosen_word_list.append(letter)

while chosen_word_list != display_list and lives > 0:
    print(f" ".join(display_list))
    print(Hangman_Art.hangman[lives])
    input_letter = input(f"Enter any correct letter to fill the space (You have only {lives} wrong letters left) :\n").lower()

    if input_letter in chosen_word_list and input_letter not in display_list:
        print(f"Lucky!!! {input_letter} is in the word...")
        i = 0
        for letter in chosen_word_list:
            if input_letter == letter:
                display_list[i] = chosen_word_list[i]
            i += 1

    elif input_letter in display_list:
        print(f"Hey U pressed {input_letter} agian...Y r u repeating the letters...C'mon hang him urself instead...")
        lives -= 1

    else:
        print(f"{input_letter} was a wrong letter. Ha Ha Ha.")
        lives -= 1


if display_list == chosen_word_list:
    print("Wow Genius u saved ur partner...")
else:
    print(Hangman_Art.hangman[lives])
    print("The bloodstain belongs to u...")