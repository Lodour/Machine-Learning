# 近邻法

## 最近邻法
> 最近邻法源于这样一种直观的想法：
> 对于一个新样本，把它逐一与已知样本比较，找出距离新样本最近的已知样本，以该样本的类别作为新样本的类别。

已知具有$N$个样本的$c$类样本集$S_N=\\{({\bf x}_i, \omega_j)|1\le i\le N, 1\le j\le c\\}$，其中${\bf x}_i$是样本$i$的$k$维特征列向量$(x_1, x_2, ..., x_k)^T$，$\omega_i$是样本对应的类别，定义两个样本间的距离度量$\delta({\bf x}_i, {\bf x}_j)$。

* 若采用欧式距离，则有$\delta({\bf x}_i, {\bf x}_j) = \sqrt{({\bf x}_i-{\bf x}_j)^T({\bf x}_i-{\bf x}_j)}$

* 若采用马氏距离，则有$\delta({\bf x}_i, {\bf x}_j) = \sqrt{({\bf x}_i-{\bf x}_j)^T\Sigma^{-1}({\bf x}_i-{\bf x}_j)}$，其中$\Sigma$是样本集$S_N$的协方差矩阵。

对于未知样本${\bf x}$，将其决策为$\omega_j$类当且仅当${\bf x}_i\in\omega_j, i=\arg\min_{i=1,2,...,N}{\delta({\bf x}, {\bf x}_i)}$
