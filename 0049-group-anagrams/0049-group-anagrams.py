class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dic = {}
        for i in strs:
            key = ''.join(sorted(i))
            sorted_dic[key] = sorted_dic.get(key,[])+ [i]
        return list(sorted_dic.values())
        