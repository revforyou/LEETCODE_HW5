class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a dynamic programming array to store whether each substring can be segmented
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: Empty string can always be segmented

        # Iterate backwards through the string to build the dp array
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Check if the substring from i to i + len(w) matches any word in the dictionary
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]  # Update dp[i] if the substring can be segmented
                if dp[i]:
                    break  # Break if the current substring can be segmented to avoid unnecessary iterations

        return dp[0]  # Return whether the entire string can be segmented
