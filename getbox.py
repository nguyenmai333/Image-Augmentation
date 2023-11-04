def get_box(image, label_dir):
    boxes = []
    cropped_images =[]
    with open(label_dir, 'r') as f:
        file = f.readlines()
        for i in range(0, len(file)):
            parts = file[i].split()
            x_center = float(parts[1])
            y_center = float(parts[2])
            width = float(parts[3])
            height = float(parts[4])
            #get box
            box = (x_center, y_center, width, height)
            #get coordinates
            left = int((box[0] - box[2] / 2) * image.shape[1])
            right = int((box[0] + box[2] / 2) * image.shape[1])
            top = int((box[1] - box[3] / 2) * image.shape[0])
            bottom = int((box[1] + box[3] / 2) * image.shape[0])
            #append box and cropped_image
            boxes.append([left, right, top, bottom])
            cropped_images.append(image[top:bottom, left:right])
    return (boxes, cropped_images)