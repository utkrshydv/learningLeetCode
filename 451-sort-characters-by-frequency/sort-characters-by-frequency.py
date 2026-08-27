from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # freq = {}

        # for ch in s:
        #     if ch in freq:
        #         freq[ch] += 1
        #     else:
        #         freq[ch] = 1

        # arr = []
        # for ch in freq:
        #     arr.append([ch, freq[ch]])

        # for i in range(len(arr)):
        #     max_index = i

        #     for j in range(i+1, len(arr)):
        #         if arr[j][1]>arr[max_index][1]:
        #             max_index = j
        #     arr[i], arr[max_index] = arr[max_index], arr[i]

        # new_s=""
        # for ch, count in arr:
        #     new_s += ch*count
        # return new_s

        freq = Counter(s)

        sorted_freq = sorted(freq, key =freq.get, reverse = True)

        result = ""

        for char in sorted_freq:
            result += char*freq[char]

        return result