import sys
sys.path.append("/home/coder/project")

from wf_steps.common import DATA_DIR, OUTPUT_DIR
import csv 
import time


data_input_path = DATA_DIR / "poker_hand_train_true.csv"
output_data = OUTPUT_DIR / "some_data.csv"

limit_rows = 2000
with data_input_path.open() as fp:
    reader = csv.reader(fp)
    for row_num, row in enumerate(reader):
        
        row = [int(val) + 5 for val in row]
        
        print(row)
        time.sleep(0.1)
        if row_num > limit_rows:
            break
