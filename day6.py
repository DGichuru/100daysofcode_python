import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
word_length = len(chosen_word)
n = 0

while n < word_length:
    display.append("_")
    n += 1


#print(display)
end_of_game = False
while not end_of_game:


    guess = input("Guess a letter from my word: \n").lower()
    """if guess in chosen_word:
        x = chosen_word.index(guess)"""
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    """ 
if guess in chosen_word:
    display.insert(x, guess)"""
   

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")


    