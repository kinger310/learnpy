def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    if digits == "":
        return []

    nums_to_letters = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    combs = [""]
    for digit in digits:
        new_combs = []
        for comb in combs:
            for letter in nums_to_letters[int(digit)]:
                new_combs.append(comb + letter)
        combs = new_combs

    return combs

print(letterCombinations("324"))
