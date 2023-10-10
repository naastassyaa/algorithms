def quick_sort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))
    return quick_sort(left) + center + quick_sort(right)


def find_sum(s, sum_to_find):
    s = quick_sort(s)

    for i in range(len(s) - 2):
        left = i + 1
        right = len(s) - 1
        while left < right:
            if s[i] + s[left] + s[right] == sum_to_find:
                return True
            elif s[i] + s[left] + s[right] < sum_to_find:
                left += 1
            else:
                right -= 1
    return False


s = [int(i) for i in input().split()]
sum_to_find = int(input())
print(find_sum(s, sum_to_find))
