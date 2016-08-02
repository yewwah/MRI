#"resize img"

import os
from PIL import Image

source = os.listdir("Normal Scans Image")
for folder in source:
	os.mkdir("Normal Scans Image\\" + folder + "_resized") 

for folder in source:
	img_files = os.listdir("Normal Scans Image\\" + folder)
	for img in img_files:
		img_old = Image.open('Normal Scans Image\\' + folder + "\\" + img)
		img_new = img_old.resize([64,64])
		img_new.save("Normal Scans Image\\" + folder + "_resized\\" + img)