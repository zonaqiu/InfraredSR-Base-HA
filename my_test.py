import cv2 as cv

lr_path = './CUFED/train/input/FLIR_00002_PreviewData.jpeg'
ref_path = './CUFED/train/ref/FLIR_00002_RGB.jpg'

lr = cv.imread(lr_path)
ref = cv.imread(ref_path)

print(type(lr))
print(lr.shape)
print(type(ref))
print(ref.shape)