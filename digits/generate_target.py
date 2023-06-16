import random


def generate_numbers():
    generated_numbers = []
    cnt = 1
    while cnt < 7:
        low_number = random.randint(0, 10) + 1
        if low_number not in generated_numbers:
            generated_numbers.append(low_number)
            cnt += 1
        mid_number = random.randint(10, 30) + 1
        if mid_number not in generated_numbers:
            generated_numbers.append(mid_number)
            cnt += 1
        high_number = random.randint(10, 30) + 1
        if high_number not in generated_numbers:
            generated_numbers.append(high_number)
            cnt += 1
    print(f'Using {sorted(generated_numbers)} make')
    return generated_numbers


operations = ['+', '-', '*', '/']
numbers = generate_numbers()


def calc(count, numbers, expressions):
    result = 0
    express = 0
    # print(length)
    for _ in range(1, 6):
        length = len(numbers)
        right_index = int(random.random() * (length-1))
        left_index = int(length-1)
        if left_index != right_index:
            right = str(numbers[right_index])
            left = str(numbers[left_index])
            operation = operations[int(random.random() * 4)]
            expression = right+operation+left
            result = eval(expression)
            if result < 0:
                expression = left+operation+right
                result = eval(expression)
            if result == int(result):
                if result != numbers[right_index] or numbers[left_index]:
                    expressions.append(expression)
                    numbers.pop(right_index)
                    numbers.pop(left_index-1)
                    numbers.append(int(result))
                    express += 1
                    if result > 500:
                        print(result)
                        return result
                else:
                    calc(count, numbers, expressions)
            else:
                numbers = numbers[::-1]
                calc(count, numbers, expressions)
        else:
            calc(count, numbers, expressions)

    print(result)
    return result


def run(num):
    c = 0
    expressions = []
    for c in range(5):
        calc(c, num, expressions)

    solution_prompt = input(f'enter s to see a solution ')
    if solution_prompt == 's':
        print(f'solution: {expressions}')
    return


run(numbers)
