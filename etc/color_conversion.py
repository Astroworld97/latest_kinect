# Python3 program change RGB Color
# Model to HSV Color Model

def rgb_to_hsv(r, g, b):

	# R, G, B values are divided by 255
	# to change the range from the range [0, 255] to the range [0, 1]
	r, g, b = r / 255.0, g / 255.0, b / 255.0

	# h, s, v = hue, saturation, value
	cmax = max(r, g, b) # maximum of r, g, b
	cmin = min(r, g, b) # minimum of r, g, b
	diff = cmax-cmin	 # diff of cmax and cmin.

	# if cmax and cmin are equal then h = 0
	if cmax == cmin:
		h = 0
	
	# if cmax equals r, then compute h
	elif cmax == r:
		h = (60 * ((g - b) / diff) + 360) % 360

	# if cmax equal g then compute h
	elif cmax == g:
		h = (60 * ((b - r) / diff) + 120) % 360

	# if cmax equal b then compute h
	elif cmax == b:
		h = (60 * ((r - g) / diff) + 240) % 360

	# if cmax equal zero
	if cmax == 0:
		s = 0
	else:
		s = (diff / cmax) * 100

	# compute v
	v = cmax * 100
	return h, s, v


''' Driver Code '''
# print(rgb_to_hsv(45, 215, 0))
# print(rgb_to_hsv(31, 52, 29))
# print(rgb_to_hsv(129, 88, 47))
print(rgb_to_hsv(0, 0, 255))