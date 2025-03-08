# Unsupervised Report

## Methodology

The unsupervised approach involves dimensionality reduction followed by clustering. 

### Dimensionality Reduction

Five methods were tested: Principal Component Analysis (PCA) (Jolliffe, 1986), PaCMAP (Wang et al., 2021), t-Distributed Stochastic Neighbor Embedding (t-SNE) (van der Maaten & Hinton, 2008), Multidimensional Scaling (MDS) (Kruskal, 1964a, 1964b; Borg & Groenen, 1997), and Locally Linear Embedding (LLE) (Roweis & Saul, 2000). PCA is efficient and preserves global structure but may miss nonlinear relationships. PaCMAP balances local and global structures better than t-SNE but can scatter data. t-SNE captures local similarities well but struggles with global structure and is computationally expensive. MDS preserves distances but is sensitive to noise, while LLE retains local structures but may introduce distortions. PCA is the most computationally efficient, while t-SNE and PaCMAP are better for clustering visualization.

### Clustering Methods

Latent spaces were clustered using K-Means (Scikit-learn, n.d.), DBScan (Ester et al., 1996), and HDBScan (Campello et al., 2013, 2015). K-Means minimizes intra-cluster variance but requires a predefined number of clusters and struggles with non-spherical data. DBScan detects clusters of varying shapes without a fixed number but is sensitive to parameter tuning. HDBScan improves on DBScan by adapting density thresholds, making it more robust but computationally expensive. K-Means is efficient for simple cases, while DBScan and HDBScan handle complex structures better.

## Results and discussion

Add Discussion here

## References

Borg, I., & Groenen, P. (1997). *Modern Multidimensional Scaling - Theory and Applications*. Springer Series in Statistics.

Campello, R. J., Moulavi, D., & Sander, J. (2013). Density-based clustering based on hierarchical density estimates.

Campello, R. J., Moulavi, D., Zimek, A., & Sander, J. (2015). Hierarchical density estimates for data clustering, visualization, and outlier detection.

Ester, M., Kriegel, H. P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. In *Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining* (pp. 226-231). AAAI Press.

Jolliffe, I. T. (1986). *Principal Component Analysis*. Springer.

Kruskal, J. B. (1964a). Nonmetric multidimensional scaling: A numerical method. *Psychometrika, 29*, 115-129.

Kruskal, J. B. (1964b). Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis. *Psychometrika, 29*, 1-27.

Roweis, S., & Saul, L. (2000). Nonlinear dimensionality reduction by locally linear embedding. *Science, 290*, 2323-2326.

Scikit-learn. (n.d.). Principal Component Analysis (PCA). Retrieved from https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

Scikit-learn. (n.d.). t-Distributed Stochastic Neighbor Embedding (t-SNE). Retrieved from https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html

Scikit-learn. (n.d.). Multidimensional Scaling (MDS). Retrieved from https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html

Scikit-learn. (n.d.). Locally Linear Embedding (LLE). Retrieved from https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html

Scikit-learn. (n.d.). K-Means clustering. Retrieved from https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

Scikit-learn. (n.d.). DBSCAN clustering. Retrieved from https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html

Scikit-learn. (n.d.). HDBSCAN clustering. Retrieved from https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html

Wang, Y., Huang, H., Rudin, C., & Shaposhnik, Y. (2021). Understanding how dimension reduction tools work: An empirical approach to deciphering t-SNE, UMAP, TriMap, and PaCMAP for data visualization. *Journal of Machine Learning Research, 22*(201), 1-73. Retrieved from http://jmlr.org/papers/v22/20-1061.html

