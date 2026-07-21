import subprocess
import os

files = subprocess.check_output(['git', 'ls-files', 'static/img/libros']).decode('utf-8').splitlines()

for f in files:
    if f.lower() != f:
        temp = f + '.temp'
        new = f.lower()
        subprocess.run(['git', 'mv', f, temp])
        subprocess.run(['git', 'mv', temp, new])
