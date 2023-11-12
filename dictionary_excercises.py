




def main():
    #Two Sum
    input_array = [2, 7, 11, 15] 
    target = 9
    num_dict = {}

    for i in range(len(input_array)):
        num = input_array[i] 
        if num not in num_dict:
            num_dict[num] = i

        complement = target - num
        if complement in num_dict and i != num_dict[complement]:
            print([i, num_dict[complement]])
            


    return 
    input_array = [1, 7, 5, 9, 2, 12, 3] 
    K = 2
    num_set= set(input_array)
    count = 0
    #find pairs with difference K

    for num in input_array:
        if (num - K) in num_set:
            count += 1

        if (num + K) in num_set:
            count += 1
        
        num_set.discard(num)

    print(count)

    return 

    input_array = [1, 2, 2, 3, 3, 3, 4]
    num_dict = {}
    max = 0
    max_num = None

    #THIS IS O(n)
    for num in input_array:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
        
        if num_dict[num] > max:
            max = num_dict[num]
            max_num = num

    print(max_num)


    input_string = "Green Apple"
    letter_map = {}

    for letter in input_string.lower():
        #letter : count
        if letter in list(letter_map.keys()):
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    for key, value in letter_map.items():
        if value == 1:
            print("First non-repeating character: ", key)
            break

    #SETS: store non repeating characters
    letter_set = set()

    for letter in input_string.lower():
        if letter in letter_set:
            print("First repeated character: ", letter)
            break
        else:
            letter_set.add(letter)

if __name__  == '__main__':
    main()
