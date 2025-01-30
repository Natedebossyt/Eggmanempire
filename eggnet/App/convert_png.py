from PIL import Image

img = Image.open("E:/Eggman empire/eggnet/App/MetalSonic2.png")
img.convert("RGBA").save("E:/Eggman empire/eggnet/App/MetalSonic3.png")
