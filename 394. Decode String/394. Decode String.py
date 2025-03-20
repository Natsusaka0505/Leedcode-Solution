class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            # if encounter ']'
            if ch == "]":
                encode = ""
                # pop content
                while stack[-1] != "[":
                    encode += stack.pop()
                # reverse
                encode = list(encode[::-1])
                # pop '['
                stack.pop()
                times = ""
                # pop number of times
                while stack and stack[-1].isdigit():
                    times += stack.pop()
                # reverse
                times = int(times[::-1])
                # extend to stack
                stack.extend(encode * times)
            else:
                stack.append(ch)

        return "".join(stack)


sol = Solution()
s = "3[a]2[bc]"
# s = "3[a2[c]]"
# s = "2[abc]3[cd]ef"
print(sol.decodeString(s))
