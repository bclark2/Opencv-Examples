import cv2


# load in the png in load_path parameter
# declare the path to write the converted jpg
def convert_to_jpg(load_path, save_path):
    image = cv2.imread(load_path)
    cv2.imwrite(save_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


convert_to_jpg('/path/to/read/png/file/file.png',
               '/path/to/write/jpg/file/file.jpg')
