from src.config import CLUSTERS_PATH, EXPORT_PATH, SCALE_CONSTANT, UPPER_BOUND, LOWER_BOUND
from src.sessions import get_tracks
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def export_clusters():
    tracks, play_count = get_tracks()
    clusters = pd.read_csv(CLUSTERS_PATH)
    clusters = clusters.merge(
        tracks[["track_name", "artist_name"]], 
        left_on = "uri", 
        right_index = True, 
        how = "left"
    )
    clusters = clusters.merge(play_count.rename("size"), left_on = "uri", right_index = True, how = "left") #series needs a name
    clusters["size"] = np.log(clusters["size"])
    clusters["size"] -= min(clusters["size"])
    clusters["size"] /= max(clusters["size"])
    clusters["size"] *= UPPER_BOUND - LOWER_BOUND 
    clusters["size"] += LOWER_BOUND

    clusters["x"] = SCALE_CONSTANT * (clusters["x"] - clusters.x.mean())
    clusters["y"] = SCALE_CONSTANT * (clusters["y"] - clusters.y.mean())
    clusters["z"] = SCALE_CONSTANT * (clusters["z"] - clusters.z.mean())

    num_colors = len(set(clusters["cluster"]))
    cmap = plt.colormaps['gist_ncar'].resampled(num_colors-1)
    cmap = [cmap(i) for i in range(num_colors-1)]
    cmap.append([0.3, 0.3, 0.3])

    clusters["r"] = [cmap[i][0] for i in clusters["cluster"]] 
    clusters["g"] = [cmap[i][1] for i in clusters["cluster"]] 
    clusters["b"] = [cmap[i][2] for i in clusters["cluster"]] 

    print(clusters.head())

    clusters.to_csv(EXPORT_PATH, index=False)

if __name__ == "__main__":
    export_clusters()
