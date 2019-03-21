# HW1

## ETF crawler

## Financial index crawler - US Non-farm Payrolls
 * Data Sourse: https://beta.bls.gov/dataViewer/view/timeseries/CES0000000001
 * [Financial index crawler - code](https://github.com/tzuhuailin/2019_Fintech_Text_Mining_and_Machine_Learning/blob/master/HW1/Financial%20Index%20crawler%20new_US%20Non-farm%20Payrolls.ipynb)
 * [Financial index crawler - flowchart](https://github.com/tzuhuailin/2019_Fintech_Text_Mining_and_Machine_Learning/blob/master/HW1/Financial%20index%20crawler_Flowchart.pdf)
 * Steps:
   1. Use requests and beautifulsoup package to find the min and max year of the existing database
   2. Use requests.post() function to ask for the data
   3. Use cvs reader and IO package to turn the requested data as cvs document
   4. Use panda package to turn the document as dataframe and show the first 20 rows of the data
