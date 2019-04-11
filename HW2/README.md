# EDA流程報告
## 收集資料
1. 針對自訂議題收集相關文本
## 清洗資料&特徵擷取（文字探勘共現性） [Co-Occurrence Matrix - code](https://github.com/tzuhuailin/2019_Fintech_Text_Mining_and_Machine_Learning/blob/master/HW2/Co-Occurrence%20Matrix.ipynb)
2. 將收集到的文本用NER挑選出【自定義類別】例如：人名與事件 (可考慮以句子為單位，或是以不同文本來源為彙整文件的基準)。
   + NER：命名實體識別技術(Named Entity Recognition)是嘗試透過先將一個句子分詞以及做詞性標注,然後根據已有的實體資料庫來做判讀。對電腦來說,分詞後的結果雖然算是分離出意義的最小單位卻仍無法操作該意義單位,因為詞彙數據有稀疏的特性(意思是說,一個詞彙和另一個詞彙之間的關係不像整數一樣存在必然的關係,也沒有數學上的特性), 命名實體識別技術可以讓電腦將詞彙和實體連結在一起。
3. 將文件與有分類過的單詞進行 TDM (term to matrix)。
4. 將 TDM 轉成 Co-Occurrence Matrix。
## 資料視覺化
5. 繪製出各類別之間的共現圖，例如：嫌疑犯和各犯罪行為之間的共現圖。
* [熱度圖(程式末端)](https://github.com/tzuhuailin/2019_Fintech_Text_Mining_and_Machine_Learning/blob/master/HW2/Co-Occurrence%20Matrix.ipynb)
* [Co-Occurrence network map](https://github.com/tzuhuailin/2019_Fintech_Text_Mining_and_Machine_Learning/blob/master/HW2/co-occurrence%20network%20map.png) : Co-Occurrence network map是以Gephi製作
----

## 探索式資料分析(Exploratory Data Abalysis, EDA)
1. 收集資料
2. 清洗資料
3. 特徵擷取
4. 資料視覺化

## EDA分析流程範例
1. 統計各 ID 有多少則消息。Comparison (類別 x 數值)
2. 依照不同時間週期來比較各 ID 所回應的消息數量。Composition (類別 x 數量)
3. 以 ID 來合併每則消息 (思考時間要如何納入？以月為單位？)。
4. 透過jieba將每則訊息的單詞擷取出來。
a. POS: 單詞可對應到【詞性】。
b. NER: 單詞可對應到【自定義類別】，例如人、事、時、地、物、組織...等。
5. 將所有單詞進行聯集；(只挑有意義的 NER or POS，省略不帶意義的單詞)。
6. 可使 ID 和各聯集單詞成為一個稀疏矩陣。
7. 將稀疏矩陣重建為 co-occurrence matrix。
8. 就可以畫出【共現圖】與【熱點圖】
   + 共現圖：https://pythondata.com/text-analytics-visualization/
   + 熱點圖：https://data-flair.training/blogs/python-heatmap-word-cloud/

## Text Minging
1. 關鍵文件預處理
2. 關鍵字抽取
3. 關鍵句抽取
4. 主題抽取
5. 監督式文字探勘：透過模型與對應關係的建構，得到可以預期或是有預測能力的特定資料輸出
6. 非監督式文字探勘：透過資料處理與聚合讓資料替自己說話，對於資料輸出的情況無法預測，不可能在事前因為對過往模型的熟悉而有相關的預測能力，資料最後輸出的型態完全取決於目前資料自身的特性與型態，我們只是透過特定的邏輯與方法，來呈現資料自身原來的樣貌
7. 相關性結論
