#!/usr/bin/env python3
from random import randint, choice

wordlist = "wordlist.txt"

baseword = "vaapukkamehu"
baseword_len = len(baseword)

a_count = baseword.count("a")
e_count = baseword.count("e")
a_leet = "4"
e_leet = "3"

# brutal hardcode
a_indexes_in_baseword = [1,2,7]
e_index_in_baseword = baseword.index("e")

# set default 
mutation_amount = 50

# store mutated words here
mutations = []
mutations.append(baseword)
mutations.append(baseword.upper())

try:
    mutation_amount = int(input("How many mutations do you want to create from {}? ".format(baseword)))
except ValueError:
    print("You failed at inputting an integer. Using default of {}".format(mutation_amount))

print("\n-----Starting mutator to create {} mutations-------\n".format(mutation_amount))

while len(mutations) <= mutation_amount:
    # generate random amounts of uppercase and leetspeak
    amount_of_uppercase_letters = randint(0, baseword_len)
    amount_of_leet_a = randint(0, a_count)
    amount_of_leet_e = randint(0, e_count)

    #print("amount of uppercase letters: " + str(amount_of_uppercase_letters))
    uppercase_indexes = []
    for i in range(amount_of_uppercase_letters):
        uppercase_indexes.append(randint(0, baseword_len))

    leet_a_indexes = []
    if amount_of_leet_a == 3:
        leet_a_indexes = a_indexes_in_baseword
    else:
        for i in range(amount_of_leet_a):
            leet_a_indexes.append(choice(a_indexes_in_baseword))

    mutated_word = baseword
    # uppercase conversions
    for index in uppercase_indexes:
        if index < baseword_len:
            mutated_word = mutated_word[:index] + mutated_word[index].upper() + mutated_word[index+1:]
        else:
            mutated_word = mutated_word[:index-1] + mutated_word[index-1].upper()
    # leetspeak conversions
    if amount_of_leet_e:
        mutated_word = mutated_word[:e_index_in_baseword] + e_leet + mutated_word[e_index_in_baseword+1:]
    
    for letter in leet_a_indexes:
        mutated_word = mutated_word[:letter] + a_leet + mutated_word[letter+1:]
    # check that created string is of right length
    if len(mutated_word) != baseword_len:
        print("ERROR OCCURRED!!!!!!!!!!!!!!!!!! SEE REFERENCE BELOW")
        print(baseword)
        print(mutated_word)
    mutations.append(mutated_word)

# write mutations into a text file
# one mutation per line
with open(wordlist, 'w') as file:
    for mutation in mutations:
        file.write(mutation)
        file.write('\n')

print("\n-----------Mutator done!------------")
print("Mutations stored to {}".format(wordlist))
