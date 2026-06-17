import cv2
import numpy as np

# 문제 1. BGR 이미지를 Gray 이미지로 변환
def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 문제 2. 이미지를 지정한 크기로 변경
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)

# 문제 3. Gray 이미지에 Binary Threshold 적용
def apply_threshold(gray_image, threshold_value):
    # 255를 최대값으로 하는 이진화 수행
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

# 문제 4. 이미지에서 빨간색 픽셀 개수 계산
def count_red_pixels(image):
    b, g, r = cv2.split(image)
    # 조건: R > 200, G < 50, B < 50
    mask = (r > 200) & (g < 50) & (b < 50)
    return np.sum(mask)
# src/main.py 수정
def find_object_center(mask):
    y_coords, x_coords = np.where(mask == 255)
    if len(x_coords) == 0: return None
    
    # 29.5 -> 29, 49.5 -> 49가 나오게 하려면
    # 내림(floor)을 하거나, 다른 반올림 방식을 사용해야 합니다.
    # 간단하게 int()를 씌우면 내림 효과가 납니다.
    cx = int(np.mean(x_coords)) 
    cy = int(np.mean(y_coords))
    
    return (cx, cy)