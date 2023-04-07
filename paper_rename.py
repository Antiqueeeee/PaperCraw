

## 下载到了excel当中的所有论文，但是需要重新命名。。
#  难顶。。
import os
import json
import pandas as pd



paper_list = list()
data = pd.read_excel("data/学术论文汇总表.xlsx")
print(data.columns)
index,author,title,publish,system = list(),list(),list(),list(),list()
for i in range(data.shape[0]):
    index.append(data.iloc[i]['序号'])
    author.append(data.iloc[i]['第一作者'])
    title.append(data.iloc[i]['论文名称'])
    publish.append(data.iloc[i]['刊物名称'])
    system.append(data.iloc[i]['收录\n系统'])

existed_list = list()
for root,dirs,files in os.walk("data/20230407"):
    for file in files:
        _file = "".join(file.split(".")[:-1])
        try:
            _index = title.index(_file)
            os.rename(
                os.path.join(root,file),
                os.path.join(root, f"{index[_index]}.{author[_index]}-{file}")
            )
        except:
            pass



# paper_list = list()
# with open("data/english_paper.json",encoding="utf-8") as f:
#     english_paper = json.load(f)
#
#
# for paper in english_paper:
#     title = paper["论文名称"]
#     idx = paper["序号"]
#     author = paper["第一作者"]
#     min_length,index = 999,-1
#     for i,item in enumerate(existed_list):
#
#         if _ < min_length:
#             index = i
#             min_length = _
#     print(f"title:{title}\nnow:{existed_list[index]}")
#     # os.rename(
#     #     os.path.join(os.path.abspath("."),"data","20230407",existed_list[index] + ".pdf"),
#     #     os.path.join(os.path.abspath("."),"data","20230407",f"{idx}.{author}-{existed_list[index]}"+".pdf")
#     # )
#     print("",end="")
# #     if title in existed_list:
# #         os.rename(
# #             os.path.join(os.path.abspath("."),"data","20230407",title + ".pdf"),
# #             os.path.join(os.path.abspath("."),"data","20230407",f"{idx}.{author}-{title}")
# #         )
# #         print(title)
# # # 能直接匹配上的就4个。。







