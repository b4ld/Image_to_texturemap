from PIL import Image

background = Image.open("newImage-image.png")
foreground = Image.open("newImage-hed.png")

background.paste(foreground, (0, 0), foreground)
background.show()