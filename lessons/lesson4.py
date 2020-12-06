# simple text editor lesson 4 - add a word count
from guizero import App, TextBox, PushButton, Text

app = App(title="WoolfWrite", width=1400, height=800)

def wordCount():
    status.value = "NOT SAVED"
    status.text_color = "red"
    text = input_box.get()
    words = str(len(text.split()))
    wordCountText.value = words + " words"

def localSave():
    filename = filename_box.get()+".txt"
    status.value = "Saved locally"
    status.text_color = "green"
    file = open(filename,"w")
    file.write(input_box.get())
    file.close()
    app.title = "WoolfWrite - " + filename

input_box = TextBox(app, width=80, height=16, multiline=True, scrollbar=True, command=wordCount)
input_box.font = "Times New Roman"
input_box.text_color = "blue"
input_box.text_size = 34
input_box.bg = "#FFFFE7"
wordCountText = Text(app, text="")
saveButton = PushButton(app, command=localSave, text="Save")
status = Text(app, text="")
filename_box = TextBox(app, text="filename", width=20, height=1, multiline=False, scrollbar=False)

wordCount()
app.display()
