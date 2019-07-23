import math
from PIL import Image
picture = Image.open("BlueBananas.jpg")

def load_img(picture):
    pic = Image.open(picture)
    return pic

def show_img(myfile):
    myfile.show()

def save_img(imgobj, banana):
    imgobj.save(banana)

def distance_formula(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def emphasize_color(pic):
    gainsboro = (220, 220, 220)
    light_gray = (211, 211, 211)
    silver = (192, 192, 192)
    dark_gray = (169, 169, 169)
    gray = (128, 128, 128)
    dim_grey = (105, 105, 105)
    pixels = picture.getdata()
    original_banana = []
    for p in pixels:
        sum = p[0] + p[1] + p[2]
        if sum >= 660:
            original_banana.append(gainsboro)
        if sum < 660 and sum >= 633:
            original_banana.append(gainsboro)
        if sum < 633 and sum >= 576:
            original_banana.append(light_gray)
        if sum < 576 and sum >= 487:
            original_banana.append(silver)
        if sum < 487 and sum >= 384:
            original_banana.append(dark_gray)
        if sum < 384 and sum >= 315:
            original_banana.append(gray)
        if sum < 315 and sum >= 0:
            original_banana.append(dim_grey)
    cyan_filtered = Image.new("RGB", picture.size)
    cyan_filtered.putdata(original_banana)
    cyan_filtered.show()

emphasize_color(picture)

pic = load_img("BlueBananas.jpg")
show_img(pic)
save_img(pic, "BetterBananas.jpg")
