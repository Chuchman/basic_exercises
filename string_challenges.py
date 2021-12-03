# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"Последняя буква в слове: {word[-1]} .")


# Вывести количество букв "а" в слове
word = 'Архангельск'
new_word = list(word.lower())
word_sum = 0
for letter in new_word:
    if letter == 'а':
        word_sum += 1
print(f"В слове {word} {word_sum} буквы 'а'.")

    



# Вывести количество гласных букв в слове
word = 'Архангельск'
word_2 = list(word.lower())
VOWEL_WORD = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
vowel_count = 0
for letter in word_2:
    if letter in VOWEL_WORD:
        vowel_count +=1
print(f" В слове 'Архангельск' {vowel_count} гласных буквы.")




    


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split(sep = ' ')
print(f"Количество слов в предложении: {len(sentence)} .")



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(f"Первая буква каждого слова: ")
for word in sentence.split(sep = ' '):
    for letter in word.split(sep = ' '):
        print(f"\t\n{letter[0]}")




# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split(sep = ' ')
total_len = len(words)
print(f"Общая длина предложения: {total_len} .")
every_len = []
for word in words:
    every_len.append(len(word))
print(f"Сумма длин слов: {sum(every_len)} .")
average_len = sum(every_len) / total_len
print(f"Усреднёная длина слова: {int(average_len)} символа.")
    
    


