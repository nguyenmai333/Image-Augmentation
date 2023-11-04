import os
import shutil
import cv2
from getbox import get_box
from filter import *


def apply_filter(image, filter_box, box):
    top, left = (box[2], box[0]) 
    bottom, right = (box[3], box[1]) 
    image[top:bottom, left:right] = filter_box
    return image


def export(images_dir, labels_dir, image_root, name_file, val, keys, filtered_object, boxes):
    cnt = 0
    for filter_ in range(0, 3):
        for ind in range(0, val - 1):
            final_image = image_root.copy()  # Tạo một bản sao của hình ảnh gốc:
            cnt += 1
            for key in keys:
                final_image = apply_filter(final_image, filtered_object[key][0][filter_][ind], boxes[int(key) - 1])
            cv2.imwrite(os.path.join(images_dir, f"{name_file}_{cnt}.jpg"), final_image)
            shutil.copy(os.path.join(labels_dir, f"{name_file}.txt"), os.path.join(labels_dir,f"{name_file}_{cnt}.txt"))


def addFilter(images_dir, labels_dir):
    list_items = os.listdir(images_dir)
    for item in list_items: 
    #file processing
        name_file = item.replace('.jpg', '')
        image_path = os.path.join(images_dir, item)
        image_root = cv2.imread(image_path)
        label_name = item.replace('jpg', 'txt')
        label_path = os.path.join(labels_dir, label_name)
        boxes, cropped_images = get_box(image_root, label_path)

        size_boxes = len(boxes)

        filtered_object = {}
        for i in range(1, size_boxes + 1):
            filtered_object[str(i)] = []

        val = 10 #custom amountOfImages default = 10

        for index_object, cropped_image in enumerate(cropped_images):
            filter_images = processing_image(cropped_image, val)
            filtered_object[str(index_object + 1)].append(filter_images)
        
        export(images_dir, labels_dir, image_root, name_file, val, list(filtered_object.keys()), filtered_object, boxes)
        