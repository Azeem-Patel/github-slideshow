from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.tab import MDTabs, MDTabsBase
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView


class TradingLeagueApp(MDApp):

    def build(self):
        self.title = "Trading League"
        return TradingLeagueApp()

    def add_row(self):
        self.root.ids.rows_container.add_widget(Row())

    def remove_row(self):
        if len(self.root.ids.rows_container.children) > 1:
            self.root.ids.rows_container.remove_widget(self.root.ids.rows_container.children[0])


class Row(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 11
        self.size_hint_y = None
        self.height = '50dp'

        # Adding Widgets for each column
        self.add_widget(MDFlatButton(text='Buy', md_bg_color=[0, 1, 0, 1], size_hint_x=None, width='50dp'))
        self.add_widget(MDFlatButton(text='Sell', md_bg_color=[1, 0, 0, 1], size_hint_x=None, width='50dp'))
        self.add_widget(MDDropDownItem(text="LIMIT"))
        self.add_widget(MDDropDownItem(text="NRML"))
        self.add_widget(MDDropDownItem(text="BCD"))
        self.add_widget(MDDropDownItem(text="Symbol"))
        self.add_widget(MDLabel(text="Expiry", halign="center"))
        self.add_widget(MDLabel(text="Instrument", halign="center"))
        self.add_widget(MDLabel(text="LotSize", halign="center"))
        self.add_widget(MDLabel(text="Quantity", halign="center"))
        self.add_widget(MDLabel(text="Price", halign="center"))


if __name__ == '__main__':
    TradingLeagueApp().run()
