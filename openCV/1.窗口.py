import cv2
# 创建窗口
# cv2.namedWindow("window",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("window",cv2.WINDOW_NORMAL)
# 改变窗口大小
cv2.resizeWindow("window",800,600)

# 展示窗口
cv2.imshow("window",0)

# 等待按键
# 0表示接收任意按键，其它整数表示等待按键的时间，单位是毫秒
# waitKey返回按下按键的ASCII值
# ord()函数可以计算ASCII值
key= cv2.waitKey(0)
if key==27:
    cv2.destroyWindow("window")

