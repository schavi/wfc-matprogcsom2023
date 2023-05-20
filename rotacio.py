
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy
import tiledict

def forgato(z):
    if tiledict.tiles[z]['varians'] == "0":
        pil_img = Image.open(tiledict.tiles[z]["nev"]+".png")
        return numpy.array(pil_img)
    if tiledict.tiles[z]['varians'] == "1":
        pil_img = Image.open(tiledict.tiles[z]["nev"]+".png")
        rotate_pil_img = pil_img.rotate(90).convert('RGB')
        vegleges = numpy.array(rotate_pil_img)
        return vegleges
    if tiledict.tiles[z]['varians'] == "2":
        pil_img = Image.open(tiledict.tiles[z]["nev"]+".png")
        rotate_pil_img = pil_img.rotate(180).convert('RGB')
        vegleges = numpy.array(rotate_pil_img)
        return vegleges
    if tiledict.tiles[z]['varians'] == "3":
        pil_img = Image.open(tiledict.tiles[z]["nev"]+".png")
        rotate_pil_img = pil_img.rotate(270).convert('RGB')
        vegleges = numpy.array(rotate_pil_img)
        return vegleges
    if tiledict.tiles[z]['varians'] == "4":
        pil_img = Image.open(tiledict.tiles[z]["nev"]+".png")
        rotate_pil_img = ImageOps.mirror(pil_img.rotate(0).convert('RGB'))
        vegleges = numpy.array(rotate_pil_img)
        return vegleges
    if tiledict.tiles[z]['varians'] == "5":
        pil_img = Image.open(tiledict.tiles[z]["nev"]+".png")
        rotate_pil_img = ImageOps.mirror(pil_img.rotate(90).convert('RGB'))
        vegleges = numpy.array(rotate_pil_img)
        return vegleges
    if tiledict.tiles[z]['varians'] == "6":
        pil_img = Image.open(tiledict.tiles[z]["nev"]+".png")
        rotate_pil_img = ImageOps.mirror(pil_img.rotate(180).convert('RGB'))
        vegleges = numpy.array(rotate_pil_img)
        return vegleges
    if tiledict.tiles[z]['varians'] == "7":
        pil_img = Image.open(tiledict.tiles[z]["nev"]+".png")
        rotate_pil_img = ImageOps.mirror(pil_img.rotate(270).convert('RGB'))
        vegleges = numpy.array(rotate_pil_img)
        return vegleges

plt.imshow(forgato(103))