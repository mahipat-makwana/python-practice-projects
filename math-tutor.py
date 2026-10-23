print('Project - Math Tutor')

from random import randrange as r
from time import time as t

no_questions = int(input("How many questions do you want?: "))
max_num = int(input("Highest number used in practice?: "))

score = 0
ans_list = []
start = t()
for question in range(no_questions):
    num1 = r(1, max_num+1)
    num2 = r(1, max_num+1)
    
    ans = num1 * num2
    your_ans = int(input(f'{num1} X {num2} = '))
    ans_list.append(f'{num1} X {num2} = {ans} || You: {your_ans}')

    if your_ans == ans:
        score += 1
    end = t()

print()
print(f'Thank you for playing! \nYou got {score} out of {no_questions} ({round(score/no_questions * 100)}%) correct in {round(end - start,2)} seconds. ({round((end-start)/no_questions,2)} seconds/question)')
print()
for a in ans_list:
    print(a)



