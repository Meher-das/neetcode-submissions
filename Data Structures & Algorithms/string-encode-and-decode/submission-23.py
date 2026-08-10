class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            if len(string) >= 100:
                string_len = "00" + str(len(string))
            elif len(string) < 10 :
                string_len = "0" + str(len(string))
            else:
                string_len = str(len(string))

            encoded_str = encoded_str + string + string_len + "~"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        answer = []
        for i in range(len(s)):
            if s[i] == "~":
                string_len = int(s[i-3:i])
                answer.append(s[i-3-string_len:i-3])
        return answer

