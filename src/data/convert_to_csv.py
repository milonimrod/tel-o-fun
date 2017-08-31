import pandas as pd
import os
import glob
from tqdm import tqdm

DATA_DIR = "data"

output_file = os.path.join(DATA_DIR, "data.csv")
if os.path.isfile(output_file):
    os.unlink(output_file)
with open(output_file, 'a') as f:
    files = glob.glob(os.path.join(DATA_DIR, "*.pkl"))
    df = pd.read_pickle(files[0])
    df.to_csv(f, header=True, encoding='windows-1255')
    del df
    for fileName in tqdm(files[1:]):
        df = pd.read_pickle(fileName)
        df.to_csv(f, header=False, encoding='windows-1255')
        del df
