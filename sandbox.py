from PIL import Image

mac = Image.open('example.png')

print(type(mac))
# => <class 'PIL.PngImagePlugin.PngImageFile'> specialized image file from PIL

# mac.show()
# this opens up the image

print(mac.size)
# (220, 165) width and height

print(mac.filename)
# 'example.png'

print(mac.format_description)
# Portable network graphics

# cropping image
# 0, 0 - starting coordinates
# 100, 100 - width height 100 100
cropped_img = mac.crop((0, 0, 100, 100))
# cropped_img.show()

# pasting cropped image on top of og image
mac.paste(im=cropped_img, box=(0, 0))

# resizing
mac.resize((3000, 500))

# rotating
mac.rotate(90)
