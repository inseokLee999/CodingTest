"""
1.아이디어
오늘 날짜를 정수로 바꾸고
add_terms함수로 privacies 에 있는 목록을 다 더해서
결과 출력
"""
def change_date(date):
    return int(date[2:4])*12*28+int(date[5:7])*28+int(date[8:10])
for i in terms:
    x,y=i.split()
    a=change_date(x)+T[y]
