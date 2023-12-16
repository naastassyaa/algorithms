def get_next_state(needle, state, x):
    m = len(needle)
    if state < m and x == needle[state]:
        return state + 1

    for ns in range(state, 0, -1):
        if needle[ns - 1] == x:
            if needle[:ns - 1] == needle[state - ns + 1:state]:
                return ns
    return 0


def compute_tf(needle):
    m = len(needle)
    tf = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for x in set(needle):
            z = get_next_state(needle, state, x)
            tf[state][x] = z

    return tf


def search(needle, haystack):
    if not needle:
        return []

    m = len(needle)
    n = len(haystack)
    tf = compute_tf(needle)
    print(tf)
    state = 0
    indexes = []

    for i in range(n):
        state = tf[state].get(haystack[i], 0)

        if state == m:
            indexes.append(i - m + 1)
            print("Pattern found at index: {}".format(i - m + 1))
    return indexes


haystack = "AABAACAADAABAABAA"
needle = "ABAA"
indexes = search(needle, haystack)
if not indexes:
    print("Pattern not found")
