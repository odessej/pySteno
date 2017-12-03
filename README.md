# Stenography tool

**Supported format are** : '.bmp', '.png', '.tga', '.tif', '.tiff'
JPEG is not supported. Maybe others formats will work, let me know and I'll add them to the list.

This is a simple tool allowing to hide a file into a picture.

The data is hid into the least significant bit of every pixel RGB value.

3 bit = 1 pixel, so if you want to know how many octets(bytes) of data you can hide into one picture use this equation :
```
floor((image.width * image.height * 3) / 8)
```

Any type of file can be hidden, the script reads the file in binary.
So if you want to hide a message, just put it into a .txt file.
