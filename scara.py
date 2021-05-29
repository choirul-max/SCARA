from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
from kivymd.utils import asynckivy
import time
import threading
import sys
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.core.window import Window  # You must import this

Window.size = (300, 500)

if __name__ == '__main__' and __package__ is None:
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

kv = (
    '''
#:import sys sys
#:import MapSource kivy_garden.mapview.MapSource

ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    LocationScreen:

<WelcomeScreen>:
    name:'welcomescreen'
    MDCard:
        size_hint: None, None
        size: 270, 400
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25

        orientation:"vertical"
        Image:
            id: avatar
            size_hint: None, None
            size: "180dp", "180dp"
            source: "logo.png"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDLabel:
            text: "Safety Car Asisstant"
            font_size: 20
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 2

        MDRoundFlatIconButton:
            text: "LOG IN"
            icon: "login"
            size_hint_x: None
            width: 100
            font_size:12
            pos_hint: {"center_x": 0.5}
            on_press:
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'left'

        MDRoundFlatIconButton:
            text: "Sign Up"
            icon: "account-badge-horizontal"
            size_hint_x: None
            width: 100
            font_size:12
            pos_hint: {"center_x": 0.5}
            on_press:
                root.manager.current = 'signupscreen'
                root.manager.transition.direction = 'left'

<LoginScreen>:
    name:'loginscreen'
    MDCard:
        size_hint: None, None
        size: 250, 400
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25

        orientation:"vertical"
        Image:
            id: avatar
            size_hint: None, None
            size: "50dp", "50dp"
            source: "logo.png"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDLabel:
            text:'Login'
            font_size: 20
            halign: 'center'
            height: self.texture_size[1]
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id:login_email
            hint_text: "Email"
            icon_right: "email"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            helper_text_mode:  'on_error'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        MDTextField:
            id:login_password
            hint_text: "Password"
            icon_right: "key"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True
            helper_text_mode:  'on_error'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"


        MDRoundFlatIconButton:
            text:'Login'
            icon: "login"
            size_hint_x: None
            width: 100
            font_size:12
            pos_hint: {"center_x": 0.5}
            on_press:
                app.login()
                app.username_changer()

        MDRoundFlatIconButton:
            text: 'Create an account'
            icon: "login"
            size_hint_x: None
            width: 180
            font_size:12
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            on_press:
                root.manager.current = 'signupscreen'
                root.manager.transition.direction = 'up'


<SignupScreen>:
    name:'signupscreen'
    MDCard:
        size_hint: None, None
        size: 250, 400
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 13

        orientation:"vertical"

        Image:
            id: avatar
            size_hint: None, None
            size: "50dp", "50dp"
            source: "logo.png"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDLabel:
            text:'Sign Up'
            font_size: 20
            halign: 'center'
            height: self.texture_size[1]
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id:signup_email
            hint_text: "Email"
            icon_right: "email"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"

        MDTextField:
            id:signup_username
            hint_text: "Usename"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"

        MDTextField:
            id:signup_password
            hint_text: "Password"
            icon_right: "key"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"

        MDRoundFlatIconButton:
            text:'Signup'
            icon: "login"
            size_hint_x: None
            width: 100
            font_size:12
            pos_hint: {"center_x": 0.5}
            on_press: app.signup()

        MDRoundFlatIconButton:
            text: 'Already have an account'
            icon: "login"
            size_hint_x: None
            width: 200
            font_size:12
            pos_hint: {"center_x": 0.5}
            on_press:
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'down'

<MainScreen>:
    name: 'mainscreen'
    BoxLayout:
        orientation:'vertical'
        MDBottomNavigation:
            panel_color: .2, .2, .2, 1
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Monitoring'
                icon: 'monitor'

                BoxLayout:
                    orientation:'vertical'
                    size_hint: None, None
                    size: 250, 400
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    elevation: 10
                    padding: 5
                    spacing: 5
                    canvas.before:
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: 'mobil.jpg'

                    MDLabel:
                        text:'DRIVER'
                        font_size: 15
                        halign: 'center'
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'
                    MDLabel:
                        id :status_driver
                        text:'hello world'
                        font_size: 15
                        halign: 'center'
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'

                    MDLabel:
                        text:'NODE 1'
                        font_size: 15
                        halign: 'right'
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'

                    MDLabel:
                        id:node_1
                        text:'HC/CO'
                        font_size: 15
                        halign: 'right'
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'

                    MDLabel:
                        text:'NODE 2'
                        font_size: 15
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'
                    MDLabel:
                        id:node_2
                        text:'HC/CO'
                        font_size: 15
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'

                    MDLabel:
                        text:'NODE 3'
                        font_size: 15
                        halign: 'right'
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'
                    MDLabel:
                        id:node_3
                        text:'HC/CO'
                        font_size: 15
                        halign: 'right'
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'

                    MDLabel:
                        text:'NODE 4'
                        font_size: 15
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'
                    MDLabel:
                        id:node_4
                        text:'CO/HC'
                        font_size: 15
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'

                    MDLabel:
                        text:'Status Gas'
                        halign: 'center'
                        font_size: 15
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'
                    MDLabel:
                        id:status_gas
                        text:'NORMAL'
                        halign: 'center'
                        font_size: 15
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'
                    MDLabel:
                        id:loc
                        text:'-'
                        halign: 'center'
                        font_size: 15
                        height: self.texture_size[1]
                        size_hint_x: None
                        width: 200
                        pos_hint: {"center_x": 0.5}
                        theme_text_color: "Custom"
                        text_color: 100/255, 128/255, 244/255, 1
                        font_style: 'Subtitle2'

                MDRoundFlatIconButton:
                    text:'MONITORING'
                    icon: "monitor"
                    size_hint_x: None
                    width: 100
                    font_size:12
                    pos_hint: {"center_x": 0.5}
                    on_press:
                        app.ondatabase()

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Map'
                icon: 'map'

                MapView:
                    id: mapview
                    lat: -7.644043
                    lon: 111.414448
                    zoom: 13
                    double_tap_zoom: True
                    map_source: MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"
                    MapMarkerPopup:
                        lat: -7.644043
                        lon: 111.414448
                        popup_size: dp(200), dp(100)
                        source: "POP_UP_MAX.png"
                        Bubble:
                            BoxLayout:
                                orientation: "horizontal"
                                padding: "5dp"
                                AsyncImage:
                                    source: "logo.png"
                                    mipmap: True
                                Label:
                                    text: "[b]Posisi Mobil[/b]"
                                    markup: True
                                    halign: "center"

                MDRoundFlatIconButton:
                    text:'MOVE'
                    icon: "map"
                    size_hint_x: None
                    width: 100
                    font_size:12
                    pos_hint: {"center_x": 0.5}
                    on_release: mapview.center_on(50.6394, 3.057)

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Log Out'
                icon: 'logout'

                on_tab_press:
                    root.manager.current = 'loginscreen'
                    root.manager.transition.direction = 'down'


'''
)


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class LocationScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='loginscreen'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(LocationScreen(name='locationscreen'))


