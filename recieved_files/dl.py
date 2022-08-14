
import hashlib, os
unique = []
for filename in os.listdir():
    if os.path.isfile(filename):
        filehash = hashlib.md5(open(filename, 'rb').read()).hexdigest()

        if filehash not in unique: 
            unique.append(filehash)
        else: 
            os.remove(filename)
