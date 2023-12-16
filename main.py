import random
import tkinter as tk

# Считывание файла
with open('words.txt', 'r', encoding='utf-8') as file:
    words = [line.rstrip() for line in file.readlines()]
# Выбор отгадываемого слова из списка
answer = random.choice(words)
guess_word = ''


# Функция проверки слова
def check_word():
    word = guess_entry.get()

    if len(word) != 5:
        guess_output.config(text='Слово должно быть из 5 букв!')
        guess_entry.config(text='')
        return None

    matches = ([], [])
    for i in range(5):
        if word[i] in answer:
            matches[0].append(word[i])
            if answer[i] == word[i]:
                matches[1].append(word[i].upper())
    if len(matches[1]) == 5:
        guess_output.config(text=f'Вы угадали слово! {answer}')
    elif len(matches[1]) != 5:
        guess_output.config(text=f'{set(matches[0])}, {matches[1]}')


window = tk.Tk()
window.geometry('400x400')
window.title('5 букв')

main_label = tk.Label(window, anchor='center', text='Добро пожаловать в игру 5 букв\nмы загадали слово\nа вам нужно его отгадать за 10 попыток')
main_label.place(x=80, y=0)


guess_label = tk.Label(window, text='Введите слово из 5 букв >')
guess_label.place(x=0, y=100)

guess_entry = tk.Entry(window, width=7)
guess_entry.place(x=150, y=100)

guess_output = tk.Label(window, text='---')
guess_output.place(x=200, y=100)

guess_button = tk.Button(window, text='Проверить', command=lambda: print(check_word()))
guess_button.place(x=150, y=150)


window.mainloop()
