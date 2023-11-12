class Solution(object):
    def longestPalindrome(self, s:str):
        self.maxlen = 0
        self.start = 0
        
        for i in range(len(s)):
            self.expandFromCenter(s,i,i)
            self.expandFromCenter(s,i,i+1)
            
        return s[self.start:self.start+self.maxlen]
        

    def expandFromCenter(self, s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        sub_len = right-left-1
        if self.maxlen < sub_len:
            self.maxlen = sub_len
            self.start = left + 1






def main():

    strings = Solution()

    print(strings.longestPalindrome("babad"))


if __name__ == "__main__":
    main()