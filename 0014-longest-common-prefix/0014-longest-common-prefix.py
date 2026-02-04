class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for i in range(1,len(strs)):
            current_pre = strs[i]

            while not current_pre.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix