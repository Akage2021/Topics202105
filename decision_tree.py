import numpy as np

# 不純度を計算します
def calc_impurity(data, labels):
   feature_num = data.shape[1]
   threshold = None
   feature = None
   impurity = 1
   for index in range(feature_num):
       for value in data[:, index]:
           sum_impurity = 0
           # ここではゲインを求める必要がないので不純度と重みの積の和まで求めます
           condition = data[:, index] >= value
           all_samples_num = len(labels)
           for column in [condition, np.logical_not(condition)]:
               I = 1
               partial_samples = labels[column]
               partial_samples_num = len(partial_samples)
               w = partial_samples_num/all_samples_num
               for _class in np.unique(partial_samples):
                   p = np.sum(partial_samples==_class)/partial_samples_num
                   I -= p**2
               sum_impurity += w*I
           # 最小の不純度となるものを記憶します
           if impurity > sum_impurity:
               impurity = sum_impurity
               threshold = value
               feature = index
   return impurity, threshold, feature

# 各ノードで計算は行われるのでノードをクラス化しました
class Node:

   def __init__(self, data, labels, max_depth):
       self.data = data
       self.labels = labels
       self.max_depth = max_depth
       self.children = []
       self.threshold = None
       self.feature = None
       self.depth = None
       self.impurity = None
       self.label = np.argmax(np.bincount(labels))

   # CART アルゴリズムの実行部分です
   def cart(self, depth=0):
       self.depth = depth
       self.impurity, self.threshold, self.feature = calc_impurity(self.data, self.labels)
       if self.impurity == 0 or self.depth == self.max_depth:
           return
       condition = self.data[:, self.feature] >= self.threshold
       for column in [condition, np.logical_not(condition)]:
           next_node = Node(self.data[column],  self.labels[column], self.max_depth)
           self.children.append(next_node)
           next_node.cart(self.depth + 1)

   # 予測します、自分が木の端点となるノードなら自分のクラス、子のノードがいるならそのノードの予測結果に委ねます
   def predict(self, data):
       if self.impurity == 0 or self.depth == self.max_depth:
           return self.label
       child_node_index = int(not data[self.feature] >= self.threshold)
       next_node = self.children[child_node_index]
       return next_node.predict(data)


# 決定木クラスです
class DecisionTree:

   # インスタンスを作る際に「最大の深さ」を指定します
   def __init__(self, max_depth):
       self.max_depth = max_depth
       self.tree = None

   # fit(データ, ラベル)とすることでノードクラスを呼び出し、学習します
   def fit(self, data, labels):
       self.tree = Node(data, labels, self.max_depth)
       self.tree.cart()

   # predict(テストデータ)とすることで予測を行います
   def predict(self, data):
       return np.array([self.tree.predict(sample) for sample in data])