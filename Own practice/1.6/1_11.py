"""
程式設計練習題 1-6 1-11 人口推算.

美國人口普查局根據以下假設來推算人口:
- 每7秒中有一個小孩出生
- 每13秒鐘有一個人死亡
- 每45秒鐘有一個新移民入境

請撰寫一程式，顯示接下來五年的人口數。假設目前人口為312,032,486，每年有365天。
提示:在Python中，如果兩個整數做除法運算，結果還是整數。小數點會被去掉。比方說，5//4結果會是1
(而不是1.25)，而10//4結果會是2(而不是2.5)。
"""

print((312032486 + (365 * 24 * 3600) // 7 - (365 * 24 * 3600) // 13 + (
       365 * 24 * 3600) // 45))
