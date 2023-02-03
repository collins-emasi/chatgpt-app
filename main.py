from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_file("story.kv")

Window.size = (320, 600)


class WindowManager(ScreenManager):
    """ A window manager to manage switching between screens """


class MessageScreen(Screen):
    """ A screen that display the stories and all message histories """


class StoryWithImage(MDBoxLayout):
    """ A horizontal layout with an dp and a username """
    text = StringProperty()
    source = StringProperty()


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wm = WindowManager(transition=FadeTransition())

    def build(self):
        """Init the application and return root widget"""
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.accent_hue = "400"
        self.title = "Chat GPT"

        screens = [
            MessageScreen(name='message')
        ]

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm


if __name__ == "__main__":
    MainApp().run()
