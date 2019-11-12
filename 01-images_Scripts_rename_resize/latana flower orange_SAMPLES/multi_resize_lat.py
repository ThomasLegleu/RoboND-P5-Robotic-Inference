import cv2, glob,os

images=glob.glob("*.jpg")

width = 500
height = 500
dim = (width, height)



set_dir = "latana"
name_type = "lat"
number = 0


for image in images:

	img=cv2.imread(image,3)

	resized=cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
	

	print('Resized Dimensions : ',resized.shape)
	cv2.imshow("Checking",resized)

	cv2.waitKey(500)
	cv2.destroyAllWindows()

	#cv2.imwrite("resized_"+image,resized)
	#cv2.imwrite(os.path.join(path,image), resized)
	cv2.imwrite('/Users/beatr/Desktop/Computer_Vision/google-images-download-master/downloads/new/latana flower orange/' + set_dir + '/' + name_type + "_" + str(number) + ".png", resized)
	number+=1