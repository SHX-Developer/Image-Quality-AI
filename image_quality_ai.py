import cv2

def improve_image_quality(image):

    #  Improving quality of image
    image = cv2.resize(image, dsize=(image.shape[1] * 2, image.shape[0] * 2), interpolation=cv2.INTER_CUBIC)

    #  Adding effects
    image = cv2.GaussianBlur(image, (5, 5), 0)
    image = cv2.addWeighted(image, 1, image, 2, 0)

    #  Saving image as original photo size
    image = cv2.resize(image, dsize=(image.shape[1] // 2, image.shape[0] // 2), interpolation=cv2.INTER_CUBIC)

    return image

#  Uploading image
image = cv2.imread("image.jpg")

#  Improve quality function
image = improve_image_quality(image)

#  Saving image
cv2.imwrite("improved_image.jpg", image)