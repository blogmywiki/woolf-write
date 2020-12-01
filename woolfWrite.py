# a very simple text editor with word count made with guizero

from guizero import App, TextBox, Text, PushButton
app = App(title="WoolfWrite", width=1200, height=750)

def wordCount():
    status.value = "NOT SAVED"
    status.text_color = "red"
    tempText = " ".join(input_box.get().split()) # remove line breaks, multiple spaces etc
    wordSplit = tempText.split(" ")
    words = str(len(wordSplit))
    wordText.value = "Words: " + words

def localSave():
    filename = filename_box.get()+".txt"
    status.value = "Saved locally"
    status.text_color = "green"
    file = open(filename,"w")
    file.write(input_box.get())
    file.close()
    file = open("woolfWrite.cfg","w")
    file.write(filename)
    file.close()
    app.title = "WoolfWrite - " + filename

file = open("woolfWrite.cfg","r")
filename = file.read()
file.close()

file = open(filename,"r")
textContents = file.read()
file.close()
    
input_box = TextBox(app, text=textContents, width=80, height=20, multiline=True, scrollbar=True, command=wordCount)
input_box.text_color = "blue"
input_box.text_size = 23
input_box.bg = "#FFFFE7"
wordText = Text(app, text="")
saveButton = PushButton(app, command=localSave, text="Save local")
status = Text(app, text="")
filename_box = TextBox(app, text=filename[:-4], width=20, height=1, multiline=False, scrollbar=False)

wordCount()
app.display()
