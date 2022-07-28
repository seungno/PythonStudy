# import random

# def listCreate(listCount):
#     returnList = []
#     for valueCreate in range(listCount):
#         randomValue=random.randint(1,100)
#         returnList.append(randomValue)
#     return returnList


a = [12,5,9,7,8,15,22]
b=[]
for t in range(len(a)):
    max = a[0] #비교될원소 뽑기
    for i in range(1, len(a)): # range 범위가 1부터인 이유는 자기 자신과 비교안해도 되기때문
        if max <= a[i]: #비교될 원소와 들어온 원소를 비교해서 들어온 원소가 크면 
            max = a[i]  #들어온 원소를 max로 교체 for 로 계속 돌리면 젤 큰수가 남게됨
    a.remove(max) #기존 리스트에 제일큰원소를 제거
    b.append(max) #새로운 리스트에 제일 큰원소 추가 
                  #for b 리스트에 제일큰원소가 차례로 추가됨
                  

print(b)
