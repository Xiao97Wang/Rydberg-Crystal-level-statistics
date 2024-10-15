#!/usr/bin/env python
# coding: utf-8

# 0 denotes g state, 1 denotes e state

from itertools import product

def calculate_f(binary_string, epsilon, U):
    # Count the number of '1's in the string
    num_ones = binary_string.count('1')
    
    # Count the number of adjacent same-value pairs ('00' or '11')
    num_adjacent_pairs = sum(binary_string[i] == binary_string[i+1] for i in range(len(binary_string) - 1))
    
    # Compute the function value
    f_value = epsilon * num_ones + U * num_adjacent_pairs
    
    return f_value

def generate_binary_numbers(L):
    # Generate all binary numbers of length L
    return [''.join(bits) for bits in product('01', repeat=L)]

def flip_bit(binary_string, index):
    # Flip the bit at the given index
    flipped = list(binary_string)
    flipped[index] = '1' if binary_string[index] == '0' else '0'
    return ''.join(flipped)

def find_local_minima(binary_numbers, epsilon, U):
    local_minima = []
    
    for binary_string in binary_numbers:
        # Calculate f_value for the original binary number
        original_f = calculate_f(binary_string, epsilon, U)
        
        # Calculate f_values for all neighbours (binary numbers with one bit flipped)
        neighbour_f_values = []
        for i in range(len(binary_string)):
            flipped_string = flip_bit(binary_string, i)
            neighbour_f_values.append(calculate_f(flipped_string, epsilon, U))
        
        # Check if the original binary number has the smallest f_value
        if original_f < min(neighbour_f_values):
            local_minima.append((binary_string, original_f))
    
    return local_minima


# the following commented part provides the details of the meta-stable states for a given L
# Parameters
#L = 5
#epsilon = 1  # Define epsilon
#U = 1.1        # Define U

# Generate all binary numbers of length L
#binary_numbers = generate_binary_numbers(L)

# Find local minima
#local_minima = find_local_minima(binary_numbers, epsilon, U)

# Output the local minima and their f_values
#print("Local minima (binary string, f_value):")
#for binary_string, f_value in local_minima:
#    print(f"{binary_string} -> f_value: {f_value}")

# the number of local minima (exclude the global minima)
#len(local_minima)-( 2 - (L % 2) )





epsilon = 1  # Define epsilon
U = 1.1        # Define U

for L in range(1, 40):  # Loop from 1 to 10 (inclusive)

    # Generate all binary numbers of length L
    binary_numbers = generate_binary_numbers(L)

    # Find local minima
    local_minima = find_local_minima(binary_numbers, epsilon, U)

    # the number of local minima (exclude the global minima)
    N_loc_min = len(local_minima)-( 2 - (L % 2) )
    
    print(L, N_loc_min    , N_loc_min **(1/L)  )


