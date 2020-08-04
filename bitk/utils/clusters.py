# AUTOGENERATED! DO NOT EDIT! File to edit: 04_utils_clusters.ipynb (unless otherwise specified).

__all__ = ['clusters_annotation', 'ass_methods', 'cluster_methods', 'find_peak_valley', 'find_best_cluster_number']

# Cell

from scipy.signal import find_peaks
from sklearn.cluster import MiniBatchKMeans,AgglomerativeClustering,\
                            SpectralClustering,DBSCAN,OPTICS,AffinityPropagation,\
                            AgglomerativeClustering,Birch
from sklearn.metrics import silhouette_score,calinski_harabasz_score,davies_bouldin_score
import numpy as np

# Cell

def clusters_annotation(df,method,params):
    if method not in [MiniBatchKMeans,AgglomerativeClustering,
                      SpectralClustering,DBSCAN,OPTICS,AffinityPropagation,
                      AgglomerativeClustering,Birch]:
        raise ValueError('method should be in sklearn.cluster.*, e.g. DBSCAN')
    if method in [MiniBatchKMeans,AgglomerativeClustering,SpectralClustering,Birch]:
        cluster= method(n_clusters=params['n_clusters'])
    elif method in [DBSCAN,OPTICS]:
        cluster=method(eps=params['eps'])
    elif method == AffinityPropagation:
        cluster=method(damping=params['damping'], preference=params['preference'])
    clustering = cluster.fit_predict(df)
    return clustering

ass_methods={
    'silhouette_score':silhouette_score,
    'calinski_harabasz_score':calinski_harabasz_score,
    'davies_bouldin_score':davies_bouldin_score
}

cluster_methods={
    'MiniBatchKMeans':MiniBatchKMeans,
    'AgglomerativeClustering':AgglomerativeClustering,
    'SpectralClustering':SpectralClustering,
    'DBSCAN':DBSCAN,
    'OPTICS':OPTICS,
    'AffinityPropagation':AffinityPropagation,
    'AgglomerativeClustering':AgglomerativeClustering,
    'Birch':Birch
}

# Cell

def find_peak_valley(sequence,peak=True):
    if peak:
        peaks, _ =  find_peaks(sequence)
        return peaks
    else:
        peaks, _ = find_peaks(-sequence)
        return peaks


def find_best_cluster_number(df,cluster_method,params,ass_method=silhouette_score):
    records = []
    if cluster_method in [MiniBatchKMeans,AgglomerativeClustering,SpectralClustering,Birch]:
        for i in range(2,20):
            params['n_clusters'] = i
            clustering = clusters_annotation(df,cluster_method,params)
            records.append([i,ass_method(df,clustering)])
    elif cluster_method in [DBSCAN,OPTICS]:
        for i in np.arange(0.1,4,0.2):
            params['eps']=i
            clustering = clusters_annotation(df,cluster_method,params)
            if sum(clustering) == -len(clustering):
                records.append([i,0])
            else:
                records.append([i,ass_method(df,clustering)])

    records = np.array(records)
#     peaks, _ =  find_peaks(records[:,1])
    if ass_method == silhouette_score:
        peaks = find_peak_valley(records[:,1])
        if len(peaks) == 0:
            return records,records,peaks
        return records[peaks[0]],records,peaks
    elif ass_method == calinski_harabasz_score:
        peaks = find_peak_valley(records[:,1])
        if len(peaks) == 0:
            return records,records,peaks
        return records[peaks[0]],records,peaks
    elif ass_method == davies_bouldin_score:
        peaks = find_peak_valley(records[:,1],False)
        if len(peaks) == 0:
            return records,records,peaks
        return records[peaks[0]],records,peaks
    else:
        raise ValueError('ass method can only be one of [silhouette_score,calinski_harabasz_score,davies_bouldin_score]')

