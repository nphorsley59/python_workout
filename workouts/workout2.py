def my_sum(numbers: list[int], start: int = 0) -> int:
    """Adds initial value (start) and items in a list of integers.
    
    Args:
        numbers (list[int]): List of integers to be summed.
        start (int, optional): Initial value added to items in numbers.
    
    Returns:
        sum (int): Sum of start and items in numbers.
    
    """
    
    sum = start
    
    for y in numbers:
        sum += y
    
    return sum;


def my_mean(numbers: list[int]) -> int:
    """Calculates the mean of a list of integers.
    
    """
    
    mean = my_sum(numbers)/len(numbers)
    
    return mean;


def count_letters(words: list[str]) -> list[int]:
    """Counts the number of letters in words and returns the shortest,
    longest, and average word length.
    
    Args:
        words (list[str]): List of words (strings) to be counted.
    
    Returns:
        letter_counts (list[int]): List of integers representing the length of
            the shortest, longest, and average word in words.
    
    """
    
    len_of_words = []
    letter_counts = []
    
    for word in words:
        len_of_words.append(len(word))
    
    letter_counts.append(min(len_of_words))
    letter_counts.append(max(len_of_words))
    letter_counts.append(my_mean(len_of_words))
    
    return letter_counts;


test_words = ["Bunting", "Cardinal", "Jay", "Falcon", "Flamingo"]
print(count_letters(test_words))