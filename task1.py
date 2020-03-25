

import utils
import numpy as np
import json
import time
import random


def kmeans(img,k):
    """
    Implement kmeans clustering on the given image.
    Steps:
    (1) Random initialize the centers.
    (2) Calculate distances and update centers, stop when centers do not change.
    (3) Iterate all initializations and return the best result.
    Arg: Input image;
         Number of K.
    Return: Clustering center values;
            Clustering labels of all pixels;
            Minimum summation of distance between each pixel and its center.
    """
    # TODO: implement this function.
    x1,x2 = np.random.choice(len(img), 2)
    y1,y2 = np.random.choice(len(img[0]), 2)
    c1 = img[x1][y1]
    c2 = img[x2][y2]
    print(c1, c2)
    modified_img = np.zeros(np.shape(img))
    old_c1 = -1
    old_c2 = -1
    ctr = 0
    while(not (c1 == old_c1 and c2 == old_c2)):
        sum1 = 0
        sum2 = 0
        error = 0
        count1 = 0
        count2 = 0
        # print("For 1 point: ")
        print(c1)
        print(c2)
        print(""+str(ctr)+"\n")
        if(ctr >= 12):
            break
        old_c1 = c1
        old_c2 = c2
        for x in range(len(img)):
            for y in range(len(img[0])):
                img[x][y] = int(img[x][y])
                c1 = int(c1)
                c2 = int(c2)
                d1 = abs(img[x][y] - c1)
                d2 = abs(img[x][y] - c2)
                if(d1 <= d2):
                    modified_img[x][y] = c1
                    error += d1
                    sum1+=img[x][y]
                    count1+=1
                else:
                    modified_img[x][y] = c2
                    error += d2
                    sum2+=img[x][y]
                    count2+=1
        print(error)
        if(count1 == 0):
            count1 = 1
        if(count2 == 0):
            count2 = 1
        c1 = sum1 / count1
        c2 = sum2 / count2
        ctr+=1

    modified_img = modified_img.astype(np.uint8)
    return (c1,c2),modified_img,-1


def visualize(centers,labels):
    """
    Convert the image to segmentation map replacing each pixel value with its center.
    Arg: Clustering center values;
         Clustering labels of all pixels.
    Return: Segmentation map.
    """
    # TODO: implement this function.
    return labels

if __name__ == "__main__":
    img = utils.read_image('lenna.png')
    k = 2

    start_time = time.time()
    centers, labels, sumdistance = kmeans(img,k)
    result = visualize(centers, labels)
    end_time = time.time()

    running_time = end_time - start_time
    print("Run time")
    print(running_time)

    centers = list(centers)
    with open('results/task1.json', "w") as jsonFile:
        jsonFile.write(json.dumps({"centers":centers, "distance":sumdistance, "time":running_time}))
    utils.write_image(result, 'results/task1_result.jpg')
