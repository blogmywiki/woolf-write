# simple text editor lesson 2 - adding a button to save
from guizero import App, TextBox, PushButton

app = App(title="WoolfWrite", width=1400, height=800)

def localSave():
    file = open("doc.txt","w")
    file.write(input_box.get())
    file.close()    
    
input_box = TextBox(app, width=80, height=16, multiline=True, scrollbar=True)
input_box.font = "Times New Roman"
input_box.text_color = "blue"
input_box.text_size = 34
input_box.bg = "#FFFFE7"

saveButton = PushButton(app, command=localSave, text="Save")

app.display()
