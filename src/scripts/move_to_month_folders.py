import datetime
import glob
import os
from tqdm import tqdm

files = glob.glob("data/*.pkl")
for f in tqdm(files):
    base_name = os.path.basename(f)
    ts = float(base_name.split("_")[1].split(".")[0])
    dir_name = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m')
    dir_name = os.path.join("data", dir_name)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    os.rename(f, os.path.join(dir_name,     base_name))
