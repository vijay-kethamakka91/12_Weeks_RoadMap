import random


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return int(num1 / num2)


op_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def main():
    name = input("Please tell us your name: ").split(' ')
    name = " ".join(_.title() for _ in name)
    print(f"Hi {name}! Welcome to the math quiz.")
    print(f"{name}, can you answer the following questions?")
    score = start_quiz()
    print(f"Congratulations {name}, on scoring {score} out of 5")


def start_quiz():
    score = 0
    for _ in range(5):
        (que, num1, num2, op) = generate_question()
        user_answer = int(input(que))
        score += 1 if validate_answer(user_answer, num1, num2, op) else score
    return score


def generate_question():
    num1 = random.randint(1, 21)
    num2 = random.randint(1, 21)
    op = random.choice(list(op_dict.keys()))
    return f"What is {num1} {op} {num2}? ", num1, num2, op


def validate_answer(user_ans, num1, num2, op):
    return user_ans == op_dict[op](num1, num2)


main()
