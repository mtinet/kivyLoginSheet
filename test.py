from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        fontName = "fonts/NanumGothic.ttf"
        return Button(text='안녕하세요 \nKivy입니다.',font_name=fontName, font_size=100)

if __name__ == '__main__':
    TestApp().run()
