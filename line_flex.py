from bs4 import BeautifulSoup
import requests

def generate_star_icons(store_rateing_star):
    # 將星數值轉換為整數（四捨五入）
    if store_rateing_star == None:
        rounded_star_num = 0
    else:
        rounded_star_num = round(store_rateing_star)

    # 設定最大星數（5顆星）
    max_stars = 5

    # 計算金星和灰星的數量
    num_gold_stars = min(rounded_star_num, max_stars)
    num_gray_stars = max_stars - num_gold_stars

    # 生成星星圖示的URL
    gold_star_url = "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
    gray_star_url = "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"


    rateing_star = []

    for i in range(num_gold_stars):
        rateing_star.append({"type": "icon", "size": "xs", "url": gold_star_url}) 

    for i in range(num_gray_stars):
        rateing_star.append({"type": "icon", "size": "xs", "url": gray_star_url})

    rateing_star.append({
                                    "type": "text",
                                    "text": str(store_rateing_star),
                                    "size": "xs",
                                    "color": "#8c8c8c",
                                    "margin": "md",
                                    "flex": 0
                                })
    return rateing_star

    # # 生成星星圖示內容
    # return rateing_star

def line_store_flex(photo_url, name, place_rate, detailed_address, business_status, telephone, googlemap_url, business_color, flex_message_datas):
    flex_message_datas.append({
            "type": "bubble",
            "size": "deca",
            "hero": {
                "type": "image",
                "url": photo_url,
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213",
                "action":{
                    "type":"uri",
                    "uri": googlemap_url
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": name,
                        "weight": "bold",
                        "size": "sm",
                        "maxLines": 1,
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "offsetTop": "sm",
                        "contents": generate_star_icons(place_rate)
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "offsetTop": "md",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "地址",
                                        "wrap": True,
                                        "color": "#8c8c8c",
                                        "size": "xs",
                                        "flex": 2
                                    },
                                    {
                                        "type": "text",
                                        "text": detailed_address,
                                        "size": "xs"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "offsetTop": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": business_status,
                                        "size": "sm",
                                        "flex": 1,
                                        "color": business_color
                                    }
                                ]
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "撥打電話",
                                    "uri": telephone
                                }
                            }
                        ]
                    }
                ]
            }
        })
    return flex_message_datas

def big_food_class():
    contents ={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://storage.googleapis.com/linebot-cls/rice_folder/rice_class_image.jpg",
            "size": "5xl",
            "aspectMode": "cover",
            "aspectRatio": "150:196",
            "gravity": "center",
            "flex": 1,
            "action": {
              "type": "postback",
              "data": "rice_class"
            }
          },
          {
            "type": "image",
            "url": "https://storage.googleapis.com/linebot-cls/noodle_folder/noodle_class_image.jpg",
            "size": "5xl",
            "aspectMode": "cover",
            "aspectRatio": "150:196",
            "gravity": "center",
            "flex": 1,
            "action": {
              "type": "postback",
              "data": "noodle_class"
            }
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://storage.googleapis.com/linebot-cls/local_folder/local_class_image.jpg",
            "size": "5xl",
            "aspectMode": "cover",
            "aspectRatio": "150:196",
            "gravity": "center",
            "flex": 1,
            "action": {
              "type": "postback",
              "data": "local_class"
            }
          },
          {
            "type": "image",
            "url": "https://storage.googleapis.com/linebot-cls/afternonn_folder/afternoon_class_image.jpg",
            "size": "5xl",
            "aspectMode": "cover",
            "aspectRatio": "150:196",
            "gravity": "center",
            "flex": 1,
            "action": {
              "type": "postback",
              "data": "dessert_class"
            }
          }
        ]
      }
    ],
    "paddingAll": "0px"
  }
}
    return contents

def rice_class():
    contents = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/rice_folder/rice1.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "炒飯"
                }
              },
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/rice_folder/rice2.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "燒臘飯"
                }
              }
            ],
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/rice_folder/rice3.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "咖哩飯"
                }
              },
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/rice_folder/rice4.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "丼飯"
                }
              }
            ]
          }
        ]
      }
    ],
    "paddingAll": "0px"
  }
}
    
    return contents

