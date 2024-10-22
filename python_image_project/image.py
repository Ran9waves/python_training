from PIL import Image, ImageFilter

img = Image.open('./images_folder/nameofthefile.jpeg')

print(img) #we get information about the image
print(img.format) #prints the format of the image
print(img.size) #prints the size of the image
print(img.mode) #print the mode of the image, i,e, RGB
print(dir(img)) #all the things that this image can give us

#we can also add some filters
filtered_img = img.filter(ImageFilter.BLUR) #this will apply the blur filter to the image
filtered_img.save("blur",'png') #this will save the image that we indicated into png, and save it in the format that we indicate
filtered_img = img.convert('L') #this will convert the image into another format, i.e. L will turn it into grayscale

filtered_img.show() #will open the file and show us the image
filtered_img.rotate(90) #this will rotate the image 90 degrees
filtered_img.resize((300,300)) #this will resize the image to the size that we indicate

box= (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('png')

img = Image.open('./images_folder/another_image.jpeg')
img.thumbnail((400, 400)) #It will resize the image and keep the actual ratio
img.save('thumbnail.jpg')

