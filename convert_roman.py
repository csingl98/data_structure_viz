class Solution:
    def subArraySum(self,arr, n, s): 

        #Write your code here
        
        left = 0
        right = 1
       
        while left < n - 1:
            
            sub_array = arr[left:right]
            val = 0
            val = sum(sub_array)
            
            if val == s:
                return sub_array

            if left < right and val > s:
                
                left += 1
            
            elif right < n:
                
                right += 1
                
        return None

def main():

    strings = Solution()

    print(strings.subArraySum([3, 3, 3, 2, 5], 5, 5))


if __name__ == "__main__":
    main()