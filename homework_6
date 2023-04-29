import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line
import csv
import random
import matplotlib.pyplot as plt


def ones_and_tens_digit_histogram(numbers):
    '''
    Input:
        a list of numbers.
    Returns:
        a list where the value at index i is the frequency in which digit i
        appeared in the ones place OR the tens place in the input list. This
        returned list will always have 10 numbers (representing the frequency
        of digits 0 - 9).

    For example, given the input list
        [127, 426, 28, 9, 90]
    This function will return
        [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]

    That is, the digit 0 occurred in 20% of the one and tens places; 2 in 30%
    of them; 6, 7, and 8 each in 10% of the ones and tens, and 9 occurred in
    20% of the ones and tens.

    See fraud_detection_tests.py for additional cases.
    '''
    histogram = [0] * 10

    # first fill histogram with counts
    for i in numbers:
        # 1's place
        histogram[i % 10] += 1

        # 10's place
        histogram[i // 10 % 10] += 1

    # normalize over total counts
    for i in range(len(histogram)):
        histogram[i] /= len(numbers) * 2

    return histogram

# Your Set of Functions for this assignment goes in here


def extract_election_votes(filename, column_names):
    '''
    This function takes as input the name of the file that the method will
    look through for data as well as a list of column names the method will
    return a list of integers that contains the values in those columns
    from every row (the order of the integers does not matter).

    Input:
        filename: the name of the file where the method will read data from
        column_names: a list of specific column names the code will check and
        extract data from.

    Returns:
        vote_counts: a list of integers that contains the vaules in the columns
        specified by column_names from every row.
    '''
    vote_counts = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            for col in column_names:
                vote_counts.append(
                    int(row[col].replace(',', '').replace('"', '')))
    return vote_counts


def plot_iran_least_digits_histogram(histogram):
    '''
    This function takes as input the output of ones_and_tens_digit_histogram()
    and plots a bar chart of the percentage of times each digit (0-9) appears
    in the least significant digits of the vote counts.

    Input:
        histogram: a list of length 10 where the value at index i is the
            frequency in which digit i appeared in the ones place OR the tens
            place in the input list. This returned list will always have 10
            numbers (representing the frequency of digits 0 - 9).

    Returns:
        None
    '''
    digits = [0] * 10
    for i in range(10):
        digits[i] = i
    ideal_val = [0] * 10
    for j in range(10):
        ideal_val[j] = 0.1
    # plot ones and tens place values separately
    plt.plot(digits, ideal_val, label='ideal')
    plt.plot(digits, histogram, label='iran')

    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.title('Distribution of the last two digits in Iranian dataset')
    plt.savefig('iran-digits.png')
    plt.legend()

    plt.show()


def plot_dist_by_sample_size():
    '''
    This function creates five different collections (sizes 10, 50, 100,
    1000 and 10,000) of random numbers where every element in the collection
    is a different random number x such that 0 <= x < 100,plots the digit
    histograms for each of those collections on one graph saves the plot as
    random-digits.png and returns nothing.

    Input:
        None

    Returns:
        None
    '''
    digits = [0] * 10
    for i in range(10):
        digits[i] = i
    ideal_val = [0] * 10
    for j in range(10):
        ideal_val[j] = 0.1

    # Plot histograms
    plt.plot(digits, ideal_val, label='ideal')

    rand_ten = [0] * 10

    for i in range(10):
        rand_ten[i] = random.randint(0, 100)
    ten_histogram = ones_and_tens_digit_histogram(rand_ten)
    rand_fifty = [0] * 50
    for i in range(50):
        rand_fifty[i] = random.randint(0, 100)
    fifty_histogram = ones_and_tens_digit_histogram(rand_fifty)
    rand_hund = [0] * 100
    for i in range(100):
        rand_hund[i] = random.randint(0, 100)
    hund_histogram = ones_and_tens_digit_histogram(rand_hund)
    rand_thous = [0] * 1000
    for i in range(1000):
        rand_thous[i] = random.randint(0, 100)
    thous_histogram = ones_and_tens_digit_histogram(rand_thous)
    rand_tenthous = [0] * 10000
    for i in range(10000):
        rand_tenthous[i] = random.randint(0, 100)
    tenthous_histogram = ones_and_tens_digit_histogram(rand_tenthous)
    plt.plot(digits, ten_histogram, label='10 random numbers')
    plt.plot(digits, fifty_histogram, label='50 random numbers')
    plt.plot(digits, hund_histogram, label='100 random numbers')
    plt.plot(digits, thous_histogram, label='1000 random numbers')
    plt.plot(digits, tenthous_histogram,
             label='10000 random numbers')
    plt.legend()

    # Set title and labels
    plt.title('Distribution of last two digits in randomly generated samples')
    plt.xlabel('Digit')
    plt.ylabel('Frequency')

    # Save plot
    plt.savefig('random-digits.png')
    plt.legend()
    plt.show()


def mean_squared_error(numbers1, numbers2):
    '''
    This function finds and returns the mean squared error for two lists of
    numbers. This code is under the assumption that the two lists are of
    equal length.

    Input:
        numbers1: a list of numbers
        numbers2: a list of numbers

    Returns:
        mse: the mean squared error between numbers1 and numbers2
    '''
    n = len(numbers1)
    squared_differences = [(numbers1[i] - numbers2[i])**2 for i in range(n)]
    mse = sum(squared_differences)/n
    return mse


def calculate_mse_with_uniform(histogram):
    '''
    This function takes a histogram (as created by ones_and_tens_digit_
    histogram) and returns the mean squared error of the given histogram
    with the uniform distribution

    Input:
        histogram: the histogram created by ones_and_tens_digit_histogram

    Returns:
        mse: the mean squared error of the given histogram with the uniform
        (ideal) distribution
    '''
    n = sum(histogram)
    expected_frequency = n / len(histogram)
    mse = sum([(v - expected_frequency) **
               2 for v in histogram]) / len(histogram)

    return mse


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    '''
    This function takes two inputs: the Iranian MSE (as computed by
    calculate_mse_with_uniform()) and the number of data points in the
    Iranian dataset, builds 10,000 groups of random numbers, where each number
    x is randomly generated such that 0 <= x < 100, and each group is the same
    size as the Iranian election data,computes the MSE with the uniform
    distribution for each of these groups,compares the 10,000 MSEs to the
    Iranian MSE by determining and printing how many of the 10,000 random MSEs
    are larger than or equal to the Iran MSE, how many of the 10,000 random
    MSEs are smaller than the Iran MSE, and the Iranian election null
    hypothesis rejection level.

    Input:
        iran_mse: the iranian mse as computed by calculate_mse_with_uniform()
        number_of_iran_datapoints: the number of data points in the Iranian
        dataset.
    '''
    samples = 10000
    low_mses = 0
    high_mses = 0
    for i in range(samples):
        random_mse = []
        for j in range(number_of_iran_datapoints):
            val = random.randint(0, 99)
            random_mse.append(val)

        hist = ones_and_tens_digit_histogram(random_mse)
        mse_val = calculate_mse_with_uniform(hist)

        if mse_val >= iran_mse:
            high_mses += 1
        else:
            low_mses += 1

    null_hypothesis_rejection_level = high_mses / samples

    print("2009 Iranian election MSE:", iran_mse)
    print("Quantity of MSEs larger than or equal to the 2009 "
          "Iranian election MSE:", high_mses)
    print("Quantity of MSEs smaller than the 2009 Iranian election MSE:",
          low_mses)
    print("2009 Iranian election null hypothesis rejection level p:",
          null_hypothesis_rejection_level)


def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    file_name = "election-iran-2009.csv"
    column_names = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    numbers = extract_election_votes(file_name, column_names)
    histogram = ones_and_tens_digit_histogram(numbers)
    iran_mse = calculate_mse_with_uniform(histogram)
    plot_iran_least_digits_histogram(histogram)
    plot_dist_by_sample_size()
    compare_iran_mse_to_samples(iran_mse, len(numbers))


if __name__ == "__main__":
    main()
