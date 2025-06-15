import numpy as np
import os
import sys
from PIL import Image

def psnr(img1, img2):
    mse = np.mean((np.array(img1, dtype = np.float32) - np.array(img2, dtype = np.float32)) ** 2)
    return 20 * np.log10(255 / (np.sqrt(mse)))

psnrs = []
for i in range(125):
    img1 = Image.open(os.path.join(sys.argv[1], f"{i:04d}.png"))
    img2 = Image.open(os.path.join(sys.argv[2], f"{i:04d}.png"))
    psnrs.append(psnr(img1, img2))
print(np.average(psnrs))