#麵類
def noodle_class():
    contents = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/noodle_folder/noodle1.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "拉麵"
                }
              },
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/noodle_folder/noodle2.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "乾麵"
                }
              }
            ],
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/noodle_folder/noodle3.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "義大利麵"
                }
              },
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/noodle_folder/noodle4.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "羹麵"
                }
              }
            ]
          }
        ]
      }
    ],
    "paddingAll": "0px"
  }
}
    
    return contents

#風味
def local_class():
    contents = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/local_folder/local1.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "美式餐廳"
                }
              },
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/local_folder/local2.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "西餐廳"
                }
              }
            ],
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/local_folder/local3.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "港式餐廳"
                }
              },
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/local_folder/local4.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "泰式餐廳"
                }
              }
            ]
          }
        ]
      }
    ],
    "paddingAll": "0px"
  }
}
    return contents

#下午茶
def dessert_class():
    contents = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/afternonn_folder/afternoon1.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "咖啡廳"
                }
              },
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/afternonn_folder/afternoon2.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "麵包店"
                }
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/afternonn_folder/afternoon3.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "蛋糕"
                }
              },
              {
                "type": "image",
                "url": "https://storage.googleapis.com/linebot-cls/afternonn_folder/afternoon4.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                "action": {
                  "type": "message",
                  "text": "手搖飲"
                }
              }
            ]
          }
        ]
      }
    ],
    "paddingAll": "0px"
  }
}
    
    return contents

class line_bot_scraper_ifoodie:
    def __init__(self, area):
        self.area = area

    def scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        response = requests.get(
            "https://ifoodie.tw/explore/" + self.area + "/list?sortby=popular&opening=true", headers=headers)

        if response.status_code != 200:
            print("Failed to retrieve the webpage. Status Code:", response.status_code)
            return []

        soup = BeautifulSoup(response.content, "html.parser")
        cards = soup.find_all('div', {'class': 'restaurant-item'}, limit=4)

        if not cards:
            print("沒有抓取到資料")
            return []

        flex_message_datas = []

        for card in cards:
            title = card.find("a", {"class": "title-text"}).getText()
            stars = card.find("div", {"class": "jsx-2373119553 text"}).getText()
            address = card.find("div", {"class": "address-row"}).getText()
            url = card.find("a", {"class": "title-text"}).get("href")
            photo = card.find("img").get("src")

            # 確保 URL 以 https:// 開頭
            if not url.startswith("http"):
                url = "https://ifoodie.tw" + url
            if not photo.startswith("http"):
                photo = "https:" + photo

            try:
                stars = float(stars)
            except ValueError:
                stars = 0

            flex_message_datas.append({
                "type": "bubble",
                "size": "deca",
                "hero": {
                    "type": "image",
                    "url": photo,
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213",
                    "action": {
                        "type": "uri",
                        "uri": url
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": title,
                            "weight": "bold",
                            "size": "sm",
                            "maxLines": 1,
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "offsetTop": "sm",
                            "contents": generate_star_icons(stars)
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "offsetTop": "md",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "地址",
                                            "wrap": True,
                                            "color": "#8c8c8c",
                                            "size": "xs",
                                            "flex": 2
                                        },
                                        {
                                            "type": "text",
                                            "text": address,
                                            "size": "xs"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            })
        
        return flex_message_datas

# 食物大分類的flex message格式


# 美食推薦地區選擇的flex message #需要改圖片
def ifoodie_class(): 
    contents={
  "type": "bubble",
  "size": "deca",
  "hero": {
    "type": "image",
    "url": "https://storage.googleapis.com/linebot-cls/taiwanfood.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://line.me/"
    }
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "台北",
          "text": "台北"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "台中",
          "text": "台中"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "台南",
          "text": "台南"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "台東",
          "text": "台東"
        }
      }
    ],
    "flex": 0
  }
}
    return contents
def no_search():
    contents ={
  "type": "bubble",
  "size": "hecto",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "附近沒有您想搜尋的食物類型",
        "weight": "bold",
        "size": "md"
      }
    ]
  }
}
    return contents

def flex_formmat(places_text):
    
    flex_message = {
        "type": "carousel",
        "contents": places_text
        }
    return flex_message