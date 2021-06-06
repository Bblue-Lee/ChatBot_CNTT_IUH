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
        file=pandas.read_csv('E:\\DATN_2020\\Chatbot_v1\\actions\\KTPM_GV.csv')

        dataRead=file[['link-name', 'name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_DoiNguGV_KHMT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_KHMT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\DATN_2020\\Chatbot_v1\\actions\\KHMT_GV.csv')

        dataRead=file[['link-name', 'name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_DoiNguGV_KHDL(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_KHDL"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\DATN_2020\\Chatbot_v1\\actions\\KHDL_GV.csv')

        dataRead=file[['link-name', 'name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_DoiNguGV_CNTT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_CNTT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\DATN_2020\\Chatbot_v1\\actions\\CNTT_GV.csv')

        dataRead=file[['link-name', 'name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []
class ActionGetInfo_DoiNguGV_HTTT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_HTMT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file=pandas.read_csv('E:\\DATN_2020\\Chatbot_v1\\actions\\HTTT_GV.csv')

        dataRead=file[['link-name', 'name-gv', 'chuc-vu','mail-gv']]
        dispatcher.utter_message(text=f'{dataRead}')
        return []





