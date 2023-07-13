import json
import jieba

# 加载prompts_list.json文件
file_path = "./resource/prompts.json"  # 指定文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    prompts = json.load(file)

# 加载停用词列表
stopwords_file = "./resource/stopword.txt"  # 停用词文件路径
with open(stopwords_file, 'r', encoding='utf-8') as file:
    stopwords = [line.strip() for line in file]

# 分词和处理
processed_prompts = []
for prompt in prompts:
    processed_prompt = {
        "title": prompt["title"],
        "content": prompt["content"],
        "note": prompt["note"]
    }

    # 分词处理
    words = list(jieba.cut(prompt["title"] + prompt["content"] + prompt["note"]))
    filtered_words = [word for word in words if word not in stopwords]
    processed_prompt["processed"] = filtered_words

    processed_prompts.append(processed_prompt)

# 保存处理后的结果
output_file_path = "./resource/processed_prompts.json"  # 指定输出文件路径
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(processed_prompts, file, ensure_ascii=False, indent=4)
