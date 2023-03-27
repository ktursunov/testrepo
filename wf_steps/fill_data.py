from pathlib import Path
from random import randint
import uuid
import os
import base64

max_depth = 2
spread = 3
out_dir = Path('./data')
out_dir.mkdir(parents=True, exist_ok=True)

def fill_folder(parent, depth=0):
    print(f'Fill folder {parent}')
    
    parent.mkdir(parents=True, exist_ok=True)
    for i in range(randint(1, spread)):
        new_file = parent / f"{uuid.uuid4().hex}.csv"
        print(f'Create file {new_file}')
        size_mb = randint(3, 10)
        content = base64.encodebytes(os.urandom(size_mb * 2**20))
        new_file.write_bytes(content)

    if depth < max_depth:
        for i in range(randint(1, 8)):
            fill_folder(parent / f'dir_{uuid.uuid4().hex}', depth + 1)


if __name__ == '__main__':
    fill_folder(out_dir)