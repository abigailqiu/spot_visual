from gensim.models import Word2Vec
from src.config import MODEL_PATH, CLUSTERS_PATH
from umap import UMAP
import pandas as pd
from sklearn.cluster import HDBSCAN

def get_clusters():
    model = Word2Vec.load(str(MODEL_PATH))
    umap_3d = UMAP(n_components = 3, n_neighbors = 15, min_dist = 0.1, metric = "cosine", random_state = 42)
    umap_trans_3d = umap_3d.fit_transform(model.wv.vectors)
    clusterer = HDBSCAN(min_cluster_size=20)
    labels_3d = clusterer.fit_predict(umap_trans_3d)
    uri_list = model.wv.index_to_key
    clustered_data = pd.DataFrame({'uri': uri_list, 'x': umap_trans_3d[:, 0], 'y': umap_trans_3d[:, 1], 'z': umap_trans_3d[:, 2], 'cluster': labels_3d})
    return clustered_data

if __name__ == "__main__":
    clustered_data = get_clusters()
    clustered_data.to_csv(CLUSTERS_PATH, index=False)

