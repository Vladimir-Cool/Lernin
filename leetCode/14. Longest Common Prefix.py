from typing import List


def prefix_check(word1: str, word2: str) -> str:
    len1 = len(word1)
    len2 = len(word2)
    len_iter = min(len1, len2)
    prefix = ""

    for i in range(len_iter):
        if word1[i] == word2[i]:
            prefix += word1[i]
        else:
            break
    return prefix


def longestCommonPrefix(strs: List[str]) -> str:
    max_prefix = strs[0]
    len_list = len(strs)

    for i in range(len_list - 1):
        max_prefix = prefix_check(max_prefix, strs[i + 1])

    if max_prefix:
        return max_prefix
    return ""


strs = ["flower", "flow", "flight"]

end = longestCommonPrefix(strs)
print(end)


class Solution:
    """Лучше решение"""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        lst = list(zip(*strs))
        for i in lst:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix
