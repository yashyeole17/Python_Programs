# Write Python Program to Create a New Image from an Existing Image.

with open('image.png','rb') as f:
    f1=open('image1.png','wb')
    f1.write(f.read())
    print("Image created Successfully")
    f1.close()