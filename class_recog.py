from PIL import Image, ImageDraw, ImageFont
import numpy as np
import face_recognition

img = Image.open('class_photo.jpg')
img = img.resize((1500, 700), Image.ANTIALIAS)
img = img.convert('RGB')
img.show()


data = np.array(img)
locations = face_recognition.face_locations(data, number_of_times_to_upsample=4)
print(locations)


# We copy the image since we don't want to draw on the original image.
img_copy = img.copy()

draw = ImageDraw.Draw(img_copy)
for location in locations:
    top, right, bottom, left = location
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0), width=3)
del(draw)
img_copy.show()