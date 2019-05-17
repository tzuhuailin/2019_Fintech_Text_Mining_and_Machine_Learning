HW4 ETF績效評比
* 前置作業
1. 報酬率(R_t)=(〖NAV〗_t-〖NAV〗_(t-1))/〖NAV〗_(t-1) 
2. 風險溢酬(RP_t )=R_t-無風險利率(r_f)：因為承擔風險而產生的報酬
3. 無風險利率抓美國公債最短市場利率然後平均(隨便抓幾年平均即可)
4. 13 week Treasury Bill 歷史市場交易利率: https://finance.yahoo.com/quote/%5EIRX/history?p=%5EIRX
5. 因為利率是年化的所以算月報酬要除以12，週報酬除以52
6. 因為作業要求分別算週報酬與月報酬，週報酬就留每一筆ETF週五的資料就好，月報酬就留每一筆的月底資料，然後再算報酬率。

* 2009_JBF_Portfolio performance evaluation with generalized Sharpe ratios - ASKSR: 請用第 38 式
1. 第38式的ASKSR為改良Sharpe ratio，將超額溢酬的第三動差與第四動差納入考量。
2. 遇到的問題: ASKSR代入風險溢酬後可能會有呈現虛根的情況
3. 若有虛根的情況，則改用第20式的ASSR，僅考慮到第三動差的改良Sharpe ratio
4. 承上所述，此篇指標是改良式的Sharpe ratio，Sharpe ratio原始定義是風險溢酬與承擔的風險的比例，Sharpe ratio越高代表承擔一單位風險的風險溢酬越多，因此Sharpe ratio越高越好。

* 2011_JBF_Omega performance measure and portfolio insurance: 請用第 8 式，L＝無風險利率
1. Omega當中的報酬需代入未扣除無風險利率的原始報酬
2. Omega也是改良Sharpe ratio的一種，但它的風險不是用變異數衡量而是以賠錢的時候平均賠多少為指標

* 013_EL_A global index of riskiness: 請用 p.494 中之 Q(g)
1. 概念: <br/>
 E[ui(w+g)] > ui(w) <br/>
 w為原始資產，對投資人而言投資此產品的期望效益(g，可正可負)要大於原始資產的期望效益才會願意投資。 <br/>
 E[e^(-α_g g) ]=1 <br/>
 以指數函數當效用函數，然後根據先前假設，投資人要覺得投資後的期望財富效用大於等於投資前的原始財富效用時才會投資。這個式子假設原始財富是0，所以e^0=1，所以期望的帶來的報酬g乘上風險趨避程度之後的期望效用要等於e^0的原始財富效用。當產品的期望風險溢酬(g)品質越好(考量平均和變異數等等)，α_g也會越大。
 


