from os import walk

def get_data():
	file_names = []
	for (dirpath, dirnames, filenames) in walk("./files"):
		file_names.extend(filenames)
		break
	return file_names



def main():
	file_names = get_data()
	print (file_names)
	for file_name in file_names:
		file = open('./files/' + file_name, 'r')
		print (file.read())

if __name__ == '__main__':
	main()
