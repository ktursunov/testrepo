from wf_steps.common import DATA_DIR

print(sum(1 for _ in DATA_DIR.glob("*")))
