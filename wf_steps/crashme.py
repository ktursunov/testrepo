import time 
import sys

GB = 1024*1024*1024

if __name__ == "__main__":
    big_string = b'a' * GB * 8
    time.sleep(30)
    sys.exit(0)