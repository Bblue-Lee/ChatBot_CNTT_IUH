import datetime as dt 
from typing import Any, Text, Dict, List

from bs4 import BeautifulSoup
import urllib.request
from numpy.core.fromnumeric import take
import pandas

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time=dt.datetime
        dispatcher.utter_message(text=f"time now: {time}")

        return []
class ActionGetInfo_coCauToChuc(Action):

    def name(self) -> Text:
        return "action_hoi_CoCauToChuc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text="lấy data về cơ cấu tổ chức")
       
        url =  'http://fit.iuh.edu.vn/category.html@184@Co-cau-to-chuc'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        try:
            content=soup.find(class_='content-bottom').find(class_='col-md-9 page-left')
            title_page=content.find(class_='page-title').text
            time=content.find(class_='title-date')
            content_ND=content.find(class_='left-content').text
            dispatcher.utter_message(text=f"{content_ND}")
        except:
            dispatcher.utter_message(text="no data")

        return []
class ActionGetInfo_DoiNguGV_KTPM(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_KTPM"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\ChatBot-CNTT\\actions\\CNTT_GV.csv\\KTPM_GV.csv')

        dataRead=file[['name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_DoiNguGV_KHMT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_KHMT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\ChatBot-CNTT\\actions\\CNTT_GV.csv\\KHMT_GV.csv')

        dataRead=file[['name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_DoiNguGV_KHDL(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_KHDL"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\ChatBot-CNTT\\actions\\CNTT_GV.csv\\KHDL_GV.csv')

        dataRead=file[['name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_DoiNguGV_CNTT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_CNTT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\ChatBot-CNTT\\actions\\CNTT_GV.csv\\CNTT_GV.csv')

        dataRead=file[['name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_DoiNguGV_HTTT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_HTMT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\ChatBot-CNTT\\actions\\CNTT_GV.csv\\HTTT_GV.csv')

        dataRead=file[['name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_thongBaoSinhVien(Action):

    def name(self) -> Text:
        return "action_hoi_thongBaoSinhVien"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url =  'http://fit.iuh.edu.vn/news.html@155@Thong-bao-Sinh-vien'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        left_content=soup.find(class_='col-md-9 page-left').find(class_='left-content')
        content_list= left_content.find(class_='content-list').find_all(class_='content')
        for x in content_list:
	        thongBao=x.find(class_='content-info col-sm-9')
	        title=thongBao.find('a').get('title')
	        time=thongBao.find('span').text
	        href=thongBao.find('a').get('href')    
	        dispatcher.utter_message(text=f"{title} \n{time}\nhttp://fit.iuh.edu.vn/{href}")
class ActionGetInfo_thucTapViecLam(Action):

    def name(self) -> Text:
        return "action_hoi_thucTapViecLam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url =  'http://fit.iuh.edu.vn/news.html@104@Thuc-tap-Viec-lam'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        left_content=soup.find(class_='col-md-9 page-left').find(class_='left-content')
        content_list= left_content.find(class_='content-list').find_all(class_='content')
        for x in content_list:
	        thongBao=x.find(class_='content-info col-sm-9')
	        title=thongBao.find('a').get('title')
	        time=thongBao.find('span').text
	        href=thongBao.find('a').get('href')    
	        dispatcher.utter_message(text=f"{title} \t{time}\nhttp://fit.iuh.edu.vn/{href}")
        return []
class ActionGetInfo_thongBaoTuyenSinh(Action):

    def name(self) -> Text:
        return "action_hoi_thongBaoTuyenSinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url =  'http://fit.iuh.edu.vn/news.html@157@Thong-tin-tuyen-sinh'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        left_content=soup.find(class_='col-md-9 page-left').find(class_='left-content')
        content_list= left_content.find(class_='content-list').find_all(class_='content')
        for x in content_list:
	        thongBao=x.find(class_='content-info col-sm-9')
	        title=thongBao.find('a').get('title')
	        time=thongBao.find('span').text
	        href=thongBao.find('a').get('href')    
	        dispatcher.utter_message(text=f"{title} \t{time}\nhttp://fit.iuh.edu.vn/{href}")
        return []

class ActionGetInfo_tinTucSuKien(Action):

    def name(self) -> Text:
        return "action_hoi_tinTucSuKien"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url =  'http://fit.iuh.edu.vn/news.html@102@Tin-tuc-Su-kien'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        left_content=soup.find(class_='col-md-9 page-left').find(class_='left-content')
        content_list= left_content.find(class_='content-list').find_all(class_='content')
        for x in content_list:
	        thongBao=x.find(class_='content-info col-sm-9')
	        title=thongBao.find('a').get('title')
	        time=thongBao.find('span').text
	        href=thongBao.find('a').get('href')    
	        dispatcher.utter_message(text=f"{title} \t{time}\nhttp://fit.iuh.edu.vn/{href}")
        return []
