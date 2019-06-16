from flask import Flask, request, abort
import pymysql
import pandas as pd

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi("YOUR TOKEN")
# Channel Secret
handler = WebhookHandler("YOUR SECRET")

def Get_Data_From_Mysql_by_content(table_name,content,content_type):
    contents_list=[]
    target_ids =[]
    db = pymysql.connect(host="YOUR HOST",port=3306, user="public_author",passwd="YOUR PASSWORD",db="AML_News" ,charset='utf8')
    try:
        with db.cursor() as cursor:
            if(content_type is 'date'):
                sql0 = "SELECT * FROM `"+table_name+"` WHERE `"+content_type+"` LIKE '"+content+"'"
            else:
                sql0 = "SELECT * FROM `"+table_name+"` WHERE `"+content_type+"` LIKE CONCAT('%', '"+content+"','%')"
            cursor.execute(sql0)
            contents_list = cursor.fetchall()
                
        db.commit()
    finally:
        db.close()
    return  pd.DataFrame(list(contents_list), columns=['id','article','location','keyword','date','name'])

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(PostbackEvent)
def handle_postback(event):
    reply_token = event.reply_token
    data = event.postback.data
        
    if data == '沒有了':
        message = "共有 "+str(len(output_dataframe)) + " 筆資料符合 :\n"
        for index , row in output_dataframe.iterrows():
            message = message + "姓名 : " + name + "\n" + "地點 : " + row['location'] + "\n" + "犯罪類型 : " + row['keyword'] + "\n\n"
        message = TextSendMessage(message)
    elif data == '洗錢風險等級_高':
        filter = (output_dataframe["keyword"] == "毒品販運") | (output_dataframe["keyword"] == "詐欺") | (output_dataframe["keyword"] == "走私") | (output_dataframe["keyword"] == "稅務犯罪") | (output_dataframe["keyword"] == "證券犯罪") | (output_dataframe["keyword"] == "證券犯罪") | (output_dataframe["keyword"] == "貪污") | (output_dataframe["keyword"] == "賄落") | (output_dataframe["keyword"]=="洗錢")  
        if len(output_dataframe[filter]) == 0:
            message = TextSendMessage(text="查無此人 !")
        else:
            message = "共有 "+str(len(output_dataframe[filter])) + " 筆資料符合 :\n"
            for index , row in output_dataframe[filter].iterrows():
                message = message + "姓名 : " + name + "\n" + "地點 : " + row['location'] + "\n" + "犯罪類型 : " + row['keyword'] + "\n\n"
            message = TextSendMessage(message)                   
    elif data == '洗錢風險等級_中':
        filter = (output_dataframe["keyword"] == "販運武器") | (output_dataframe["keyword"] == "贓物") | (output_dataframe["keyword"] == "竊盜") | (output_dataframe["keyword"] == "綁架") | (output_dataframe["keyword"] == "拘禁") | (output_dataframe["keyword"] == "妨礙自由") | (output_dataframe["keyword"] == "環保犯罪") | (output_dataframe["keyword"] == "偽造文書")  
        if len(output_dataframe[filter]) == 0:
            message = TextSendMessage(text="查無此人 !")
        else:
            message = "共有 "+str(len(output_dataframe[filter])) + " 筆資料符合 :\n"
            for index , row in output_dataframe[filter].iterrows():
                message = message + "姓名 : " + name + "\n" + "地點 : " + row['location'] + "\n" + "犯罪類型 : " + row['keyword'] + "\n\n"
            message = TextSendMessage(message)
    elif data == '洗錢風險等級_低':
        filter = (output_dataframe["keyword"] == "人口販運") | (output_dataframe["keyword"] == "姓剝削") | (output_dataframe["keyword"] == "偽造貨幣") | (output_dataframe["keyword"] == "殺人") | (output_dataframe["keyword"] == "搶奪") | (output_dataframe["keyword"] == "勒續") | (output_dataframe["keyword"] == "海盜") | (output_dataframe["keyword"] == "資恐")  
        if len(output_dataframe[filter]) == 0:
            message = TextSendMessage(text="查無此人 !")
        else:
            message = "共有 "+str(len(output_dataframe[filter])) + " 筆資料符合 :\n"
            for index , row in output_dataframe[filter].iterrows():
                message = message + "姓名 : " + name + "\n" + "地點 : " + row['location'] + "\n" + "犯罪類型 : " + row['keyword']  + "\n\n"
            message = TextSendMessage(message)

    elif data == '地點_北部':
        filter = (output_dataframe["location"] == "台北") | (output_dataframe["location"] == "基隆") | (output_dataframe["location"] == "新北") | (output_dataframe["location"] == "桃園") | (output_dataframe["location"] == "新竹") | (output_dataframe["location"] == "苗栗")
        if len(output_dataframe[filter]) == 0:
            message = TextSendMessage(text="查無此人 !")
        else:
            message = "共有 "+str(len(output_dataframe[filter])) + " 筆資料符合 :\n"
            for index , row in output_dataframe[filter].iterrows():
                message = message + "姓名 : " + name + "\n" + "地點 : " + row['location'] + "\n" + "犯罪類型 : " + row['keyword'] + "\n\n"
            message = TextSendMessage(message)
        
    elif data == '地點_中部':
        filter = (output_dataframe["location"] == "台中") | (output_dataframe["location"] == "彰化") | (output_dataframe["location"] == "雲林") | (output_dataframe["location"] == "嘉義") | (output_dataframe["location"] == "南投")
        if len(output_dataframe[filter]) == 0:
            message = TextSendMessage(text="查無此人 !")
        else:
            message = "共有 "+str(len(output_dataframe[filter])) + " 筆資料符合 :\n"
            for index , row in output_dataframe[filter].iterrows():
                message = message + "姓名 : " + name + "\n" + "地點 : " + row['location'] + "\n" + "犯罪類型 : " + row['keyword']  + "\n\n"
            message = TextSendMessage(message)
        
    elif data == '地點_南部':
        filter = (output_dataframe["location"] == "台南") | (output_dataframe["location"] == "高雄") | (output_dataframe["location"] == "屏東")
        if len(output_dataframe[filter]) == 0:
            message = TextSendMessage(text="查無此人 !")
        else:
            message = "共有 "+str(len(output_dataframe[filter])) + " 筆資料符合 :\n"
            for index , row in output_dataframe[filter].iterrows():
                message = message + "姓名 : " + name + "\n" + "地點 : " + row['location'] + "\n" + "犯罪類型 : " + row['keyword'] + "\n\n"
            message = TextSendMessage(message)
