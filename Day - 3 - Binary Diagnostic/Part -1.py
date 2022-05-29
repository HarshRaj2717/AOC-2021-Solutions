from input import input_text


def main():
    gamma = ''
    epsilon = ''
    for i in range(len(input_text[0])):
        list1 = []

        for j in range(len(input_text)-1):
            list1.append(input_text[j][i])

        if list1.count('0') > list1.count('1'):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(int(gamma, 2)*int(epsilon, 2))


if __name__ == "__main__":
    main()
