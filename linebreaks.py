#!/usr/bin/python

# This is a really ugly work around script for fixing the delimiters my
# spreadsheet program uses. Diablo II expects rows to be delimited by in the
# Windows style newline (carriage return - linefeed 0x0D0A) but my spreadsheet
# program uses the more usual (to me, at least) newline (linefeed 0x0A).

# sometimes a file ends up with a mix of 0x0A and 0x0D0A delimiters.
# my strategy will be to break the file up into its rows by parsing first by
# the larger delimiter and then each chunk by the smaller delimter. I'll then
# glue them back together with the correct one.

import os
import sys



# change all normal delimiters to windows styled ones
def windowsify_delimiters(contents):
	windows_delimiter = "\x0d\x0a"
	normal_delimiter = "\x0a"
	accumulator = []
	chunks = contents.split(windows_delimiter)
	for c in chunks:
		rows = c.split(normal_delimiter)
		for r in rows:
			accumulator.append(r)
	return windows_delimiter.join(accumulator)



# get all the .txt filenames from our Data/Global/Excel directory
def get_filenames():
	target_path = "./Data/Global/Excel"
	target_file_extension = ".txt"
	filenames = os.listdir(target_path)
	result = []
	for fn in filenames:
		if fn.endswith(target_file_extension):
			result.append(target_path + '/' + fn)
	return result



def run():
	filenames = get_filenames()
	for fn in filenames:
		fd = open(fn, 'r')
		contents = fd.read()
		fd.close()
		updated = windowsify_delimiters(contents)
		fd = open(fn, 'w')
		fd.write(updated)
		if len(contents) != len(updated):
			msg = fn + ": " + str(abs(len(updated) - len(contents)))
			msg += " changes"
			print(msg)
		fd.close()



if __name__ == "__main__":
	run()



