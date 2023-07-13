from gensim.models import KeyedVectors
import jieba
import json
# 加载Word2Vec模型
model = KeyedVectors.load_word2vec_format( 'resource/cn.cbow.bin', binary=True, unicode_errors='ignore')

         
# def get_prompts(input_text):
#     # 只需要调用这个函数就可以了 计算文本相似度并找到最佳匹配
    
#     ret=[]
    
#     # 加载prompts_list.json文件
#     file_path = "./resource/processed_prompts.json"  # 指定文件路径
#     with open(file_path, 'r', encoding='utf-8') as file:
#         processed_prompts = json.load(file)
#     # 加载停用词列表
#     stopwords_file = "./resource/stopword.txt"  # 停用词文件路径
#     with open(stopwords_file, 'r', encoding='utf-8') as file:
#         stopwords = [line.strip() for line in file]    
#     cut_texts = list(jieba.cut(input_text))
#     filtered_words = [word for word in cut_texts if word not in stopwords]
    
#     best_match = None
#     best_similarity = -1
    
#     for processed_prompt in processed_prompts:
#         similarity = model.n_similarity(filtered_words, processed_prompt["processed"])
#         if similarity > best_similarity:
#             best_similarity = similarity
#             best_match = processed_prompt
    
#     print("\n最佳匹配文本：", best_match["title"]+'\n'+best_match["content"]+'\n'+best_match["note"])
#     print("\n输入分词：", filtered_words)
#     print("\n相似度：", best_similarity)
#     return best_match

def get_prompts(input_text):
    ret = []
    
    # 加载prompts_list.json文件
    file_path = "./resource/processed_prompts.json"  # 指定文件路径
    with open(file_path, 'r', encoding='utf-8') as file:
        processed_prompts = json.load(file)
    
    # 加载停用词列表
    stopwords_file = "./resource/stopword.txt"  # 停用词文件路径
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        stopwords = [line.strip() for line in file]    
    
    cut_texts = list(jieba.cut(input_text))
    filtered_words = [word for word in cut_texts if word not in stopwords]
    
    matches = []
    
    for processed_prompt in processed_prompts:
        similarity = model.n_similarity(filtered_words, processed_prompt["processed"])
        if similarity > 0.25:  # 只保留相似度大于0.25的部分
            matches.append((similarity, processed_prompt))
    
    matches.sort(reverse=True, key=lambda x: x[0])  # 按相似度排序
    
    top_matches = matches[:10]  # 最大10个元素
    print("\n-----------------------------------------------------------------------\n")
    for similarity, match in top_matches:
        # print("\n最佳匹配文本：", match["title"]+'\n'+match["content"]+'\n'+match["note"])
        # print("相似度：", similarity)
        ret.append(match)
    
    print("\n输入分词：", filtered_words)
    print("\n-----------------------------------------------------------------------\n")
    return ret



if __name__ == '__main__':
    while True:
        input_text = input("请输入：")
        get_prompts(input_text)




    