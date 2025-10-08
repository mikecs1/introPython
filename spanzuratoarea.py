cuvant = 't r i u n g h i u l a r'
        # t r _ _ _ _ _ _ _ _ _ r
        # 5 incercari

# word = 'triunghiular'
word = 'paralelipipedic'
start_letter = word[0]
end_letter = word[-1]
display_word = ''
tried_char = []
for i in word:
    if i != start_letter and i != end_letter:
        i = '_'
    else:
        tried_char.append(i)
    display_word += i
attempts = 5
tried_char = list(set(tried_char))

while attempts > 0:
    print(f'Cuvantul este: {display_word}. Mai aveti {attempts} incercari!')
    letter = input('Va rugam sa introduceti litera: ').lower()
    if len(letter) != 1:
        print('Va rugam introduceti doar o litera odata!')
        continue
    elif not letter.isalpha():
        print('Va rugam introduceti doar litere!')
        continue
    if letter in word.lower():
        if letter in tried_char:
            print(f'Ati mai incercat aceasta litera! Pana acum ati incercat {tried_char}')
        for index, character in enumerate(word.lower()):
            if character == letter:
                if letter not in tried_char:
                    tried_char.append(letter)
                display_word = display_word[:index] + letter + display_word[index+1:]
    else:
        if letter not in tried_char:
            tried_char.append(letter)
            attempts -= 1
            if attempts < 1:
                print(f'Ati pierdut!. Nu mai aveti incercari! Cuvantul cautat era "{word}"')
        else:
            print(f'Ati mai incercat aceasta litera! Pana acum literele incercate sunt {tried_char} ')
    # if not "_" in display_word:
    if word == display_word:
        print(f'Felicitari! Ati castigat! Cuvantul gasit este "{word}" ')
        break
