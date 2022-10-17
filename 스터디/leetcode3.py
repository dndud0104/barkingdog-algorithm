from collections import deque

def lengthOfLongestSubstring(s):
    maxleng = len(set(s))
    substring = deque([])
    tmpleng = 0

    for a in s:
        if not a in substring:
            substring.append(a)
        elif a in substring:
            tmpleng = max(len(substring),tmpleng)
            while True:
                if substring[0]!= a:
                    substring.popleft()
                elif substring[0] == a:
                    substring.popleft()
                    break
            substring.append(a)
        if len(substring) == maxleng:
            return maxleng
    tmpleng = max(len(substring),tmpleng)
    return tmpleng





s = "ohvhjdml"
print(lengthOfLongestSubstring(s))
