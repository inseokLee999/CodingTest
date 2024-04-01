"""
1. 아이디어
for 문으로 학생 통화기록의 합
통화요금을 계산해서 dictionary 에 저장 D[학생이름]=통화요금,
통화요금 계산 후 정렬후 출력
2. 시간복잡도
O(nlogn)
3. 자료구조
dict={}
A=[]
"""
n = int(input())
A = list(input() for _ in range(n))
def translate_time(S):
    return 60*int(S[:2])+int(S[3:5])
def calculate_price(T):
    if T<=100:
        return 10
    else :
        return 10+((T-100+50-1)//50*3)
def solution(n,A):
    D={}

    for a in A:
        if a[6:] in D:
            D[a[6:]]+= translate_time(a[:5])
            #print(a[6:])
            #print("누적 시간  : ",D[a[6:]])
        else :
            D[a[6:]]=translate_time(a[:5])
            #print(a[6:])
            #print("누적 시간  : ",D[a[6:]])
    for key,value in D.items():
        D[key]=calculate_price((value))
    answer=list(D.items())
    answer.sort(key=lambda x:(-x[1],x[0]))
    return answer
B=solution(n,A)
for name,cost in B:
    print(name,cost)