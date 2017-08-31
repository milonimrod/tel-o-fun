import httplib
import urllib
import datetime
import json
import os
import time
import pandas as pd
headers = {
}

params = urllib.urlencode({
})


def convert_to_df(d):
    for entry in d["features"]:
        # update the coordinates to be long / lat
        entry["attributes"].update(entry["geometry"])
    df = pd.DataFrame.from_records([v["attributes"] for v in d["features"]])\
        .set_index("tachana_id")
    df["tr_idkun"] = pd.to_datetime(df["tr_idkun"], unit='ms')
    return df


try:
    conn = httplib.HTTPSConnection('api.tel-aviv.gov.il')
    conn.request("GET", "/telofan/Stations?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    data = json.loads(data)
    timestamp = int(time.time())
    output_dir = os.path.join("data",
                              datetime.datetime.now().strftime('%Y-%m'))
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    df = convert_to_df(data)
    print df.shape
    df.to_pickle(os.path.join(output_dir, "data_{0}.pkl".format(timestamp)))
    conn.close()
except Exception as e:
    print e
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
