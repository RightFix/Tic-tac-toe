import re
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
      self.theme_cls.theme_style = "Light"
      self.theme_cls.primary_palette = "Orange"
      
      return super().build()
    
    x = True
    re = re
    
MainApp().run()
