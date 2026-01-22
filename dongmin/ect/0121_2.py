n=int(input())

k=0
for _ in range(n):
    l=input()
    lst=list(l)
    st=set(lst)
    for i in st:
        a=lst.count(i)
        if not i*a in l:
            k+=1
            break

print(n-k)


#그룹 단어 체커 1316
#집합 자료형(set)은 중복을 허용하지 않는다. 
# count()는 리스트에서 특정 값의 개수를 세는 함수이다.
# n = int(input())
# bad = 0

# for _ in range(n):
#     w = input().strip()
#     seen = set()
#     prev = ""
#     ok = True

#     for ch in w:
#         if ch != prev:
#             if ch in seen:
#                 ok = False
#                 break
#             seen.add(ch)
#             prev = ch

#     if not ok:
#         bad += 1

# print(n - bad)
