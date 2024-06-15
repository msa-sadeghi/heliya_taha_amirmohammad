def sum_(*args):
    res = 0
    for number in args:
        res += number
    return res

print(sum_(12, 14, 16,18,19,45))
print(sum_())
print(sum_(1))