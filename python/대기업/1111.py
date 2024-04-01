from math import factorial

def kth_permutation(A, k):
    n = len(A)
    result = []

    # 문자열 A를 리스트로 변환하여 정렬
    A = sorted(list(A))

    # k번째 순열 찾기
    k -= 1  # 0-based index로 변환
    for i in range(n):
        # 현재 글자를 결과에 추가
        idx, k = divmod(k, factorial(n - 1 - i))
        result.append(A.pop(idx))

    return ''.join(result)

# 입력 받기
A,k = input().split()
k = int(k)

# 결과 출력
result = kth_permutation(A, k)
print(result)
