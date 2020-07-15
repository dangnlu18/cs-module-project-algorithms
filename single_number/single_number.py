'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #create char map to count number of times char appears in array
    char_map = {}
    for val in arr:
        if val in char_map:
            char_map[val] +=1
        else:
            char_map[val] =1
    
    for key in char_map:
        if char_map[key] ==1:
            return key

single_number([1,2,3,4,4,3,2])

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")