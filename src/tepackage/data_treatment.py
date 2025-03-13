from enum import IntEnum
from typing import Any, TYPE_CHECKING
from numpy.typing import NDArray

if TYPE_CHECKING:
    import matplotlib.pyplot as plt

class Clusterer(IntEnum):
    kmeans=1,
    hdbscan=2,
    dbscan=3,



class DataClusterer:

    __slots__ = ('clusterer_method', 'clusterer', 'cluster_labels')


    def __init__(self, method:Clusterer) -> None:

        self.clusterer_method=method

    def _setup_clusterer(self,**kwargs:dict[str,Any]) -> None:

        if self.clusterer_method == Clusterer.kmeans:
            from sklearn.cluster import KMeans

            kwargs.setdefault("random_state", 42)
            kwargs.setdefault("n_clusters", 2)

            self.clusterer = KMeans(**kwargs)

        elif self.clusterer_method == Clusterer.hdbscan:
            from sklearn.cluster import HDBSCAN

            kwargs.setdefault("min_cluster_size", 35)
            self.clusterer = HDBSCAN(**kwargs)

        elif self.clusterer_method == Clusterer.dbscan:
            from sklearn.cluster import DBSCAN

            kwargs.setdefault("eps", 0.5)
            kwargs.setdefault("min_samples", 5)

            self.clusterer = DBSCAN(**kwargs)
        else:
            raise NotImplementedError('Unknown clusterer method')

    def clusterize(self, data:NDArray, **kwargs:dict[str,Any]) -> NDArray:
        self._setup_clusterer(**kwargs)

        self.cluster_labels = self.clusterer.fit_predict(data)


def plot_clustering_2d(data:NDArray, labels:NDArray, show_noise: bool = True, 
                 title:str='Clustering Results',
                 plot_indexes:tuple[int,int] = (0,1),
                 **kwargs: Any) -> "plt.Figure":
    
    
    import matplotlib.pyplot as plt
    from tepackage.shared import PLOT_MARKERS
    from copy import copy

    from matplotlib import cm

    kwargs.setdefault("alpha", 0.8)
    kwargs.setdefault("s", 1)

    fig = plt.figure()
    unique_labels = set(labels)

    colormap = cm.get_cmap("tab10", len(unique_labels))
    colors = [colormap(i) for i in range(len(unique_labels))]

    markers = copy(PLOT_MARKERS)

    for label, color in zip(unique_labels, colors):

        marker = markers.pop()
        if len(markers) == 0:
            markers = copy(PLOT_MARKERS)

        if label == -1 and not show_noise:
            continue

        if label == -1:
            color = "red"
            marker = "."
            kwargs["alpha"] = 0.5
            kwargs["edgecolor"] = "none"
        else:
            color = color
            marker = marker

        plt.scatter(
            data[labels == label, plot_indexes[0]],
            data[labels == label, plot_indexes[1]],
            color=color,
            marker=marker,
            label=f"Cluster {label}" if label != -1 else "Noise",
            **kwargs,
        )

    plt.title(title)
    plt.xlabel(f"Component {plot_indexes[0]+1}")
    plt.ylabel(f"Component {plot_indexes[1]+1}")

    plt.legend(
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        title="Legend",
    )
    plt.tight_layout()
    plt.gcf()
    
    return fig