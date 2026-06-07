class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i]) * int(num2[j])
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] = (res[i+j] % 10)           
        res, zeros = res[::-1], 0
        while zeros < len(res) and res[zeros] == 0:
            zeros += 1
        return "".join([str(x) for x in res[zeros:]])