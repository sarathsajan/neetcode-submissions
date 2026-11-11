class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
        kv_s = {}
        kv_t = {}
        for letter in alphabet_list:
            kv_s[letter] = 0
            kv_t[letter] = 0

        for index in range(len(s)):
            if s[index] in kv_s:
                kv_s[s[index]] += 1
            if t[index] in kv_t:
                kv_t[t[index]] += 1

        for letter in alphabet_list:
            if not kv_s[letter] == kv_t[letter]:
                return False
        return True