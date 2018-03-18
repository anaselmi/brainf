from memory import memory

def linter(code):
    valid_char = ["+", "-", ">", "<", ".", ",", "[", "]"]
    valid_code = []
    left_bracket_count = 0
    right_bracket_count = 0
    bracket_index = []
    
    #Loop cleans input of non valid characters, appends it to a list, and raises an error if we have mismatched brackets
    for i, char in enumerate(code):
        if char not in valid_char:
            continue
        else:
            valid_code.append(char)
            if char == "[":
                left_bracket_count += 1
            if char == "]":
                right_bracket_count += 1
    
    if left_bracket_count != right_bracket_count:
        raise Exception("Mismatched brackets.")

    #Second loop goes through valid_code and pairs right brackets with left brackets
    for i, char in enumerate(valid_code):
        if char == "[":
                bracket_index.append(i)
        if char == "]":
                valid_code[i] = bracket_index.pop()
                

    
    return(valid_code)


if __name__ == "__main__":
    test_string = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>[+++++++++++++++.>.+++.-----]-.--------.<<+.<."
    test_string_brackets = "+++[++[++]+]+[++[++]++[++]++]"
    test_string_altered = "flameon++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.<<+.<."
    test_string_bracket_error = "++++[[++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.<<+.<."
    print(linter(test_string_brackets))
