import sys

sys.path.append("/home/coder/project")

import logging
import random
import time
import uuid

from wf_steps.common import OUTPUT_DIR

logging.basicConfig(level=logging.INFO)

data_path = OUTPUT_DIR / f"long_step_data_{uuid.uuid4()}.txt"

iterations = random.randint(10, 180)

logging.warning(f"Running {iterations} iterations")
with data_path.open("w") as data_fp:
    for i in range(1, iterations + 1):
        msg = f" {i}. Rolos is awesome!"
        logging.info(msg)
        data_fp.write(msg + '\n')
        time.sleep(1)
