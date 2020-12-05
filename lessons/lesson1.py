# simple text editor lesson 1 - add a text box
from guizero import App, TextBox

app = App(title="WoolfWrite", width=1400, height=800)
    
input_box = TextBox(app, width=80, height=16, multiline=True, scrollbar=True)
input_box.font = "Times New Roman"
input_box.text_color = "blue"
input_box.text_size = 34
input_box.bg = "#FFFFE7"

app.display()
