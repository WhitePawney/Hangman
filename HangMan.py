import random


def list_to_str(list):
    a = ""
    for element in list:
        a = a + element
    return a

def file_to_list(file):
    list_of_word = []
    for element in file:
        stripped_line = element.strip()
        line_list = stripped_line.split()
        list_of_word.append(line_list)
    return list_of_word


def draw_gallow(tries):
    u = 1
    if tries == u:
        print("---------")
        print("|       |")
        print("|")
        print("|")
        print("|")
        print("|")
    u = u + 1

    if tries == u:
        print("---------")
        print("|       |")
        print("|       @")
        print("|")
        print("|")
        print("|")
    u = u + 1

    if tries == u:
        print("---------")
        print("|       |")
        print("|       @")
        print("|    <--|-->")
        print("|")
        print("|")
    u = u + 1

    if tries == u:
        print("---------")
        print("|       |")
        print("|       @")
        print("|    <--|-->")
        print("|       |   ")
        print("|")
    u = u + 1

    if tries == u:
        print("---------")
        print("|       |")
        print("|       @")
        print("|    <--|-->")
        print("|       |")
        print("|      //")
    u = u + 1
    if tries == u:
        print("---------")
        print("|       |")
        print("|       X")
        print("|    XXX|XXX")
        print("|       X")
        print("|      XX")

word_list = open('word_list.txt', 'r')
list_of_words = file_to_list(word_list)
word_list.close()

random_word = random.choice(list_of_words)
random_word = list_to_str(random_word)
print("WELCOME TO HANGMAN!\n You have 6 tries! If you fail 6 times, you lose! GOOD LUCK")
print("The word you have to guess is: ")
#print(random_word)
#print(type(random_word))
guessed = random_word[0] + "_" * (len(random_word) - 2) + random_word[len(random_word) - 1]
guessed = list(guessed)
#print(guessed)
#print(type(guessed))
x = list_to_str(guessed)
print(x)


player_input = input("Guess your letter: ")
player_input = player_input.upper()

lstGuessed = []

tries = 1

while True:

    if (player_input in random_word) and (player_input not in lstGuessed):
        indices = [index for index, element in enumerate(random_word) if element == player_input]
        #print(indices)
        for element in range(len(guessed)):
            for element_2 in indices:
                if element == element_2:
                    guessed[element] = player_input
        lstGuessed.append(player_input)
        x = list_to_str(guessed)
        print(x)
        draw_gallow(tries)

    elif (player_input in random_word) and (player_input in lstGuessed):
        print("You already guessed that")
        x = list_to_str(guessed)
        print(x)
        draw_gallow(tries)

    elif (player_input not in random_word) and (player_input not in lstGuessed):
        lstGuessed.append(player_input)
        tries = tries + 1
        print("Wrong letter. Please try again!")
        x = list_to_str(guessed)
        print(x)
        print("Tries: ", tries)
        draw_gallow(tries)

    elif (player_input not in random_word) and (player_input in lstGuessed):
        print("You already tried that!! Guess the letter: ")

    if "_" not in guessed:
        print("Congrats! You guessed the word!!")
        break

    if tries == 6:
        print("YOU LOST!! muahahahah")
        draw_gallow(tries)
        break

    player_input = input("Guess the letter: ")
    player_input = player_input.upper()


#print(guessed)
#print(lstGuessed)










