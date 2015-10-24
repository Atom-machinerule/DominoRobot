from image import Image
from processing import Processing

images = ["images/Masked.jpg"]

def process_images():
	for img in images:
		img = Image(img, 1)
		processing = Processing(img)
		processing.get_domino_points()	

if __name__ == '__main__':
	process_images()
