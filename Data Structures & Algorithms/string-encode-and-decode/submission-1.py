class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([s +  '\n' for s in strs])

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s[:-1].split('\n')