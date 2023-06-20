class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = []
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            # Convert characters to integers or use 0 if the index is out of range
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Calculate sum and carry
            digit_sum = digit_a + digit_b + carry
            carry = digit_sum // 2
            result.append(str(digit_sum % 2))

            # Decrement indices
            i -= 1
            j -= 1

        # Reverse the result and return as a string
        return ''.join(result[::-1])


# Example usage:
solution = Solution()
binary_string1 = "101010"
binary_string2 = "11011"

sum_result = solution.addBinary(binary_string1, binary_string2)
print("Sum:", sum_result)
