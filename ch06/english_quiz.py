from random import choice

print("Write the following sentence in English.")

f = open('ch06/ko_en.txt', 'r', encoding="UTF-8")

li = []
for line in f.readlines()[1:]:
    li.append(line.split('\t'))

for qna in li:
    qna[1] = qna[1].replace('\n', '')

question = choice(li)
print(question[0])

your_answer = input('\nyour answer: ')

if your_answer == question[1]:
    print('\nresult: Correct!')
else:
    print('\nresult: Not correct!')
    print('right answer:' + question[1])

print('----------------------------------------------------------------------')