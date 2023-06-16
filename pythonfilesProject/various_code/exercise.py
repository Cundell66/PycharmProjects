questions = open('questions.txt', 'r')

sum_questions = [line.strip() for line in questions.readlines()]

questions.close()
score = 0
total = len(sum_questions)

for line in sum_questions:
    q, a = line.split("=")
    ans = input(f'{q}=')
    if a == ans:
        score = score + 1

result = open('result.txt', 'w')
result.write(f"Your final score is {score}/{total}.")
result.close()
