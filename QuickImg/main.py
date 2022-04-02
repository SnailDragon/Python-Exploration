from PIL import Image, ImageFilter, ImageChops

#Read image
im = Image.open( 'howlscastle.jpg' )
#Display image
#im.show()

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

newr = ImageChops.multiply(r, Image.new('RGB', r.size, (255,0,0)))

newr.save('newr.jpg', 'JPEG')
#Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data

