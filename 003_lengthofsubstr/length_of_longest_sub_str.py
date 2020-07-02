class Solution:
    def length_of_longest_sub_string(self, s: str) -> int:
        if not s:
            return 0
        max = 1
        for i, char in enumerate(s):
            char_list = [char]
            j = i+1
            while j <= len(s) - 1:
                if s[j] not in char_list:
                    char_list.append(s[j])
                else:
                    break
                j += 1
            if max < len(char_list):
                max = len(char_list)
        return max

    def length_of_longest_sub_string2(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res
