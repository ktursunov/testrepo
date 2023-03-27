import sys 

sys.path.append("/home/coder/project")

from wf_steps.common import OUTPUT_DIR

data_path = OUTPUT_DIR / "some_test_data.txt"

data_path.write_text("Rolos is awesome")
