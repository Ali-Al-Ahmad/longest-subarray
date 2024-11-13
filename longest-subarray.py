"an algorithm to find the longest subarray with equal number of 1s and 0s"

array = [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

LENGTH_OF_ARRAY = len(array)
LONGEST_STARTING_INDEX = 0
LONGEST_ENDING_INDEX = 0
MAXIMUM_COUNTER = 0

for i in range(LENGTH_OF_ARRAY):
    ZEROS_COUNTER = 0
    ONES_COUNTER = 0

    for j in range(i, LENGTH_OF_ARRAY):

        if array[j] == 0:
            ZEROS_COUNTER += 1

        if array[j] == 1:
            ONES_COUNTER += 1

        # reassign the starting and ending indices when length of subarray greater than previous
        if ZEROS_COUNTER == ONES_COUNTER and ZEROS_COUNTER > MAXIMUM_COUNTER:
            LONGEST_STARTING_INDEX = i
            LONGEST_ENDING_INDEX = j
            MAXIMUM_COUNTER = ZEROS_COUNTER

print(f"""starting index: {LONGEST_STARTING_INDEX}
ending index: {LONGEST_ENDING_INDEX}""")
print(f"length of the subbarray is: {LONGEST_ENDING_INDEX-LONGEST_STARTING_INDEX+1}")
