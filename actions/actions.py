from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from bs4 import BeautifulSoup
import urllib.request
import csv
import re

class ActionGetInfo_coCauToChuc(Action):

    def name(self) -> Text:
        return "action_hoi_CoCauToChuc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class  ActionGetInfo_gvKTPM(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_KTPM"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_gvKHMT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_KHMT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_gvCNTT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_CNTT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_gvHTMT(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_HTMT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_gvKHDL(Action):

    def name(self) -> Text:
        return "action_hoi_DoiNguGV_KHDL"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_daoTaoSauDH(Action):

    def name(self) -> Text:
        return "action_hoi_DaoTaoSauDH"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_daoTaoDH(Action):

    def name(self) -> Text:
        return "action_hoi_daoTaoDH"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_TTTS(Action):

    def name(self) -> Text:
        return "action_hoi_thongTinTuyenSinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_congTrinhNgienCuu(Action):

    def name(self) -> Text:
        return "action_hoi_congTrinhNghienCuu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_tinTucSuKien(Action):

    def name(self) -> Text:
        return "action_hoi_tinTucSuKien"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_cauLacBoLapTrinh(Action):

    def name(self) -> Text:
        return "action_hoi_cauLacBoLapTrinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_cauLacBoAnToanThongTin(Action):

    def name(self) -> Text:
        return "action_hoi_cauLacBoAnToanThongTin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_thongBaoSinhVien(Action):

    def name(self) -> Text:
        return "action_hoi_thongBaoSinhVien"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_bieuMauHuongDan(Action):

    def name(self) -> Text:
        return "action_hoi_huongDan_bieuMau"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]
class ActionGetInfo_viecLamThucTap(Action):

    def name(self) -> Text:
        return "action_hoi_thucTap_viecLam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[]





    