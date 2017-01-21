import hashlib
import os
import sys

def spacify(string, n):
  return ' '.join(string[i:i+n] for i in xrange(0, len(string), n))

BUFFER_SIZE = 65536

print("\n")

for f in os.listdir(sys.argv[1]):
  sha1 = hashlib.sha1()

  with open(sys.argv[1] + "/" + f, 'rb') as ff:
    while True:
      data = ff.read(BUFFER_SIZE)
      if not data:
        break
      sha1.update(data)

  print("SHA1 hash of file {0}:\n{1}\nCertUtil: -hashfile command completed successfully.".format(f, spacify(sha1.hexdigest(), 2)))
