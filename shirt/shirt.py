import sys
import os
from PIL import Image, ImageOps

def main():
    check_sys()
    muppet_maker()
def check_sys():
    t1,e1 = os.path.splitext(sys.argv[1])
    t2,e2 = os.path.splitext(sys.argv[2])
    accepted = [".jpeg", ".jpg", ".png"]
    if 3 > len(sys.argv) > 3:
        sys.exit("Need two command-line arguments...")
    if e1.lower() != e2.lower():
        sys.exit("File extensions must be the same")
    if not any(x in e1 for x in accepted) and not any(x in e2 for x in accepted):
        sys.exit("File must be either a .jpg, .jpeg or .png")
        
def muppet_maker():
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")
    shirtfile = Image.open("shirt.png")
    size = shirtfile.size
    muppet = ImageOps.fit(imagefile, size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])

if __name__ == "__main__":
    main()
