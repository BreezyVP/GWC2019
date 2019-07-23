#Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
filename = Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    pic = Image.open(filename)
    return pic

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(myfile):
    myfile.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgobj, cat):
    imgobj.save(cat)

pic = load_img("CatInSunglasses.jfif")
show_img(pic)
save_img(pic, "CoolCat.jfif")
# Define your obamicon() function here
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
#import Filters

def obama_filter(pic):
    pixels = pic.getdata()
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    original_cat = []
    for p in pixels:
        sum = p[0] + p[1] + p[2]
        if sum < 182:
            original_cat.append(darkBlue)
        elif sum > 182 and sum < 364:
            original_cat.append(red)
        elif sum > 364 and sum < 546:
            original_cat.append(lightBlue)
        else:
            original_cat.append(yellow)
    obama_filtered = Image.new("RGB", pic.size)
    obama_filtered.putdata(original_cat)
    obama_filtered.show()
obama_filter(pic)

save_img("ObamaCat.jfif")
