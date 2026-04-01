class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result


    def decode(self, encoded: str) -> List[str]:
        i = 0

        result = []

        while i < len(encoded):
            prefix_length_str = ""
            while encoded[i] != "#":
                prefix_length_str += encoded[i]
                i += 1

            prefix_length = int(prefix_length_str)
            i += 1
            part = encoded[i : i + prefix_length]

            result.append(part)
            i += prefix_length

        return result

