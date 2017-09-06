Extract TimeMachine
===================

Do you have a Mac OS Time Machine backup that you need to get the data off of, but you only have Linux boxes? If so, you've come to the right place!

Time Machine backups do clever things, for details look at:
* http://hints.macworld.com/article.php?story=20080623213342356
* https://gist.github.com/vjt/5183305

This script will read a Time Machine backup, and spit the result into a directory.

To run it, you must pass three command line arguments (in this order):
1. The Time Machine directory you want to copy. If /media/tm/ is where your time machine is mounted, look in /media/tm/Backups.backupdb/<computer name>/<snapshot date>/Macintosh HD/
2. The .HFS+ Private Directory Data folder (look in /media/tm/), and
3. The root directory to put the copy into.

If you have any problems, create an issue or a PR!

This program comes with no warranty or gaurantee of any kind, use at your own risk. Always back up your data before running strange scripts on it.
