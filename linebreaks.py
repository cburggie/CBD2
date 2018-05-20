#!/usr/bin/python

# when diablo ii is parsing a .txt file as a spreadsheet it uses 0x0d0a to delimit lines.
# my spreadsheet program (libreoffice calc) when saving as a .csv file will use 0x0a to delimit lines.
# this tool takes a standalone 0x0a byte and precedes it with a 0x0d byte.



import os
import sys



# strategy is to split the contents by the longer delimiter, then each
# substring by the shorter one. We'll splice all those back together
# with the correct one. This will catch cases of mixed line breaks.

def fix_file_contents(contents):
	
	big_separator = "\x0d\x0a"
	little_separator = "\x0a"
	
	big_segments = contents.split(big_separator)
	accumulator = []
	for bs in big_segments:
		small_chunks = bs.split(little_separator)
		for sc in small_chunks:
			accumulator.append(sc)
	return big_separator.join(accumulator)





def get_filenames():
	
	target_path = "./Data/Global/Excel"
	target_file_extension = ".txt"
	
	filenames = os.listdir(target_path)
	result = []
	for fn in filenames:
		if target_file_extension in fn:
			result.append(target_path + '/' + fn)
	return result





def run():
	
	filenames = get_filenames()
	for fn in filenames:
		fd = open(fn, 'r')
		contents = fd.read()
		fd.close()
		updated = fix_file_contents(contents)
		fd = open(fn, 'w')
		fd.write(updated)
		fd.close()

if __name__ == "__main__":
	run()



