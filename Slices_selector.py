import os
import numpy as np
from skimage.io import imread,imsave
from skimage.measure import compare_ssim
import pandas as pd

def compare(img1, img2, threshold = 0.5):
	if compare_ssim(img1, img2) > threshold:
		return True
	return False


# Row names 

row_names = ["ab_" + str(x) for x in range(300)]
col_names = ["n_" + str(x) for x in range(300)]

df = pd.DataFrame(index=row_names, columns=col_names)
df = df.fillna(0) # with 0s rather than NaNs
# Load the images 

all_ab_scans = []
ab_source = os.listdir('abnormal_scan_resized')
for folder in ab_source:
	ab_scans = []
	images = os.listdir("abnormal_scan_resized/" + folder)
	for img in images:
		ab_scans.append(imread("abnormal_scan_resized/" + folder + "/" + img))

	all_ab_scans.append(ab_scans)

normal_source = os.listdir("Normal_resized")
for folder in normal_source:
	images = os.listdir("Normal_resized/" + folder)
	print 'Currently in folder ', folder
	for img in images:
		normal_img = imread("Normal_resized/" + folder + "/" + img)
		col = img.split('.')[0]
		for ab_fol in all_ab_scans:
			index = 1
			for ab_single_scan in ab_fol:
				if compare(ab_single_scan, normal_img):
					new_val = df.loc['ab_'+ str(index), 'n_'+str(col)]
					df.set_value('ab_'+ str(index), 'n_'+str(col), new_val)
				index += 1
import pickle
f = open('df.frame')
pickle.dump(df, f)
f.close()
# Compute similarity across images 
def compare(img1, img2, threshold = 0.5):
	if compare_ssim(img1, img2) > threshold:
		return True
	return False

	