import Filters

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

obama_cat = []

def obama_filter(pic):
    pic.getdata()
    pixels = list(pic.getdata())
    for p in pixels:
        sum = p[0] + p[1] + p[2]
    for intensity in item:
        if sum < 182:
            obama_cat.append(darkBlue)
        elif sum > 182 and sum < 364:
            obama_cat.append(red)
        elif sum > 364 and sum < 546:
            obama_cat.append(lightBlue)
        else:
            obama_cat.append(yellow)

obama_filter(pic)
save_img("ObamaCat.jfif")
