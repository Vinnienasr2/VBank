from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivy.uix.camera import Camera
import qrcode
import json


Window.size = (360, 750)


# screens
class LoginScreen(MDScreen):
    pass  

class RegistrationScreen(MDScreen):
    pass

class HomeScreen(MDScreen):
    pass

class SendMoney(MDScreen):
    pass

class CompleteTransaction(MDScreen):
    pass


class QrReceiveMoney(MDScreen):
    def on_enter(self, *args):
        # Generate QR code with receiver name and account number
        receiver_name = "John Doe"
        account_number = "1234567890123"  # 13-digit account number
        data = f"Receiver: {receiver_name}\nAccount Number: {account_number}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save QR code as a temporary file
        img_path = "temp_qr_code.png"
        img.save(img_path)

        # Display QR code on the screen
        self.ids.qr_code_image.source = img_path

class QRSendMoney(MDScreen):
    pass

class MyCard(MDCard):
    title = ""
    image_source = ""
    icon = ""
    label_color = [0, 0, 0, 1] 

    
class ClickableLabel(ButtonBehavior, MDLabel):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dispatch('on_release')
            return True
        return super().on_touch_down(touch)
    
class MyConfirmationDialog(MDDialog):
    pass

class MainApp(MDApp):
    def build(self):
        Builder.load_file('main.kv')
        self.screen_manager = ScreenManager(transition=FadeTransition())
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(RegistrationScreen(name='register'))
        self.screen_manager.add_widget(HomeScreen(name='home'))
        self.screen_manager.add_widget(SendMoney(name="send_money"))
        self.screen_manager.add_widget(CompleteTransaction(name="complete_transaction"))
        self.screen_manager.add_widget(QrReceiveMoney(name="qr_receive_money"))
        self.screen_manager.add_widget(QRSendMoney(name="qr_send_money"))
        return self.screen_manager

    def register(self):
        self.screen_manager.current = 'register'

    def login(self):
        self.screen_manager.current = 'login'

    def send_money(self):
        self.screen_manager.current = 'send_money'
        
    def back(self):
       self.screen_manager.current = 'home'
       
    def back_to_send_money(self):
        self.screen_manager.current ='send_money'
       
    def send_transfer(self, account_number, amount_field):
        pass
    
    def validate_input(self):
        send_money_text = self.root.ids.account_number.text if hasattr(self.root.ids, 'send_money_field') else ""
        amount_text = self.root.ids.amount_field.text if hasattr(self.root.ids, 'amount_field') else ""

        
    def show_dialog(self):
        dialog  = MDDialog(
            title="Confirmation receiver Name",
            text="Name: Vincent Mwangi",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda *args: dialog.dismiss()
                ),
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: self.complete_transaction(dialog)
                ),
            ],
        )
        dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def complete_transaction(self, dialog):
        self.screen_manager.current = 'complete_transaction'
        dialog.dismiss()
        
    def exit_successfully(self):
        self.screen_manager.current = 'send_money'
        
    def qr_receive_money(self):
        self.screen_manager.current = 'qr_receive_money'
        
    def qr_send_money(self):
        self.screen_manager.current = 'qr_send_money'
        
if __name__ == '__main__':
    MainApp().run()
