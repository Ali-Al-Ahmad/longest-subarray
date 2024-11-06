array = [0,0,1,1,0,0,1,0,0,1,0,0,1]

length_of_array = len(array)
longest_starting_index = 0
longest_ending_index = 0
maximum_counter = 0

for i in range(length_of_array):
    zeros_counter=0
    ones_counter=0
    
    for j in range(i,length_of_array):
        
        if array[j] == 0:
            zeros_counter+=1
            
        if array[j] == 1:
            ones_counter+=1
            
        # reassign the starting and ending indices when length of subarray greater than previous
        if zeros_counter == ones_counter and zeros_counter > maximum_counter:
            longest_starting_index = i
            longest_ending_index = j
            maximum_counter = zeros_counter
            
print(f"start:{longest_starting_index} end:{longest_ending_index}")
print(f"length of the subbarray is: {longest_ending_index-longest_starting_index+1}")
        
        
        