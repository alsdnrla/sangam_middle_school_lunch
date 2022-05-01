import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from pytz import timezone






  



def sc_lunch(data_time):
  todaying = datetime.now(timezone('Asia/Seoul')) + timedelta(data_time)
  today_d = todaying.strftime("%Y%m%d")
  today_b = todaying.strftime("%Y년 %m월 %d일")

  

  req = requests.get(f"https://open.neis.go.kr/hub/mealServiceDietInfo?Type=text&KEY=ecabe857ea114a09a0db1163ae5fa947&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7031189&MLSV_FROM_YMD={today_d}&MLSV_TO_YMD={today_d}")
  if req.status_code == 200:
    try:
      
      
      soup = BeautifulSoup(req.text, 'html.parser')
      
      
      middle_lunch = soup.select_one("ddish_nm").get_text()
      cal_info = soup.select_one("cal_info").get_text()
      
      
      return today_b, middle_lunch, cal_info
    except:
      N_lunch = "오늘의 급식은 존재하지 않습니다."
      N_cal = "0  - Kcal"
      return today_b, N_lunch, N_cal
  else:
    return None
      
   







   


