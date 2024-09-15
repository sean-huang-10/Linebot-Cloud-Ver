from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, LocationMessage, TextSendMessage ,FlexSendMessage ,PostbackEvent
from google.cloud import storage
from flask import request, abort
from line_flex import line_store_flex, flex_formmat, rice_class, noodle_class, dessert_class, big_food_class, local_class, line_bot_scraper_ifoodie, ifoodie_class, no_search
from get_api_keys import get_api_key
import functions_framework , googlemaps , requests

LINE_BOT_ACCESS_TOKEN = ''
LINE_BOT_SECRET = ''
GOOGLEMAPS_API_KEY =''
gmaps = None
line_bot_api = None
parser = None

user_states = 0
food_preference = ''

@functions_framework.http
def read_file_from_gcs(request):
    LINE_BOT_ACCESS_TOKEN = get_api_key('LINE_BOT_ACCESS_TOKEN.txt')
    LINE_BOT_SECRET = get_api_key('LINE_BOT_SECRET.txt')
    
    line_bot_api = LineBotApi(LINE_BOT_ACCESS_TOKEN)
    parser = WebhookParser(LINE_BOT_SECRET)
    
    try:
        # 獲取 X-Line-Signature header 的值
        signature = request.headers['X-Line-Signature']

        # 獲取請求體
        body = request.get_data(as_text=True)

        try:
            # 使用 WebhookParser 解析請求體
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            abort(400)

        # 處理事件
        for event in events:
            if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
                global user_states
                global food_preference
                user_message = event.message.text.strip()
                # 讓使用者選擇使用的功能
                if user_message == "美食推薦":
                    replymessage = FlexSendMessage(
                        alt_text='隨時即行傳送訊息',
                        contents=ifoodie_class()
                        )
                    line_bot_api.reply_message(event.reply_token, replymessage)
                    user_states = 1  # 設定用戶選擇的功能為「美食推薦」

                #根據使用者選擇的功能來運行
                elif user_states == 1:       
                    area = user_message
                    ifoodie = line_bot_scraper_ifoodie(area)
                    flex_message_datas = ifoodie.scrape()
                    if flex_message_datas:
                        replymessage = FlexSendMessage(
                            alt_text="美食推薦",
                            contents={
                                "type": "carousel",
                                "contents": flex_message_datas
                            }
                        )
                        line_bot_api.reply_message(event.reply_token, replymessage)
                        user_states = 0            
                    else:
                        text = "沒有找到相關餐廳資訊。"
                        replymessage = TextSendMessage(text)
                        line_bot_api.reply_message(event.reply_token, replymessage)

                elif user_message == "附近美食":
                    replymessage = [FlexSendMessage(
                        alt_text='隨時即行傳送訊息',
                        contents=big_food_class()
                        ),
                        TextSendMessage(text="請點擊想要查詢的食物類型")]
                    line_bot_api.reply_message(event.reply_token, replymessage)
                    user_states = 2  # 設定用戶選擇的功能為「附近美食」
                elif user_states == 3:
                    food_preference =  event.message.text  # 保存用戶的偏好
                    text = '請點擊下方"＋"傳送位置資訊'
                    replymessage = TextSendMessage(text)
                    line_bot_api.reply_message(event.reply_token, replymessage)

                else:
                    text = "請點擊功能選單"
                    replymessage = TextSendMessage(text=text)
                    line_bot_api.reply_message(event.reply_token, replymessage)

#====================================================================================================

            if isinstance(event, MessageEvent) and isinstance(event.message, LocationMessage):
                location = event.message

                if user_states == 3:
                    replymessage = FlexSendMessage(
                        alt_text='隨時即行傳送訊息',
                        contents=get_store_info(location, food_preference)  # 使用用戶的食物偏好
                    )
                    line_bot_api.reply_message(event.reply_token, replymessage)
                    user_states = 0
                else:
                    replymessage = TextSendMessage(text="請先選擇「附近美食」以傳送您的定位資訊。")
                    line_bot_api.reply_message(event.reply_token, replymessage)

