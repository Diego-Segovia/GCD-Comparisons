from random import randint as rint

def consec_gcd(a,b):
    """
    consec_gcd computes the greatest common divisor of two
    integers using the Consecutive Interger Checking Algorithm.

    :param a: integer
    :param b: integer
    :return: gcd and iteration count
    """
    min_val = min(a,b)
    
    for x in range(min_val):
        if a % min_val == 0:
            if b % min_val == 0:
                return min_val, x+1
            else:
                min_val -= 1
        else:
            min_val -= 1


def euclid_gcd(a,b, count=0):
    """
    euclid_gcd computes the greatest common divisor
    of two integers using the Euclidean Algorithm.

    :param a: integer
    :param b: integer
    :param count: inital iteration count
    :return: gcd and iteration count
    """
    if b == 0:
        return a, count
    else:
        return euclid_gcd(b, a%b, count+1) 


def get_int_pairs():
    """
    get_int_pairs generates 100 pairs of randomly generated integers.

    :return: array of tuples of integer pairs
    """
    pair_arr = [None]*100
    
    for i in range(len(pair_arr)):
        int_pair = (rint(3000,300000), rint(3000,300000))
        pair_arr[i] = int_pair
    
    return pair_arr

# Generate integer pairs
pairs_arr = get_int_pairs()

# First pair of integers
x, y = pairs_arr[0]

# Initial max pair for Consecutive Integer Checking Algorithm
max_x_consec = x
max_y_consec = y

# Initial min pair for Consecutive Integer Checking Algorithm
min_x_consec = x
min_y_consec = y

# Initial max pair for Euclidean Algorithm
max_x_euclid = x
max_y_euclid = y

# Initial min pair for Euclidean Algorithm
min_x_euclid = x
min_y_euclid = y

# Initial max & min gcd and iteration count for Consecutive Integer Checking Algorithm
max_consec_gcd, max_consec_count = consec_gcd(max_x_consec, max_y_consec)
min_consec_gcd, min_consec_count = consec_gcd(min_x_consec, min_y_consec)

# Initial max & min gcd and iteration count for Euclidean Algorithm
max_euclid_gcd, max_euclid_count = euclid_gcd(max_x_euclid, max_y_euclid)
min_euclid_gcd, min_euclid_count = euclid_gcd(min_x_euclid, min_y_euclid)

# Total iterations for Consecutive Integer Checking Algorithm
total_iter_count_consec = max_consec_count

# Total iterations for Euclidean Algorithm
total_iter_count_euclid = max_euclid_count

for index in range(1, len(pairs_arr)):
    x, y = pairs_arr[index]

    gcd_consec, iter_count_consec = consec_gcd(x,y)
    total_iter_count_consec += iter_count_consec

    ''' Check for new max iteration count for
    Consecutive Integer Checking Algorithm '''
    if iter_count_consec > max_consec_count:
        max_consec_count = iter_count_consec
        max_consec_gcd = gcd_consec
        max_x_consec = x
        max_y_consec = y

    ''' Check for new min iteration count for
    Consecutive Integer Checking Algorithm '''
    if iter_count_consec < min_consec_count:
        min_consec_count = iter_count_consec
        min_consec_gcd = gcd_consec
        min_x_consec = x
        min_y_consec = y

    gcd_euclid, iter_count_euclid = euclid_gcd(x,y)
    total_iter_count_euclid += iter_count_euclid
    
    # Check for new max iteration count for Euclidean Algorithm
    if iter_count_euclid > max_euclid_count:
        max_euclid_count = iter_count_euclid
        max_euclid_gcd = gcd_euclid
        max_x_euclid = x
        max_y_euclid = y

    # Check for new min iteration count for Euclidean Algorithm
    if iter_count_euclid < min_euclid_count:
        min_euclid_count = iter_count_euclid
        min_euclid_gcd = gcd_euclid
        min_x_euclid = x
        min_y_euclid = y
    
# Average iterations for Consecutive Integer Checking Algorithm
consec_avg = total_iter_count_consec / len(pairs_arr)

# Average iterations for Euclidean Algorithm
euclid_avg = total_iter_count_euclid / len(pairs_arr)

# Formatted output of results
print('Consecutive Integer Checking Algorithm')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print(f'The most number of iterations used is ({max_consec_count}) for GCD({max_x_consec}, {max_y_consec}) = {max_consec_gcd}.')
print(f'The least number of iterations used is ({min_consec_count}) for GCD({min_x_consec}, {min_y_consec}) = {min_consec_gcd}.')
print(f'The average number of iterations used for all 100 pairs is ({consec_avg}).')
print()
print('Euclidean Algorithm')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print(f'The most number of iterations used is ({max_euclid_count}) for GCD({max_x_euclid}, {max_y_euclid}) = {max_euclid_gcd}.')
print(f'The least number of iterations used is ({min_euclid_count}) for GCD({min_x_euclid}, {min_y_euclid}) = {min_euclid_gcd}.')
print(f'The average number of iterations used for all 100 pairs is ({euclid_avg}).')