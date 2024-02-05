import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    # test_case: #기호 + 테스트 케이스번호, N: 테스트케이스 길이
    test_case, N = input().split()
    # 테스트 케이스의 길이는 정수이므로 형변환
    N = int(N)
    # N개의 단어
    words = input().split()

    num_chr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 각 단어가 몇개씩 나왔는지 count
    counts = [0] * 10
    # 결과 출력할 리스트
    result = [0] * len(words)

    for word in words:
        for idx in range(len(num_chr)):
            if word == num_chr[idx]:
                counts[idx] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(len(result)-1, -1, -1):
        counts[num_chr.index(words[i])] -= 1
        result[counts[num_chr.index(words[i])]] = words[i]

    print(test_case)
    print(*result)