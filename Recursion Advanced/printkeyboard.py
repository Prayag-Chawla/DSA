def get_phone_keypad_combinations(n):
    keypad_mapping = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }

    def backtrack(current_digit_index, current_combination):
        if current_digit_index == len(n):
            combinations.append(current_combination)
            return

        current_digit = n[current_digit_index]
        if current_digit not in keypad_mapping:
            return

        letters = keypad_mapping[current_digit]
        for letter in letters:
            backtrack(current_digit_index + 1, current_combination + letter)

    combinations = []
    backtrack(0, "")
    return combinations


n = "23"
result = get_phone_keypad_combinations(n)
print(result)
