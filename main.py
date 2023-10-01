def solution(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i % 2 == 0:
                res.append(matrix[i][j])
            else:
                res.append(matrix[i][-1 - j])
    return " ".join(res)


if __name__ == "__main__":
    m, n = [int(i) for i in input().split()]
    matrix = []
    for i in range(m):
        matrix.append([i for i in input().split()])

    print(solution(matrix))
