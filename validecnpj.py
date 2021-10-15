import re


# def valida(cnpj):
#     if len(cnpj) == 18:
#         return True
#     else:
#         return False


def NumbersOfCNPJ(cnpj):
    numbers = re.sub(r'[^0-9]', '', cnpj)
    digits = [int(number) for number in numbers]
    return digits


def SumOfDigits(digits, sequence):
    sumDigitis = sum([x*y for x, y in zip(digits, sequence)])

    return sumDigitis


def DigitCNPJ(sum):
    value = 11 - (sum % 11)
    value = value if value <= 9 else 0
    return value


if __name__ == "__main__":
    first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    cnpj = input('Digite seu cpnj: ')

    try:
        numbers = NumbersOfCNPJ(cnpj)

        firstSum = SumOfDigits(numbers[:-2], first)

        firstDigit = DigitCNPJ(firstSum)

        if(firstDigit == numbers[-2]):
            secondSum = SumOfDigits(numbers[:-1], second)
            secondDigit = DigitCNPJ(secondSum)

            if(secondDigit == numbers[-1]):
                print('CNPJ válido!')
            else:
                print('CNPJ inválido.')
        else:
            print('CNPJ inválido.')
    except:
        print('CNPJ inválido')
