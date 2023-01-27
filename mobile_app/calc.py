from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainA(App):
    def build(self):
        self.icon = "calc1.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_operator = None
        self.last_btn = None

        main_lyot = BoxLayout(orientation = "vertical")
        self.sltn = TextInput(background_color = "pink", foreground_color = "black", multiline=False, halign="right", font_size=55, readonly=True)

        main_lyot.add_widget(self.sltn)
        btns = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            [".","0","C","+"],
        ]

        for r in btns:
            h_lyot = BoxLayout()
            for l in r:
                btn = Button(
                    text = l, font_size=30, background_color="white",
                    pos_hint={"center_x": 0.5, "center_y":0.5},
                )
                btn.bind(on_press = self.on_btn_press)
                h_lyot.add_widget(btn)
            main_lyot.add_widget(h_lyot)

        equal_btn = Button(text="=", font_size=30, background_color="white",
                           pos_hint={"center_x":0.5, "center_y":0.5},
                           )
        equal_btn.bind(on_press=self.on_sltn)
        main_lyot.add_widget(equal_btn)

        return main_lyot

    def on_btn_press(self,instance):
        crnt = self.sltn.text
        btn_txt = instance.text

        if btn_txt == 'C':
            self.sltn.text = ""
        else:
            if crnt and (
                self.last_operator and btn_txt in self.operators):
                return
            elif crnt == "" and btn_txt in self.operators:
                return
            else:
                new_txt = crnt + btn_txt
                self.sltn.text = new_txt
        self.last_btn = btn_txt
        self.last_operator = self.last_btn in self.operators

    def on_sltn(self, instance):
        txt = self.sltn.text
        if txt:
            sltn = str(eval(self.sltn.text))
            self.sltn.text = sltn


if __name__ == "__main__":
    app = MainA()
    app.run()

