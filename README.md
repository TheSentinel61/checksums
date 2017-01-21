# Checksums

Scripts for running checksums against directories and files on
Windows and Linux and producing consistent output independent of the
operating system.

## Requirements

Both Linux and Windows should be able to meet the following requirements using
built in programs, the requirements are the same for both platforms, allowing
for easy comparison.

* [x] Iterate through each file within a directory
* [x] Compute the SHA1 checksum of each file
* [ ] Output the SHA1 checksum and filename separated by a space
* [ ] Allow the output to be redirected

## Instructions

1. Open command prompt. Run `echo %PATH%`
2. Copy checksum.cmd to one of the directories specified after running the above
3. To run the checksum, run: `checksum.cmd <path>`
