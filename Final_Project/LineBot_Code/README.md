# Line Bot

本專案使用 Python LINE Bot SDK 在 Heroku 上架設 反洗錢小博士 機器人。

## 在你開始之前

確保您具有以下內容：

- 擁有 Line 帳號
- 擁有 [Heroku](https://www.heroku.com) 帳戶
- 本專案所使用之 資料庫 host 和 password


## 程式檔案解說

> 資料夾裡需含有兩份文件來讓你的程式能在 heroku 上運行

- Procfile：heroku 執行命令，web: {語言} {檔案}，這邊語言為 python，要自動執行的檔案為 app.py，因此我們改成 **web: python app.py**。
- requirements.txt：列出所有用到的套件，heroku 會依據這份文件來安裝需要套件
- app.py : 聊天機器人的主程式 

## 參考資料

-更詳細之架設教學考參考 [Github](https://github.com/yaoandy107/line-bot-tutorial)