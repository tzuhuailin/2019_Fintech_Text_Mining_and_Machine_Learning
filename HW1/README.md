# HW1

## ETF crawler - Technology Equity ETF
 * 使用的套件：requests
 * 原因：Requests是用Python語言編寫，基於urllib，採用Apache2 Licensed開源協議的HTTP庫。它比urllib更加方便，可以節約我們大量的工作，完全滿足      HTTP測試需求。Requests的哲學是以PEP20為中心開發的，所以它比urllib更加Pythoner。且支持Python3。
 * 流程
   1. 用requests.get抓取目標網址
   2. 網址後面加上目標ETF的名稱與要抓取的時間
   3. 抓下來存成BeautifulSoup類型
   4. 取出bs中需要的字串
   5. 分解字串並把時間和價格存成dictionary
   6. 把每一個etf的dictionary存成dataframe
 * 可能遇到的錯誤
   1. 在函式裡改dataframe但最後print的時候dataframe沒變 -> 函式最後return把dataframe指派給主程式的dataframe
   2. FileNotFoundError -> 確認Technology Equity ETF List (75).csv在資料夾中
   3. ImportError -> 確認安裝每一個所需模組
   4. dataframe的合併使用join會使得後面的key值若沒有出現在第一行的key則不會出現 -> 使用merge
   5. merge合併預設使用inner也就是兩邊都有的key才會保留 -> 使用how='outer'
   6. 抓下來的資料並沒有照時間順序 -> 排序dataframe
   
## Financial index crawler - US Non-farm Payrolls
 * Data Sourse: https://beta.bls.gov/dataViewer/view/timeseries/CES0000000001
 * [Financial index crawler - code](https://github.com/tzuhuailin/2019_Fintech_Text_Mining_and_Machine_Learning/blob/master/HW1/Financial%20Index%20crawler%20new_US%20Non-farm%20Payrolls.ipynb)
 * [Financial index crawler - flowchart](https://github.com/tzuhuailin/2019_Fintech_Text_Mining_and_Machine_Learning/blob/master/HW1/Financial%20index%20crawler_Flowchart.pdf)
 * Steps:
   1. Use requests and beautifulsoup package to find the min and max year of the existing database
   2. Use requests.post() function to ask for the data
   3. Use cvs reader and IO package to turn the requested data as cvs document
   4. Use panda package to turn the document as dataframe and show the first 20 rows of the data
 * 可能遇到的錯誤
   1. BLS Beta Labs的資料下載並非直接連結到檔案網址，而是送出一個form，因此不能以request.get()抓資料，而要以request.post()並輸入form所要求的資訊(selectedSeriesIds、startYear和endYear)
   2. 所送出的form當中資料可及的startYear與endYear需另外用requests和beautifulsoup從下拉式表單爬
   3. 前一步驟爬下來的年份為String，記得轉成數字格式才能做比較
