from defs import *
import keyboard
import os

codes = []
count = 1000

def dislike(a):
    global code, next
    with open('dataset/train_data_0.txt', 'a') as file: file.write(f'{code},\n')
    next = True
    print('\x1b[Adisliked')
def like(a):
    global code, next
    with open('dataset/train_data_1.txt', 'a') as file: file.write(f'{code},\n')
    next = True
    print('\x1b[Aliked')

print('Генерация изображений...')
for name in os.listdir('imgs'): os.remove(f'imgs/{name}')
for n in range(count):
    img, c = get_img(lowq=True)
    codes.append(c)
    img.save(f'imgs/{n}.png')

keyboard.on_release_key('q', dislike)
keyboard.on_release_key('w', like)

print('Оценивание...')
for i in range(count):
    print(i)
    global code, next
    next = False
    code = codes[i]
    while next == False:
        pass

print('Фильтрация...')
with open('dataset/train_data_0.txt', 'r') as file: lines = list(set(file.readlines()))
with open('dataset/train_data_0.txt', 'w') as file: 
    for line in lines: file.write(line)

with open('dataset/train_data_1.txt', 'r') as file: lines = list(set(file.readlines()))
with open('dataset/train_data_1.txt', 'w') as file: 
    for line in lines: file.write(line)

print(f'Датасет создан. Новый объем: {get_size()}/{10*10*10*10*10*2*2*2*2} позиций')