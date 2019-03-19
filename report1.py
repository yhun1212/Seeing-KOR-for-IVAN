import numpy as np
import cv2
import matplotlib.pyplot as pltp
import imageio

def getRepColor(img):
    R_aver = 0 ; C_aver = 0
    r_num = 1 ; c_num = 1
    r_count = 0 ; c_count = 0

    while r_num > img.shape[0]:
        R_aver += img.shape[0]
        r_num += 1
        r_count += 1
    while c_num > img.shape[1]:
        C_aver += img.shape[1]
        c_num += 1
        c_count += 1
    
    R_aver = R_aver // r_count
    C_aver = C_aver // c_count

    color = img[R_aver, C_aver]
    return color

filename = '지융미 응원영상.mp4'
cap = cv2.VideoCapture(filename) 

CList = []

#만들어 놓은 리스트에 모든 각 프레임의 color값들 넣어줌
while(True): #For each frame
    ret, frame = cap.read() #각 프레임 읽어오기

    if ret == False: #프레임 다 읽으면 while문 끝내기
        break 

    c = getRepColor(frame) #위에서 정의한 함수 사용 = color값 뽑아냄
    CList.append(c) #뽑아낸 칼라값 리스트에 더해줌
#    

cap.release()

img = np.zeros((1000,len(CList),3)) 
#이미지 만들어줌: 세로 1000, 가로는 프레임 수만큼, depth는 3(r,g,b)
#세로 길이는 임의로 조정하면 됨!

#visualizing barcode
for i in range(len(CList)): #CList의 길이만큼 = 프레임 수만큼
    img[:,i] = CList[i] 
    #첫시간에 img[50,50]=[255,0,0] 이렇게 좌표 찍었던 것 응용
    #[:]: 전체 구간
    #img[:,i]: column은 전체구간, row는 i번째
    #CList[i] = CList의 i번째 원소 = i번째 프레임의 r,g,b 값 

        
#cv2에서는 이미지 읽을 때 b,g,r 순서이기 때문에 b와 r의 순서 바꿔줘야 함
b, g, r = cv2.split(img)   #img파일을 b,g,r로 분리
img2 = cv2.merge([r,g,b]) #b,r을 바꿔서 Merge

img2 = img2.astype(np.uint8) #r,g,b range error 고치기
plt.imshow(img2) 
plt.show()

imageio.imwrite('지융미 바코드.png', img2) #img를 '0314_forest.png'라는 이름의 이미지 파일로 저장하기

cv2.destroyAllWindows() #cv2.imshow 함수를 사용했으면 이 내용을 붙어야 함!
