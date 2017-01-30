from tkinter import *

root = Tk()
root.title("Meditation center Registration")
topFrame = Frame(root)
topFrame.grid(row=0, column = 1)
myFramePersonal = Frame(root)
myFramePersonal.grid(row=1, column=0)
myFrameCourse = Frame(root)
myFrameCourse.grid(row=1, column=2)
myFrameExperience = Frame(root)
myFrameExperience.grid(row=1, column=1)

#set Label on the top
Label(topFrame, text="APPLICATION FORM", font="80px", bg="green").grid(stick=E)


#set Personal information on Frame myFramePersonal
sex=StringVar()
sex.set(None)
Radiobutton(myFramePersonal, text="Male", variable=sex, value="Male").grid(row=0, column=0, sticky=W)
Radiobutton(myFramePersonal, text="Female", variable=sex, value="Female").grid(row=1, column=0, sticky=W)

#set Radiobutton for retreat
Label(myFramePersonal, text="Course Type:").grid(row=2, column=0, sticky=W)
course = BooleanVar()
radio = ["Intro", "Basic", "Reatreat", "Assistant"]
radio1 = []

for x in radio:
	r = Radiobutton(myFramePersonal, text=x, variable=course, value=x)
	r.grid(row=radio.index(x)+3, column=0, sticky=W)
	radio1.append(r)

def form():
	data = ["First Name:", "Last Name:", "Date of birth", "Country:", 
	"Address/P.O.Box:", "Phone:", "Email:", "Education:", "Occupation:"]
	for x in data:
		Label(myFramePersonal, text=x, font="5px").grid(sticky=W)
		Entry(myFramePersonal).grid(sticky=W)	

form()

# set infromation on Frame myFrameExperience
Label(myFrameExperience, text="PREVIOUS MEDITATION EXPERIENCE", font="40px").grid(row=0, column=1)

header = ["Location", "Technique", "Teacher", "Date"]
head = []
for x in header:
	h = Label(myFrameExperience, text=x, font="10px")
	h.grid(row=1, column=header.index(x))
	head.append(h)
	
rows = []
for i in range(5):
	cols = []
	for j in range(4):
		e = Entry(myFrameExperience)
		e.grid(row=i+2, column=j, sticky=NSEW)
		cols.append(e)
		rows.append(cols)
	
#set health bar
Label(myFrameExperience, text="PHYSICAL HEALTH PROBLEMS", font="70px").grid(row=8, column=1)

header_med = ["Medical condition", "Treatment", "Duration", "Present condition"]
head_med = []
print(head_med)
for x in header_med:
	h = Label(myFrameExperience, text=x, font="20px")
	h.grid(row=9, column=header_med.index(x))
	head_med.append(h)
	
rows2 = []
for i in range(5):
	cols = []
	for j in range(4):
		e = Entry(myFrameExperience)
		e.grid(row=i+11, column=j, sticky=NSEW)
		cols.append(e)
		rows2.append(cols)

Label(myFrameExperience, text="MENTAL HEALTH PROBLEMS", font="70px").grid(row=17, column=1)

header_ment = ["Medical condition", "Treatment", "Duration", "Present condition"]
head_ment = []
for x in header_med:
	h = Label(myFrameExperience, text=x, font="20px")
	h.grid(row=18, column=header_ment.index(x))
	head_ment.append(h)
	
rows3 = []
print (rows3)
for i in range(5):
	cols = []
	for j in range(4):
		e = Entry(myFrameExperience)
		e.grid(row=i+20, column=j, sticky=NSEW)
		cols.append(e)
		rows3.append(cols)

Label(myFrameExperience, text="Addictions:").grid(row=26, sticky=W)
Entry(myFrameExperience).grid(row=27)

Label(myFrameCourse, text="Course finished:").grid()
vc=StringVar()
c = Entry(myFrameCourse, textvariable=vc)
c.grid()

def save():
    text = c.get() 
    with open("test.txt", "w") as f:
        f.writelines(text)


Button(myFrameCourse, text="Submit", command=save).grid()



root.mainloop()