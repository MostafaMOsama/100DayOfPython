import random
# Step 1
word_list = ["mostafa", "mohamed", "osama"]
chosen_word = random.choice(word_list)

display = []
word_lenth = len(chosen_word)

for _ in chosen_word:
    display += "_"
print(display)

guess = str(input("guess a Letter : ").lower())


for position in range(word_lenth):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
