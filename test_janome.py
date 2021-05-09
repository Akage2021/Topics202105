# Janomeを使うための宣言 --- (*1)
from janome.tokenizer import Tokenizer
# Janomeの準備 --- (*2)
tok = Tokenizer()
# 形態素に分割 --- (*3)
tokens = tok.tokenize("今日は家族でラーメンを食べに行った。")
# 分割結果を確認 --- (*4)
for t in tokens:
   print(t)