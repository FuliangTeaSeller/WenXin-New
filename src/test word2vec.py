from gensim.models import KeyedVectors

# model = KeyedVectors.load_word2vec_format('cn.cbow.bin', binary=True, encoding='utf-8', errors='replace')
model = KeyedVectors.load_word2vec_format( 'cn.cbow.bin', binary=True, unicode_errors='ignore')
# similarities = []
text_A = ['我', '爱', '吃', '苹果']
texts_B = [['我', '喜欢', '吃', '香蕉'], ['我', '喜欢', '吃', '苹果'], ['我', '喜欢', '吃', '橘子']]

# 加载Word2Vec模型
# model = KeyedVectors.load_word2vec_format('cn.cbow.bin', binary=True)

# 计算文本相似度并找到最佳匹配
best_match = None
best_similarity = -1

for text_B in texts_B:
    similarity = model.n_similarity(text_A, text_B)
    if similarity > best_similarity:
        best_similarity = similarity
        best_match = text_B

print("最佳匹配文本：", best_match)


