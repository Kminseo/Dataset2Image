import os
import cv2
import random
import numpy as np

def datset_viewer(data_ad,width_size,height_size,row_count,column_count):
    data_list = os.listdir(data_ad)
    random.shuffle(data_list) # If you don't using shuffle, this line made to anotation
    row_num = 0
    column_num = 0
    result_img = np.zeros((height_size, width_size, 3), np.uint8)
    resize_w = int(width_size/row_count)
    resize_h = int(height_size/column_count)
    for data in data_list:
        img = cv2.imread(data_ad+"/"+data)
        img = cv2.resize(img,(resize_w,resize_h))
        if(column_num == column_count):
            break
        result_img[resize_h*column_num:resize_h*(column_num+1),resize_w*row_num:resize_w*(row_num+1)]=img
        if(row_num < row_count-1):
            row_num += 1
        else:
            row_num = 0
            column_num += 1
        
    return result_img

if __name__ == "__main__":
    dataset_list = '/home/cailab/Desktop/weld_data/images/0'
    width_size = 640
    height_size = 480
    row_count = 10
    column_count = 10
    img=datset_viewer(dataset_list,width_size,height_size,row_count,column_count)
    # check img
    cv2.imshow("result",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # save img
    cv2.imwrite("test.jpg",img)
