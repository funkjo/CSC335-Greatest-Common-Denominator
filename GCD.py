#
# John Funk
#
# CSC 335-01
#
# 3 Feb 2020
#

from random import randrange


# Generator 100 pairs of random integers
def rand_pair_generator():
    pairs = []
    for i in range(100):
        n = randrange(5000, 50001)
        m = randrange(5000, 50001)
        pair = (n, m)
        pairs.append(pair)

    return pairs


# consecutive integer checking algorithm
def consecutive_integer_checking(n, m):

    # determine the smaller and larger value from the input integers
    if m <= n:
        min = m
        max = n
    else:
        min = n
        max = m

    # return the larger value if the smaller value is 0
    if min == 0:
        return max

    # check each integer to see if it is the GCD
    # if it is not, decrease by one and check the next integer
    count = 0
    i = min
    while i >= 0:
        count += 1
        if m % i == 0:
            if n % i == 0:
                gcd = i
                break
        i -= 1

    return gcd, count, n, m


# euclid's algorithm
def euclids_algorithm(n, m, _n, _m, count):
    count += 1

    # determine the smaller and larger value from the input integers
    if m < n:
        min = m
        max = n
    else:
        min = n
        max = m

    # return the larger value if the smaller value is 0
    if min == 0:
        return max, count, _n, _m
    else:
        return euclids_algorithm(min, max % min, _n, _m, count)


# run the consecutive integer checking algorithm
def test_consecutive_integer_checking(pairs):
    most_iterations = (0, 0, 0, 0)
    least_iterations = (0, 0, 0, 0)
    avg = 0
    for x in pairs:
        result = consecutive_integer_checking(x[0], x[1])
        if result[1] >= most_iterations[1]:
            most_iterations = result
            if avg == 0:
                least_iterations = most_iterations
                avg = avg + result[1]
                continue
        if result[1] <= least_iterations[1]:
            least_iterations = result

        avg = avg + result[1]
    print("Consecutive Integer Checking Algorithm:")
    print("The most number of iterations used is [" +
          str(most_iterations[1]) + "] for GCD(" +
          str(most_iterations[2]) + ", " +
          str(most_iterations[3]) + ") = " +
          str(most_iterations[0]))
    print("The least number of iterations used is [" +
          str(least_iterations[1]) + "] for GCD(" +
          str(least_iterations[2]) + ", " +
          str(least_iterations[3]) + ") = " +
          str(least_iterations[0]))
    print("The average number of iterations for all 100 pairs is [" + str(avg/100) + "]")


# run euclid's algorithm
def test_euclids_algorithm(pairs):
    most_iterations = (0, 0, 0, 0)
    least_iterations = (0, 0, 0, 0)
    avg = 0
    for x in pairs:
        result = euclids_algorithm(x[0], x[1], x[0], x[1], 0)
        if result[1] >= most_iterations[1]:
            most_iterations = result
            if avg == 0:
                least_iterations = most_iterations
                avg = avg + result[1]
                continue
        if result[1] <= least_iterations[1]:
            least_iterations = result

        avg = avg + result[1]
    print("Euclid's Algorithm:")
    print("The most number of iterations used is [" +
          str(most_iterations[1]) + "] for GCD(" +
          str(most_iterations[2]) + ", " +
          str(most_iterations[3]) + ") = " +
          str(most_iterations[0]))
    print("The least number of iterations used is [" +
          str(least_iterations[1]) + "] for GCD(" +
          str(least_iterations[2]) + ", " +
          str(least_iterations[3]) + ") = " +
          str(least_iterations[0]))
    print("The average number of iterations for all 100 pairs is [" + str(avg/100) + "]")


def main():
    integer_pairs = rand_pair_generator()
    test_consecutive_integer_checking(integer_pairs)
    print("\n")
    test_euclids_algorithm(integer_pairs)


if __name__ == '__main__':
    main()

