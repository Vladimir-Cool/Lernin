def isValid(s: str) -> bool:
    check_stac = []

    char_group = {
        "[": "]",
        "{": "}",
        "(": ")",
    }

    for char in s:
        if char in ["[", "{", "("]:
            check_stac.append(char)
        elif char in ["]", "}", ")"]:
            if check_stac and char == char_group[check_stac[-1]]:
                check_stac.pop()
            else:
                return False

    if check_stac:
        return False
    return True


print(isValid("( ) {}}}"))
