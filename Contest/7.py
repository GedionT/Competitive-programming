
def romanToInteger(roman) -> int:
    #  Given a Roman number, change to its corresponding integer value
    #  Input: "XXI"
    #  Output: 21

    #  Create a dictionary to map Roman numerals to their integer values
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i in range(1, len(roman)):
        if roman_dict[roman[i-1]] < roman_dict[roman[i]]:
            total -= roman_dict[roman[i-1]]
        else:
            total += roman_dict[roman[i-1]]

    total += roman_dict[roman[-1]]

    return total


if __name__ == '__main__':
    print(romanToInteger("XXI"))
