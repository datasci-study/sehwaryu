# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

# 이진탐색 함수 만들기
# p = 전체 쪽수, l = 첫째 쪽수 a = 찾아야하는 쪽수
def binarySearch(p, l, a):
    c = (l+p)/2
    print(c)
    # 이진탐색을 몇번 실시하는지 담는 변수
    count = 0 
    # a가 중간값보다 큰 경우 l = c
    if a > c:
        count +=1
        binarySearch(p, c, a)
    # a가 중간값보다 작은 경우 p = c
    elif a < c:
        count +=1
        binarySearch(c,l,a)
    elif c == a:
        print(count)
        
binarySearch(400,1,300)




# T = int(input())
# for t in range(T):
#     P, A, B = map(int,input())
#     count_A = 0
#     count_B = 0
#     l = 1
#     c = int((l+P)/2)