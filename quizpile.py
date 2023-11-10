import random

def Lotto():
    result = []

    for i in range(6):
        number = random.randint(1,45)
        if number not in result:
            result.append(number)

    result.sort()
    return result

result = Lotto()
print(f"생성된 로또 번호는 {result} 입니다.")
