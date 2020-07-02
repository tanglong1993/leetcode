from unittest import TestCase
from length_of_longest_sub_str import Solution


class TestLengthOfLongestSubStr(TestCase):
    def test_success(self):
        solution = Solution()
        s = "abcdabcdd"
        # n = solution.length_of_longest_sub_string(s)
        n = solution.length_of_longest_sub_string2(s)
        self.assertEqual(n, 4)

        s = ""
        # n = solution.length_of_longest_sub_string(s)
        n = solution.length_of_longest_sub_string2(s)
        self.assertEqual(n, 0)

        s = "aaaaaa"
        # n = solution.length_of_longest_sub_string(s)
        n = solution.length_of_longest_sub_string2(s)
        self.assertEqual(n, 1)


        
