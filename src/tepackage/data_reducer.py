from enum import IntEnum
from typing import Any, TYPE_CHECKING
from numpy.typing import NDArray

if TYPE_CHECKING:
    import matplotlib.pyplot as plt

class Reducer(IntEnum):
    pca=1,
    pacmap=2,
    tsne=3,
    mds=4,
    lle=5,


class DataReducer:
    __slots__ = ('reducer_method', 'dimensions', 'reducer')


    def __init__(self, reducer_method:Reducer, dimensions:int) -> None:

        self.reducer_method=reducer_method
        self.dimensions=dimensions


    def _setup_reducer(self, **kwargs:dict[str,Any]) -> None:
        kwargs.setdefault("n_components", self.dimensions)
        if self.reducer_method == Reducer.pca:
            from sklearn.decomposition import PCA
            self.reducer = PCA(**kwargs)
        elif self.reducer_method == Reducer.mds:
            from sklearn.manifold import MDS
            self.reducer = MDS(**kwargs)       
        elif self.reducer_method == Reducer.lle:
            from sklearn.manifold import LocallyLinearEmbedding
            self.reducer = LocallyLinearEmbedding(**kwargs)
        elif self.reducer_method == Reducer.pacmap:
            from pacmap import PaCMAP
            self.reducer = PaCMAP(**kwargs)

        elif self.reducer_method == Reducer.tsne:
            from sklearn.manifold import TSNE
            self.reducer = TSNE(**kwargs)
        else:
            raise NotImplementedError('Unknown reducer type')

    def reduce(self, data:NDArray, **kwargs:dict[str,Any]) -> NDArray:
        self._setup_reducer(**kwargs)
        return self.reducer.fit_transform(data)


def plot_reduced_data(latent_data:NDArray,
                       title:str='Reduced data',
                        plot_dimensions:tuple[int,int] = (0,1),
                       **kwargs) -> "plt.Figure":

        import matplotlib.pyplot as plt
        import numpy as np

        title = kwargs.pop("plot_title", title)
        kwargs.setdefault("alpha", 0.8)
        kwargs.setdefault("s", 1)

        fig = plt.figure()

        normalized_indices = np.linspace(0, 1, latent_data.shape[0])
        scatter = plt.scatter(
            latent_data[:, plot_dimensions[0]],
            latent_data[:, plot_dimensions[1]],
            c=normalized_indices,
            cmap="coolwarm",
            **kwargs,
        )

        plt.colorbar(scatter, label="Normalized Time")

        plt.title(title)
        plt.xlabel(f"Dimension {plot_dimensions[0]+1}")
        plt.ylabel(f"Dimension {plot_dimensions[1]+1}")
        plt.gcf()
        return fig