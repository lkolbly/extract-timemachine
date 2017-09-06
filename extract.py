import os
import sys
import shutil

def convert(snapshotRoot, hfsPrivateDirectory, destinationRoot):
	privateDirectories = set(os.listdir(hfsPrivateDirectory))

	toProcess = [snapshotRoot]
	while len(toProcess) > 0:
		dirname = toProcess.pop()
		print(dirname)

		destDir = destinationRoot + "/" + dirname[len(snapshotRoot):]
		print(destDir)

		# Make this directory exist in the target
		try:
			os.mkdir(destDir)
		except FileExistsError:
			print(destDir, "already exists, not creating")
			pass

		for entry in os.scandir(dirname):
			if entry.is_dir():
				# Recurse into this directory
				toProcess.append(entry.path)
			elif "dir_%d"%entry.stat(follow_symlinks=False).st_nlink in privateDirectories:
				# This is a link to a HFS+ private directory
				print(entry.name, "is a directory, nlink =", entry.stat().st_nlink)
				try:
					shutil.copytree(hfsPrivateDirectory + "/dir_%d"%entry.stat(follow_symlinks=False).st_nlink, destDir + "/" + entry.name, ignore_dangling_symlinks=True)
				except shutil.Error as e:
					print("Error occurred copying:", e)
			else:
				# This is just a file
				print("copying", entry.name)
				try:
					open(destDir + "/" + entry.name, "wb").write(open(entry.path, "rb").read())
				except FileNotFoundError:
					print("Could not find file", entry.path, "it is probably a symlink")
			#print(entry.name, entry.stat().st_nlink, entry.is_dir())
		pass


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage:", sys.argv[0],"<Time Machine snapshot directory> <HFS private directory> <destination directory>")
		sys.exit(1)
	convert(sys.argv[1], sys.argv[2], sys.argv[3])
