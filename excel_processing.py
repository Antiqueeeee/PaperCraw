import pandas as pd
from tqdm import tqdm,trange
import time
import json
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


### excel中有需要下载的文献信息，包括中文文献和英文文献
#中文文献：在CNKI中下载文献，使用爬虫填入论文标题信息 + debug + 手动下载
#英文文献：在http://spis.hnlat.com/ 中检索下载文献
#          使用爬虫填入论文标题，然后捕获所有搜索结果，计算检索结果和论文标题的编辑距离
#          选中编辑距离最小的文献，点击下载
#          使用os工具获取下载路径中的所有文件，下载完成后再重新获取所有文件，对新增文件的文件名进行修改
def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

paper_all = pd.read_excel("data/paper_all.xlsx")
logger.info(paper_all.columns)
chinese_paper,english_paper = list(),list()
for i in trange(paper_all.shape[0]):
    paper = dict()
    for col in paper_all.columns:
        paper[col] = str(paper_all.iloc[i][col])
    if is_contain_chinese(paper["论文名称"]):
        chinese_paper.append(paper)
    else:
        english_paper.append(paper)

with open("data/chinese_paper.json","w",encoding="utf-8") as f:
    json.dump(chinese_paper,f,ensure_ascii=False,indent=2)

with open("data/english_paper.json","w",encoding="utf-8") as f:
    json.dump(english_paper,f,ensure_ascii=False,indent=2)