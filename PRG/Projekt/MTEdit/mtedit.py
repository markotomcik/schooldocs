import json
from tkinter import *
from PIL import Image, ImageTk
from tkinter import simpledialog, colorchooser, messagebox, filedialog

CANVAS_HEIGHT = 750
CANVAS_WIDTH = 1250
CANVAS_COLOR = "#ffffff"

MIN_SIZE = 1
MAX_SIZE = 10

class ResizeDialog(simpledialog.Dialog):
    def body(self, master):
        Label(master, text=L["Height:"]).grid(row=0, padx=10, pady=5)
        Label(master, text=L["Width:"]).grid(row=1, padx=10, pady=5)

        self.height = Entry(master)
        self.height.insert(0, app.canvas["height"])
        self.width = Entry(master)
        self.width.insert(0, app.canvas["width"])

        self.height.grid(row=0, column=1, padx=10, pady=5)
        self.width.grid(row=1, column=1, padx=10, pady=5)

        return self.height # initial focus

    def validate(self):
        if self.height.get().isdigit() and self.width.get().isdigit():
            self.result = {
                "height": self.height.get(),
                "width": self.width.get()
            }
            return 1
        else:
            messagebox.showwarning(title=L["Illegal value"], message=L["Not an integer. Please try again."])

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.master.title(L["MT Editor"])
        self.master.minsize(1000, 800)
        self.master.geometry("1440x810+125+75")
        self.master.configure(bg="white")

        self.tool = {
            "color": "#000000",
            "size": 1,
            "shape": L["pen"]
        }

        self.moves = []

        self.import_resources()
        self.create_widgets()
        self.create_menu()

        self.old_x = None
        self.old_y = None

        self.events()

    def import_resources(self):
        self.icons = {
            "toolbar": {
                "shape": {
                    L["pen"]: ImageTk.PhotoImage(Image.open("Resources/icons/pencil-alt-solid.png")),
                    L["circle"]: ImageTk.PhotoImage(Image.open("Resources/icons/circle-solid.png")),
                    L["rectangle"]: ImageTk.PhotoImage(Image.open("Resources/icons/square-solid.png")),
                    L["line"]: ImageTk.PhotoImage(Image.open("Resources/icons/slash-solid.png"))
                },
                "color": ImageTk.PhotoImage(Image.open("Resources/icons/palette-solid.png"))
            }
        }

    def events(self):
        self.canvas.bind("<Motion>", self.motion)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.master.bind("<Control-z>", lambda a : self.delete_moves)
        self.master.bind("<Control-d>", self.delete_all)
        self.master.bind("<Escape>", lambda a : self.master.quit())

    def motion(self, e):
        x, y = e.x, e.y
        self.statusbarItem["position"]["text"] = f"X: {x} Y: {y}"

    def paint(self, e):
        if self.tool["shape"] == L["pen"]:
            self.paint_pen(e)
        elif self.tool["shape"] == L["circle"]:
            self.paint_circle(e)
        elif self.tool["shape"] == L["rectangle"]:
            self.paint_rectangle(e)
        elif self.tool["shape"] == L["line"]:
            self.paint_line(e)

    def paint_pen(self, e):
        x, y = e.x, e.y
        self.statusbarItem["position"]["text"] = f"X: {x} Y: {y}"

        self.line_width = self.tool["size"]
        paint_color = self.tool["color"]
        if self.old_x and self.old_y:
            self.moves.append(self.canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.line_width, fill=paint_color, capstyle=ROUND, smooth=TRUE, splinesteps=36))
        self.old_x = e.x
        self.old_y = e.y

    def paint_circle(self, e):
        x, y = e.x, e.y
        self.statusbarItem["position"]["text"] = f"X: {x} Y: {y}"

        self.line_width = self.tool["size"]
        paint_color = self.tool["color"]
        if not(self.old_x and self.old_y):
            self.old_x = e.x
            self.old_y = e.y
            self.moves.append(self.canvas.create_oval(self.old_x, self.old_y, e.x, e.y, fill=paint_color, outline=paint_color))
        else:
            self.canvas.coords(self.moves[-1], self.old_x, self.old_y, e.x, e.y)

    def paint_rectangle(self, e):
        x, y = e.x, e.y
        self.statusbarItem["position"]["text"] = f"X: {x} Y: {y}"

        self.line_width = self.tool["size"]
        paint_color = self.tool["color"]
        if not(self.old_x and self.old_y):
            self.old_x = e.x
            self.old_y = e.y
            self.moves.append(self.canvas.create_rectangle(self.old_x, self.old_y, e.x, e.y, fill=paint_color, outline=paint_color))
        else:
            self.canvas.coords(self.moves[-1], self.old_x, self.old_y, e.x, e.y)

    def paint_line(self, e):
        x, y = e.x, e.y
        self.statusbarItem["position"]["text"] = f"X: {x} Y: {y}"

        self.line_width = self.tool["size"]
        paint_color = self.tool["color"]
        if not(self.old_x and self.old_y):
            self.old_x = e.x
            self.old_y = e.y
            self.moves.append(self.canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.line_width, fill=paint_color, capstyle=ROUND, smooth=TRUE, splinesteps=36))
        else:
            self.canvas.coords(self.moves[-1], self.old_x, self.old_y, e.x, e.y)

    def reset(self, e):
        self.old_x, self.old_y = None, None

    def delete_moves(self):
        if self.moves:
            self.canvas.delete(self.moves[-1])
            self.moves = self.moves[:-1]

    def change_language(self, lang="en"):
        response = messagebox.askyesnocancel(title=L["Language change"], message=L["Applying language changes requires reopening. Do you wish to do it now?"])
        if response:
            with open('Locales/lang.json', 'r') as file:
                json_data = json.load(file)
                json_data["default"] = lang
            with open('Locales/lang.json', 'w') as file:
                json.dump(json_data, file, indent=4)
            global do
            do = True
            self.master.destroy()
        elif response == None:
            return
        else:
            with open('Locales/lang.json', 'r') as file:
                json_data = json.load(file)
                json_data["default"] = lang
            with open('Locales/lang.json', 'w') as file:
                json.dump(json_data, file, indent=4)

    def create_menu(self):
        self.create_menuBar()
        self.create_popupMenu()

    def create_popupMenu(self):
        self.popupMenu = Menu(self.master, tearoff=0)

        backgroundMenu = Menu(self.popupMenu, tearoff=0)
        backgroundMenu.add_command(label=L["Color"], command=self.set_bg_color)
        backgroundMenu.add_command(label=L["Size"], command=self.set_bg_size)
        self.popupMenu.add_cascade(label=L["Background"], menu=backgroundMenu)

        self.popupMenu.add_command(label=L["Exit (Esc)"], command=self.master.quit)

        self.canvas.bind("<Button-3>", self.showMenu)

    def showMenu(self, e):
        self.popupMenu.post(e.x_root, e.y_root)

    def create_menuBar(self):
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        # mtedit
        mteditMenu = Menu(self.menu, tearoff=0)

        mteditMenu.add_command(label=L["Exit (Esc)"], command=self.master.quit)
        self.menu.add_cascade(label=L["MT Editor"], menu=mteditMenu)

        # edit
        editMenu = Menu(self.menu, tearoff=0)
        editMenu.add_command(label=L["Undo (Ctrl + Z)"], command=self.delete_moves)

        editMenu.add_separator()

        editMenu.add_command(label=L["Delete all (Ctrl + D)"], command=self.delete_all)

        self.menu.add_cascade(label=L["Edit"], menu=editMenu)

        # background
        backgroundMenu = Menu(self.menu, tearoff=0)
        backgroundMenu.add_command(label=L["Color"], command=self.set_bg_color)
        backgroundMenu.add_command(label=L["Size"], command=self.set_bg_size)

        backgroundMenu.add_separator()

        backgroundMenu.add_command(label=L["Reset"], command=self.reset_bg)

        self.menu.add_cascade(label=L["Background"], menu=backgroundMenu)

        # help
        settingsMenu = Menu(self.menu, tearoff=0)

        langMenu = Menu(settingsMenu, tearoff=0)
        for item in lang["languages"]:
            langMenu.add_command(label=lang[item]["name"], command=lambda lang=item: self.change_language(lang))

        settingsMenu.add_cascade(label=L["Language"], menu=langMenu)
        self.menu.add_cascade(label=L["Settings"], menu=settingsMenu)

    def create_widgets(self):
        self.create_main()
        self.create_toolbar()
        self.create_canvas()
        self.create_statusbar()

    def create_main(self):
        self.main = Frame(self.master, bg="white")
        self.main.grid(row=0, column=0, sticky="news")

        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(0, weight=1)

    def create_toolbar(self):
        self.toolbar = Frame(self.main, bd=1, relief=RAISED, bg="white")

        penColor = Button(self.toolbar, image=self.icons["toolbar"]["color"], bg="white", relief=FLAT, height=36, width=36, command=self.set_color)
        penColor.pack(padx=2, pady=2)
        scale = Scale(self.toolbar,length=150, from_=MIN_SIZE, to=MAX_SIZE, bg="white", relief=FLAT, bd=0, command=self.set_size)
        scale.pack(anchor=CENTER, padx=2, pady=2)

        penColor = Button(self.toolbar, image=self.icons["toolbar"]["shape"][L["pen"]], bg="white", relief=FLAT, height=36, width=36, command=lambda shape=L["pen"] : self.set_shape(shape))
        penColor.pack(padx=2, pady=2)
        penColor = Button(self.toolbar, image=self.icons["toolbar"]["shape"][L["circle"]], bg="white", relief=FLAT, height=36, width=36, command=lambda shape=L["circle"] : self.set_shape(shape))
        penColor.pack(padx=2, pady=2)
        penColor = Button(self.toolbar, image=self.icons["toolbar"]["shape"][L["rectangle"]], bg="white", relief=FLAT, height=36, width=36, command=lambda shape=L["rectangle"] : self.set_shape(shape))
        penColor.pack(padx=2, pady=2)
        penColor = Button(self.toolbar, image=self.icons["toolbar"]["shape"][L["line"]], bg="white", relief=FLAT, height=36, width=36, command=lambda shape=L["line"] : self.set_shape(shape))
        penColor.pack(padx=2, pady=2)
        
        self.toolbar.pack(side=LEFT, fill=Y, expand=False)

    def create_canvas(self):
        self.frame = Frame(self.main, bg="white")
        self.frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.canvas = Canvas(self.frame, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg=CANVAS_COLOR, cursor="crosshair")
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

    def create_statusbar(self):
        self.statusbar = Frame(self.master)
        self.statusbar.grid(row=1, column=0, sticky="news")
        
        self.statusbarItem = {
            "shape": Label(self.statusbar, text=L["Tool: "] + self.tool["shape"], width=15, bg="white", bd=1, relief=SUNKEN, anchor=W),
            "color": Label(self.statusbar, text=L["Tool color: "], bd=1, relief=SUNKEN, anchor=W, bg="white"),
            "color_icon": Label(self.statusbar, bd=1, relief=SUNKEN, anchor=W, bg="white"),
            "color_value": Label(self.statusbar, text=self.tool["color"], width=10, bd=1, relief=SUNKEN, anchor=W, bg="white"),

            "size": Label(self.statusbar, text=L["Size: "] + str(self.tool["size"]), width=10, bg="white", bd=1, relief=SUNKEN, anchor=W),

            "separator": Label(self.statusbar, bg="white", bd=1, relief=SUNKEN, anchor=W),

            "bg_color": Label(self.statusbar, text=L["Background color: "], bd=1, relief=SUNKEN, anchor=W, bg="white"),
            "bg_color_icon": Label(self.statusbar, bg="white", bd=1, relief=SUNKEN, anchor=W),
            "bg_color_value": Label(self.statusbar, text=self.canvas["bg"], width=10, bd=1, relief=SUNKEN, anchor=W, bg="white"),

            "bg_size": Label(self.statusbar, text=L["Background size: "] + self.canvas["height"] + "x" + self.canvas["width"], width=30, bg="white", bd=1, relief=SUNKEN, anchor=W),

            "position": Label(self.statusbar, text="X: 0 Y: 0", width=15, bd=1, relief=SUNKEN, anchor=W, bg="white")
        }

        self.statusbarCanvas = {
            "color_icon": Canvas(self.statusbarItem["color_icon"], height=10, width=10, bg=self.tool["color"]),
            "bg_color_icon": Canvas(self.statusbarItem["bg_color_icon"], height=10, width=10, bg=self.canvas["bg"])
        }
        
        for canvas in self.statusbarCanvas:
            self.statusbarCanvas[canvas].pack(side=LEFT)

        for item in self.statusbarItem:
            if item is "separator":
                self.statusbarItem[item].pack(side=LEFT, expand=True, fill=BOTH)
            elif item[-4:] == "icon":
                self.statusbarItem[item].pack(side=LEFT, fill=Y)
            else:
                self.statusbarItem[item].pack(side=LEFT)
        
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

    def reset_bg(self):
        self.canvas["bg"] = CANVAS_COLOR
        self.canvas["height"] = CANVAS_HEIGHT
        self.canvas["width"] = CANVAS_WIDTH

    def delete_all(self):
        self.canvas.delete("all")

    def set_bg_color(self):
        self.canvas["bg"] = colorchooser.askcolor(color=self.canvas["bg"], title=L["Background color"])[1]
        self.statusbarCanvas["bg_color_icon"]["bg"] = self.canvas["bg"]
        self.statusbarItem["bg_color_value"]["text"] = self.canvas["bg"]

    def set_bg_size(self):
        dialog = ResizeDialog(self.master, title=L["Background size"])
        if dialog.result:
            self.canvas["height"] = dialog.result["height"]
            self.canvas["width"] = dialog.result["width"]
            self.statusbarItem["bg_size"]["text"] = L["Background size: "] + self.canvas["height"] + "x" + self.canvas["width"]
    
    def set_color(self):
        self.tool["color"] = colorchooser.askcolor(color=self.tool["color"], title=L["Tool color"])[1]
        self.statusbarCanvas["color_icon"]["bg"] = self.tool["color"] 
        self.statusbarItem["color_value"]["text"] = self.tool["color"] 

    def set_size(self, size):
        self.tool["size"] = size
        self.statusbarItem["size"]["text"] = L["Size: "] + self.tool["size"] 

    def set_shape(self, shape):
        self.tool["shape"] = shape
        self.statusbarItem["shape"]["text"] = L["Tool: "] + self.tool["shape"]

do = True

while do:
    do = False
    with open("Locales/lang.json") as json_file:
        lang = json.load(json_file)

    with open("Locales/en.json") as json_file:
        en = {}
        en_tmp = json.load(json_file)
        for item in en_tmp:
            en[item] = item

    if lang["default"] != "en":
        with open("Locales/" + lang[lang["default"]]["file"]) as json_file:
            L = json.load(json_file)
    else:
        L = en

    root = Tk()
    app = Application(master=root)
    app.mainloop()