class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "BlueGray"
        self.strng = Builder.load_string(kv)
        self.url = "https://project-ta-9b55d-default-rtdb.firebaseio.com//.json"
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url, json=to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'

    auth = 'uulac0qbPH8gTcJCKrkzK5qjB4ulVu0ip5lHd6R9'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()

        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'

        else:
            print("user no longer exists")

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen')

    def ondatabase(self):
        threading.Thread(target=self.database()).start()

    def database(self):
        async def set_heading():
            while True:

                supported_arm = 'ARM'
                supported_node1 = 'NODE1'
                supported_node2 = 'NODE2'
                supported_node3 = 'NODE3'
                supported_node4 = 'NODE4'
                supported_statusdriver = 'StatusDriver'
                supported_statusgas = 'StatusGas'
                supported_loc = 'LOCATION'
                request = requests.get(self.url + '?auth=' + self.auth)
                data = request.json()
                emails = set()

                for key, value in data.items():
                    emails.add(key)

                self.data_all = [data[supported_arm]['ARM'], data[supported_node1]['CO1'], data[supported_node1]['HC1'],
                                 data[supported_node2]['CO2'], data[supported_node2]['HC2'],
                                 data[supported_node3]['CO3'], data[supported_node3]['HC3'],
                                 data[supported_node4]['CO4'], data[supported_node4]['HC4'],
                                 data[supported_statusdriver]['StatusDriver'], data[supported_statusgas]['StatusGas'],
                                 data[supported_loc]['lat'], data[supported_loc]['lon']]

                await asynckivy.sleep(1)
                data_status_arm = self.strng.get_screen('mainscreen').ids.status_driver
                data_status_arm.text = f' {str(self.data_all[0])} / {str(self.data_all[9])}'

                await asynckivy.sleep(1)
                data_node_1 = self.strng.get_screen('mainscreen').ids.node_1
                data_node_1.text = f'CO:{str(self.data_all[1])} /HC:{str(self.data_all[2])}'

                await asynckivy.sleep(1)
                data_node_2 = self.strng.get_screen('mainscreen').ids.node_2
                data_node_2.text = f'CO:{str(self.data_all[3])} /HC:{str(self.data_all[4])}'

                await asynckivy.sleep(1)
                data_node_3 = self.strng.get_screen('mainscreen').ids.node_3
                data_node_3.text = f'CO:{str(self.data_all[5])} /HC:{str(self.data_all[6])}'

                await asynckivy.sleep(1)
                data_node_4 = self.strng.get_screen('mainscreen').ids.node_4
                data_node_4.text = f'CO:{str(self.data_all[7])} /HC:{str(self.data_all[8])}'

                await asynckivy.sleep(1)
                data_status_gas = self.strng.get_screen('mainscreen').ids.status_gas
                data_status_gas.text = str(self.data_all[10])

                await asynckivy.sleep(1)
                data_status_loc = self.strng.get_screen('mainscreen').ids.loc
                data_status_loc.text = f'lat:{str(self.data_all[11])} /lon:{str(self.data_all[12])}'
                time.sleep(2)

        asynckivy.start(set_heading())


if __name__ == '__main__':
    LoginApp().run()