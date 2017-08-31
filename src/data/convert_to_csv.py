import pandas as pd
import os
import glob
from tqdm import tqdm
import bz2
import click


@click.command()
@click.option('--dir', default="**", help='The data folder you want to merge')
def merge(dir):
    data_dir = "data"
    od = "" if dir == "**" else dir
    output_file = os.path.join(data_dir, "data_{0}.csv.bz2".format(od))
    if os.path.isfile(output_file):
        os.unlink(output_file)
    with bz2.BZ2File(output_file, 'wb') as f:
        files = glob.glob(os.path.join(data_dir, dir, "*.pkl"))

        # read the first file and write it with headers
        df = pd.read_pickle(files[0])
        df.to_csv(f, header=True, encoding='windows-1255')
        del df
        for fileName in tqdm(files[1:]):
            # write all other files without headers
            df = pd.read_pickle(fileName)
            df.to_csv(f, header=False, encoding='windows-1255')
            del df


if __name__ == '__main__':
    merge()
