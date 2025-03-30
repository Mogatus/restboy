import tkinter as tk
from tkinter import ttk
from idlelib.tooltip import Hovertip
import RestBoyFunctions
from Request import Request
import requests


class RestBoyGUI:


    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rest Boy")
        self.root.geometry("1400x600")
        self.createMenu()
        
        # left side of GUI with folders and testcases
        self.leftFrame = ttk.Frame(self.root, relief="raised", borderwidth="1")
        self.leftFrame.pack(side='left', fill='y')

        # right side with tabbed requests
        self.rightFrame = ttk.Frame(self.root, relief="raised", borderwidth="1")
        self.rightFrame.pack(side='right', fill='both', expand=True)

        # add headers
        leftColHeader = ttk.Label(self.leftFrame, text="Collection", font=("Helvetica", 10))
        leftColHeader.pack(side='top', anchor='w')
        
        rightColHeader = ttk.Label(self.rightFrame, text="Requests", font=("Helvetica", 10))
        rightColHeader.pack(side='top', anchor='w')
        
        # add Treeview on left frame
        self.tree = self.createTree()
        
        # add Tabbed Pane on right frame
        self.notebookPane = self.createNotebook()
        self.openRequest("request_1")

        self.root.mainloop()


    def createNotebook(self):
        tabControl = ttk.Notebook(self.rightFrame)
        tabControl.pack(expand = 1, fill ="both")
        return tabControl


    def createTree(self):
        self.tree = ttk.Treeview(self.leftFrame, selectmode='browse')
        self.tree.pack(side='left', fill='y')
        vsb = ttk.Scrollbar(self.leftFrame, orient="vertical", command=self.tree.yview)
        vsb.pack(side='right', fill='y')

        self.tree.configure(yscrollcommand=vsb.set)

        f1 = self.tree.insert("",tk.END,text="Folder 1")
        f2 = self.tree.insert("",tk.END,text="Folder 2")
        self.tree.insert(f1,tk.END,text="File 1_1")
        self.tree.insert(f2,tk.END,text="File 2_1")

        return self.tree
    

    def createMenu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        collectionMenu = tk.Menu(menu)
        
        menu.add_cascade(label="Collection", menu=collectionMenu)

        collectionMenu.add_command(label="Open Collection", command=self.openCollection)
        collectionMenu.add_command(label="Export Collection", command=self.exportCollection)
        collectionMenu.add_separator()
        collectionMenu.add_command(label="Preferences", command=self.preferences)
        collectionMenu.add_command(label="Quit", command=self.root.quit)

        helpMenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="Help", command=self.help)


    def addRequestPane(self, request):
        print("addRequest by creating new tab in notebookPane")
        
        tab = ttk.Frame(self.notebookPane) 
        self.notebookPane.add(tab, text=request.name)

        # frame for Method, URL und send-Button
        urlFrame = ttk.Frame(tab, relief="raised", borderwidth="1")
        urlFrame.pack(side="top", fill="x")

        self.methods = ttk.Combobox(urlFrame, state="readonly", values=["GET", "POST", "PUT", "PATCH", "DELETE"])
        self.methods.set(request.method)
        self.methods.pack(side="left")

        self.urlEntry = ttk.Entry(urlFrame)
        self.urlEntry.insert(0, request.url)
        self.urlEntry.pack(side="left", expand=True, fill="x")

        sendButton = tk.Button(urlFrame, text ="Send", command = self.sendRequest)
        sendButton.pack(side="right")

        # frame for request attributes like params or body (left side) and response info (right side)
        requestInfoFrame = ttk.Frame(tab, relief="raised", borderwidth="1")
        requestInfoFrame.pack(side="bottom", fill="both", expand=True)

        self.requestPane = tk.Text(requestInfoFrame) # todo: tabbed pane with methods, body, ...
        self.requestPane.pack(side = "left", fill="both", expand=True)

        self.responsePane = tk.Text(requestInfoFrame)
        self.responsePane.pack(side = "right", fill="both", expand=True)

    def openCollection(self):
        print("Open Collection - to be done")


    def exportCollection(self):
        print("Export Collection - to be done")

    
    def openRequest(self, requestName):
        req = Request(requestName, "GET", "http://localhost:56135/xyna/ping?input=sepp", "")
        self.addRequestPane(req)


    def preferences(self):
        print("Preferences - to be done")

    def sendRequest(self):
        req = Request("", self.methods.get(), self.urlEntry.get(), "")
        resp = RestBoyFunctions.sendRequest(req)
        self.responsePane.insert(tk.INSERT, resp.text)


    def help(self):
        print("Help - to be done")