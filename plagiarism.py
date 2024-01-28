import glob

def check_plagiarism(file_extension):
	files = glob.glob(f"*.{file_extension}")
	num_files = len(files)

	for i in range(num_files):
		for j in range(i+1, num_files):
			file1 = files[i]
			file2 = files[j]

			with open(file1, 'r') as f1, open(file2, 'r') as f2:
				content1 = f1.read()
				content2 = f2.read()

				if content1 == content2:
					print(f"{file1} and {file2} are identical.")
				else:
					print(f"{file1} and {file2} are different.")

# Example usage
check_plagiarism("file2.txt")
