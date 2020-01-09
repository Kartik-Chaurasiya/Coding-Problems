"""
This problem was asked by Google.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0."""


input = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
lvl = {-1: 0}
max_len = 0
for line in input.split('\n') :
	depth = line.count('\t')
	lvl[depth] = len(line) - depth + lvl[depth-1]
	if '.' in line :
		max_len = max(max_len, lvl[depth]+depth)
print(max_len)


"""
Output :

32
[Finished in 0.2s]

"""