import cv2
import numpy as np
import csv
from PIL import Image

if __name__ == '__main__':

    count = 0
    index = 0

    data = []
    amount = 3096

    while index < amount:

        if count <= 9:
            img_path = './romance 2/romance_0000' + str(count) + '.jpg'
        elif count <= 99:
            img_path = './romance 2/romance_000' + str(count) + '.jpg'
        elif count <= 999:
            img_path = './romance 2/romance_00' + str(count) + '.jpg'
        elif count >= 1000:
            img_path = './romance 2/romance_0' + str(count) + '.jpg'
        image = Image.open(img_path)

        num_colors = 1

        small_image = image.resize((80, 80))
        result = small_image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)

        result = result.convert('RGB')
        main_colors = result.getcolors(80 * 80)
        print(main_colors[0][1])
        data.append(main_colors[0][1])
        count += 1
        index += 1

    f = open('romance 2.csv', 'w')
    writer = csv.writer(f)
    for i in data:
        writer.writerow(i)
    total = round(amount / 0.9)
    print(total)
    different = total - amount
    number = 0
    white = [255,255,255]
    while number < (total - amount):
        writer.writerow(white)
        number += 1
    f.close()


    # for count, col in main_colors:
    #     if count < 40:
    #         continue
    #     a = np.zeros((224, 224, 3))
    #     a = a + np.array(col)
    #     # print(a)
    #     cv2.imshow('a', a.astype(np.uint8)[:, :, ::-1])
    #     cv2.waitKey()