#====================================================================================================

            if isinstance(event, PostbackEvent):
                data = event.postback.data
                if data == "rice_class":
                    replymessage = [FlexSendMessage(alt_text="米飯類選擇", contents=rice_class()),
                                    TextSendMessage(text="請點選圖卡告訴我你想吃甚麼飯，上述沒有想吃的也可以打字輸入呦")]
                    line_bot_api.reply_message(event.reply_token, replymessage)
                    user_states = 3
                    
                elif data == "noodle_class":
                    replymessage = [FlexSendMessage(alt_text="麵類選擇", contents=noodle_class()),
                                    TextSendMessage(text="請點選圖卡告訴我你想吃甚麼飯，上述沒有想吃的也可以打字輸入呦")]
                    line_bot_api.reply_message(event.reply_token, replymessage)
                    user_states = 3
                elif data == "local_class":
                    replymessage = [FlexSendMessage(alt_text="風味選擇", contents=local_class()),
                                    TextSendMessage(text="請點選圖卡告訴我你想吃甚麼飯，上述沒有想吃的也可以打字輸入呦")]
                    line_bot_api.reply_message(event.reply_token, replymessage)
                    user_states = 3

                elif data == "dessert_class":
                    replymessage = [FlexSendMessage(alt_text="下午茶選擇", contents=dessert_class()),
                                    TextSendMessage(text="請點選圖卡告訴我你想吃甚麼飯，上述沒有想吃的也可以打字輸入呦")]
                    line_bot_api.reply_message(event.reply_token, replymessage)
                    user_states = 3
    
    except:
        print(request.args)
    
    return 'OK'

#====================================================================================================

def get_store_info(location, need_food , max_results=10):
    global user_states
    GOOGLEMAPS_API_KEY = get_api_key('GOOGLEMAPS_API_KEY.txt')
    gmaps = googlemaps.Client(key=GOOGLEMAPS_API_KEY)

    try: 
        # Geocoding an address
        origin_location = {'lat':location.latitude, 'lng':location.longitude}
        # 使用 Places API 搜尋附近500公尺內的餐廳
        places_result = gmaps.places_nearby(location=origin_location, radius=500, keyword=need_food, language="zh-TW")

        places_text = []
        flex_message_datas = []
        # 列印每個餐廳的名稱及經緯度
        for place in places_result['results'][:max_results]:
            name = place.get('name')  # 獲取餐廳名稱
            place_location = place['geometry']['location']  # 獲取餐廳的經緯度
            lat = place_location['lat']
            lng = place_location['lng']

            address = place.get('vicinity')
            
            # 獲取餐廳的照片,評論分數及營業時間
            place_phtot = place.get('photos',[])
            place_rate = place.get('rating')
            opening_hours = place.get('opening_hours', {}) 
            business_time = opening_hours.get('open_now', '無營業時間')

            # 獲取店家的place_id,url及電話
            place_id = place.get('place_id')
            store_result = gmaps.place(place_id) 
            googlemap_url = store_result["result"]['url'] # 獲取餐廳的url
            
            telephone = 'tel:' + store_result["result"].get("formatted_phone_number", "0000").replace(" ", "")
            

            if business_time:
                business_status = '營業中'
                business_color = "#00A600"

            else:
                business_status = '已打烊'
                business_color = "#CE0000"

            if place_phtot:
                photo_reference = place_phtot[0].get('photo_reference')
                photo_url = get_photo_url(photo_reference , GOOGLEMAPS_API_KEY)
            else:
                photo_reference = ""
                photo_url = "https://www.post.gov.tw/post/internet/images/NoResult.jpg"

            # 使用 Geocoding API 獲取中文地址
            reverse_geocode_result = gmaps.reverse_geocode((lat, lng), language='zh-TW')
            # 獲取address_components的資訊:[0]street_number(如:13號) , [1]route(如:青海路二段) , [2]administrative_area_level_3(如:逢甲里) , [3]administrative_area_level_2(如:西屯區)
            #                             [4]administrative_area_level_1(如:台中市) , [5]country(如:台灣) , [6]postal_code
            detailed_address = reverse_geocode_result[0]['address_components'][4]['long_name'] + reverse_geocode_result[0]['address_components'][3]['long_name'] + address
            places_text.append(line_store_flex(photo_url, name, place_rate, detailed_address, business_status, telephone, googlemap_url, business_color , flex_message_datas))

        flex_message = flex_formmat(places_text[0])
        user_states = 0
        return flex_message

    except:
        flex_message = no_search()
        user_states = 0
        return flex_message

#====================================================================================================

def get_photo_url(photo_reference,GOOGLEMAPS_API_KEY , max_width=400):
    base_url = 'https://maps.googleapis.com/maps/api/place/photo'
    params = {
        'photoreference': photo_reference,
        'maxwidth': max_width,
        'key': GOOGLEMAPS_API_KEY
    }
    url = f"{base_url}?{requests.compat.urlencode(params)}"
    # print('bb') check
    return url

#==============================================================




