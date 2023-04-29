"""
Hannah Lee
CSE 163 AE

A file that contains multiple unrelated functions for
Assessment 2: Primer
"""


def total(n: int) -> int | None:
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result

# Write your functions here!


def travel(directions: str, init_coord: tuple[int, int]) -> tuple[int, int]:
    """
    Given a string of directions and a starting position (x, y),
    this function will calculate the new position after following
    the directions. The directions string will use 'N' for in. y-coord,
    'E' for inc. the x-coord, 'S' for dec. the y-coord., and 'W' for dec.
    the x-coord. Direction string is case insensitive. The function returns
    a tuple that indicates the new position after following the directions
    starting from the given x, y. The returned tuple should be in the format
    (x_new, y_new). Any characters that are not directions ('N', 'E', 'S',
    'W') will be ignored.
    """
    x, y = init_coord
    for direction in directions:
        if direction.lower() == 'n':
            y += 1
        elif direction.lower() == 'e':
            x += 1
        elif direction.lower() == 's':
            y -= 1
        elif direction.lower() == 'w':
            x -= 1
    return (x, y)


def reformat_date(date: str, origin_format: str, new_format: str) -> str:
    """
    Reformats the given date string following the formate given by the
    new format. Can assume that there is at least one digit for each part
    of the date provided. Can assume that there will be no invalid date
    formats. Returns reformatted date.
    """
    parts = date.split('/')
    old = origin_format.split('/')
    new = new_format.split('/')
    dict = {}
    index = 0
    for part in old:
        dict[part] = parts[index]
        index += 1
    new_date = ""
    length = len(new)
    count = 1
    for part in new:
        new_date += dict[part]
        if count < length:
            new_date += '/'
            count += 1
    return new_date


def longest_word(file_name: str) -> str | None:
    """
    this function returns the longest word in the given file
    as well as which line it occurs on. if there are ties
    for the longest word, it should return the one that appears
    first in the file. if the file is empty or there are no words
    in the file, the function should return None.
    """
    if len(file_name) == 0:
        return None
    max_length = 0
    max_word = ""
    max_line = 0
    with open(file_name) as f:
        for line_num, line in enumerate(f, start=1):
            for token in line.split():
                token = token.strip()
                if len(token) > max_length:
                    max_word = token
                    max_length = len(token)
                    max_line = line_num
    if max_length == 0:
        return None
    return f"{max_line}: {max_word}"


def get_average_in_range(nums: list[float], low: float, high: float) -> float:
    """
    this function returns the average of all values within the given list
    thst lies in the given range from low(inclusive) to high (exclusive).
    if there are no values in the given range, it returns 0. can assume
    low <= high.
    """
    total = 0
    count = 0
    for num in nums:
        if low <= num < high:
            total += num
            count += 1
    if count == 0:
        return 0
    average = total / count
    return average


def mode_digit(n: int) -> int:
    """
    this function returns the digit that appears most
    frequently in the given integer number. the given number may be
    positive or negative but the most frequent digit returned should
    always be non-negative. if there is a tie for the most frequent
    digit, the digit with the greatest value should be returned.
    """
    max_count = 0
    mode = 0
    count_digits = [0] * 10
    if n < 0:
        n = -n
    while n > 0:
        digit = n % 10
        count_digits[digit] += 1
        if count_digits[digit] > max_count:
            max_count = count_digits[digit]
            mode = digit
        elif count_digits[digit] == max_count and digit > mode:
            mode = digit
        n //= 10
    return mode
