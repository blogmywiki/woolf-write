# a very simple text editor with word count made with guizero
from guizero import App, TextBox, Text, PushButton

app = App(title="WoolfWrite", width=1400, height=800)

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

# open config file with filename of last saved document
try:
    file = open("woolfWrite.cfg","r") 
    filename = file.read()
    file.close()
except:
    print("Could not open/read config file")
    filename = "new document.txt"

# if no saved document assign some text, otherwise open last document
if filename == "new document.txt":
    textContents = "It was a dark and stormy night..."
else:
    try:
        file = open(filename,"r")
        textContents = file.read()
        file.close()
    except:
        print("Could not open/read text file " + filename)
        textContents = "Error opening file " + filename
    
input_box = TextBox(app, text=textContents, width=80, height=16, multiline=True, scrollbar=True, command=wordCount)
input_box.font = "-apple-system" # MacOS system font, replace with something like Arial if not on a Mac
input_box.text_color = "blue"
input_box.text_size = 34
input_box.bg = "#FFFFE7"
wordText = Text(app, text="")
saveButton = PushButton(app, command=localSave, text="Save local")
status = Text(app, text="")
filename_box = TextBox(app, text=filename[:-4], width=20, height=1, multiline=False, scrollbar=False)

wordCount()
app.display()
