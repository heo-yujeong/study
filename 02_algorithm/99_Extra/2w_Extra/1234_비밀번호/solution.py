import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N, num_list = input().split()

    pw_stack = []

    for num in num_list:
        if pw_stack:
            if num == pw_stack[-1]:
                pw_stack.pop()
            else:
                pw_stack.append(num)
        else:
            pw_stack.append(num)

    pw = ''.join(pw_stack)

    print(f'#{test_case}', ''.join(pw_stack))