import cv2
import numpy as np

def apply_median_blur(image, kernel_size): #5
    return cv2.medianBlur(image, kernel_size)

def increase_brightness(image, value): #30
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = np.where(v <= 255 - value, v + value, 255)
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

def decrease_brightness(image, value): #30
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = np.where(v >= value, v - value, 0)
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

def salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size
    
    num_salt = int(total_pixels * salt_prob)
    salt_coordinates = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coordinates[0], salt_coordinates[1]] = 255
    
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coordinates = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coordinates[0], pepper_coordinates[1]] = 0
    
    return noisy_image

def processing_image(image, val):
    increase = []
    decrease = []
    noise = []
    for i in range(1, val):
        increase.append(increase_brightness(image, i * 5));
        decrease.append(decrease_brightness(image, i * 8));
        noise.append(salt_and_pepper_noise(image, 0.001*i*1.12, 0.001*i*1.12))
    #for i in range(1, val):
    #    images.append(apply_median_blur(image,i + 2))
    return [increase, decrease, noise]

