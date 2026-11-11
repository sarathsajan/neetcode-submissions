class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
        kv_s = {}
        kv_t = {}
        for letter in alphabet_list:
            kv_s[letter] = 0
            kv_t[letter] = 0

        for letter in s:
            if letter in kv_s:
                kv_s[letter] += 1
                
        for letter in t:
            if letter in kv_t:
                kv_t[letter] += 1

        for letter in alphabet_list:
            if not kv_s[letter] == kv_t[letter]:
                return False
        return True