separator = '-'
def encode_category_name(name):
	return name.replace(' ', separator)

def decode_category_name(name):
	return name.replace(separator, ' ')