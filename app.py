from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return a

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    userText = decoded['queryResult']['intent']['displayName']
    #sendText(user,userText)
    if (userText == 'สวัสดีตอนเช้า') :
        sendText(user,'ดีเช่นกัน')
    elif (userText == 'นนท์อยากกินอะไรครับ') :
        sendText(user,'ซูซิ!!!')
    elif (userText == 'อยากดื่มอะไรไหม') :
        sendText(user,'ชาเขียวมัมชะ++ เลี้ยงใช้ปะ')
    elif (userText == 'เลี้ยงจ้า') :
        sendText(user,'เย้ มีเมียเป็นพี่รหัสมันดีอย่างนี้นี่เอง')
    elif (userText == 'ใครน่ารัก') :
        sendText(user,'ฉันนะสิ ฉันนะสิ')
    elif (userText == 'อยู่ไหนเนี่ย') :
        sendText(user,'อยู่ในใจพี่ตลอดไป')
    elif (userText == 'นนท์อยากไปเที่ยวไหน') :
        sendText(user,'นนท์อยากไปญี่ปุ่น แล้วพี่อยากไปเที่ยวไหน')
    elif (userText == 'พี่อยากไปเยอรมัน') :
        sendText(user,'เก็บตัง รอแต่งงาน แล้วไปเที่ยวรอบโลกกัน')
    elif (userText == 'โอ้ย') :
        sendText(user,'พี่อย่าเล่นตัว ')
    elif (userText =='นนท์นี่') :
        sendText(user,'จ๋าพี่ ')
    else :
        sendText(user,'ไม่พบคำสั่ง')
    return '',200
def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
