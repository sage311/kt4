import cv2
import numpy as np

capture = cv2.VideoCapture(r"C:\Users\arina\OneDrive\Desktop\kt4-main\она_исла.mp4")

# Параметры вращения
angle = 0
rotation_speed = 0.02  # Увеличили скорость вращения для более динамичного эффекта

while capture.isOpened():
    ret, frame = capture.read()

    if not ret:
        break

    # Установка ширины и высоты окна
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cv2.namedWindow('Result', cv2.WINDOW_NORMAL)

    height, width = frame.shape[:2]
    center_x, center_y = width // 2, height // 2

    # Смещение вершин для эффекта вращения
    offset_x = int(200 * np.sin(angle))  # Уменьшили смещение по X
    offset_y = int(150 * np.cos(angle))  # Увеличили смещение по Y

    # Перспективное преобразование
    src_points = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    dst_points = np.float32([[offset_x, offset_y],
                              [width - offset_x, offset_y],
                              [width - offset_x, height - offset_y],
                              [offset_x, height - offset_y]])

    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Применение перспективного преобразования
    rotated_frame = cv2.warpPerspective(frame, matrix, (width, height))

    # Преобразование кадра в оттенки серого
    gray_frame = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2GRAY)

    # Показ результата
    cv2.imshow('Result', gray_frame)
    cv2.resizeWindow('Result', 1920, 1080)

    angle += rotation_speed

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
capture.release()
cv2.destroyAllWindows()
