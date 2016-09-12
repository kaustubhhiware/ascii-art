from PIL import Image	
import sys

ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def individual_ascii(image):
	"""
		Maps each pixel to an ascii char based on the range
		in which it lies.

		0-255 is divided into 11 ranges of 25 pixels each.
	"""

	pixels_in_image = list(image.getdata())
	char_list = [ASCII_CHARS[pixel_value/25] for pixel_value in pixels_in_image]

	return "".join(char_list)

def transform(image):
	image = image.convert('L')
	char_list = individual_ascii(image)

	ascii_art = [char_list[index: index + 100] for index in xrange(0, len(char_list), 100)]

	return "\n".join(ascii_art)


def transform_image(image_path):
	"""
		Handle the image conversion
	"""
	image = None
	try:
		image = Image.open(image_path)
	except Exception, e:
		return
	# image is opened , and exists at this point

	ascii_art = transform(image)
	print ascii_art


if __name__=="__main__":

	image_path = sys.argv[1]
	transform_image(image_path)