#    elif data == '108年':
#        message = TextSendMessage(text="敬啟期待此功能上線～")
#    elif data == '107年':
#        message = TextSendMessage(text="敬啟期待此功能上線～")
#    elif data == '106年以前':
#        message = TextSendMessage(text="敬啟期待此功能上線～")
        
    line_bot_api.reply_message(reply_token, message)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_token = event.reply_token
    if user_message == '新聞':
        # TODO...    
        message = TextSendMessage(text=user_message)
        line_bot_api.reply_message(reply_token, message)

    else:
        global name
        global table_name
        global output_dataframe 
        
        table_name = 'group_11'
        name = event.message.text
        content_type = 'name'
        
        output_dataframe = Get_Data_From_Mysql_by_content( table_name , name , content_type )
        
        if len(output_dataframe) == 0:
            message = TextSendMessage(text="查無此人 !")
        else :
            message = TemplateSendMessage(alt_text='是否還有其他詳細資訊',
                                          template=CarouselTemplate(
                                                  columns=[
                                                          CarouselColumn(
                                                                  title='是否還有其他資訊',
                                                                  text='沒有了',
                                                                  actions=[                                                                
                                                                          PostbackTemplateAction(label='沒有了',data='沒有了'),
                                                                          PostbackTemplateAction(label='沒有了',data='沒有了'),
                                                                          PostbackTemplateAction(label='沒有了',data='沒有了')                                                                           
                                                                          ]
                                                                  ),
                                                          CarouselColumn(
                                                                  title='是否還有其他資訊',
                                                                  text='洗錢風險等級',
                                                                  actions=[
                                                                          PostbackTemplateAction(label='高',data='洗錢風險等級_高'),
                                                                          PostbackTemplateAction(label='中',data='洗錢風險等級_中'),
                                                                          PostbackTemplateAction(label='低',data='洗錢風險等級_低')                                                                                                 
                                                                          ]
                                                                  ),
                                                          CarouselColumn(
                                                                  title='是否還有其他資訊',
                                                                  text='地點',
                                                                  actions=[
                                                                          PostbackTemplateAction(label='北部',data='地點_北部'),
                                                                          PostbackTemplateAction(label='中部',data='地點_中部'),
                                                                          PostbackTemplateAction(label='南部',data='地點_南部')
                                                                          ]
                                                                   )#,
#                                                          CarouselColumn(
#                                                                  title='是否還有其他資訊',
#                                                                  text='發生年份',
#                                                                  actions=[
#                                                                          PostbackTemplateAction(label='108',data='108年'),
#                                                                          PostbackTemplateAction(label='107',data='107年'),
#                                                                          PostbackTemplateAction(label='106以前',data='106年以前')
#                                                                          ]
#                                                                  )
                                                          ]
                                           )
                       )                                                                                                          
        line_bot_api.reply_message(reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
