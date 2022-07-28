listOrigin = [12,5,9,7,8,15,22]
sortList=[]
# for t in range(len(listOrigin)):
#     max = listOrigin[0] #비교될원소 뽑기
#     for i in range(1, len(listOrigin)): # range 범위가 1부터인 이유는 자기 자신과 비교안해도 되기때문
#         if max <= listOrigin[i]: #비교될 원소와 들어온 원소를 비교해서 들어온 원소가 크면 
#             max = listOrigin[i]  #들어온 원소를 max로 교체 for 로 계속 돌리면 젤 큰수가 남게됨
#     listOrigin.remove(max) #기존 리스트에 제일큰원소를 제거
#     sortList.append(max) #새로운 리스트에 제일 큰원소 추가 
#                   #for b 리스트에 제일큰원소가 차례로 추가됨
# print(sortList)

listOrigin.remove(listOrigin[1])

print(listOrigin)


print('Hello World!')