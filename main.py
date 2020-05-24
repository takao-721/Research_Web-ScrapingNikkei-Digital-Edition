import sys
import MeCab
import requests as web

titles = ["ノキア、4G+5Gで世界最速　エリクソンやサムスン超す",
              "養殖マグロ水揚げAIでタイミングよく　豊田通商とNEC",
              "パナ子会社ATOUN、着るロボットで遠隔フィットネス"]



for title in titles:
    m = MeCab.Tagger ("mecabrc")
    print(m.parse (title))
    target_words = m.parse (title).split()
    for index in range(len(target_words)):
        target_words[index] = target_words[index][:target_words[index].find(",*")-1] 
        #if target_words[index] == '':
        #    target_words.remove('')
    print(target_words)