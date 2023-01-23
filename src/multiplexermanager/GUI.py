"""MODULES"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import os
import shutil
from errno import EEXIST

import fileopener as fo
import operations as ops
import plotting as plot
import FETs as fet
import CV as cv


'''LOCAL DIRECTORIES'''
cwd = os.getcwd()

try:
    os.makedirs(cwd + '/data')
except OSError as exc:
    if exc.errno == EEXIST and os.path.isdir(cwd + '/data'):
        pass
    else: 
        raise

try:
    os.makedirs(cwd + '/plots')
except OSError as exc:
    if exc.errno == EEXIST and os.path.isdir(cwd + '/plots'):
        pass
    else:
        raise

ifp = os.path.expanduser('~/Documents/')


'''FUNCTIONS - SETTINGS'''
def settings():
    pass

def guide():
    '''Opens a guide to using the application'''
    help_wdw = tk.Toplevel()
    help_wdw.title('Help guide')
    help_wdw.iconbitmap('graphicon.ico')
    help_wdw.geometry('250x250')
    help_wdw.grab_set()
    
    tk.Label(help_wdw, text = 'No-one is coming to help you').pack()

def about():
    '''Opens a window with information about the application'''
    about_wdw = tk.Toplevel()
    about_wdw.title('About the app')
    about_wdw.iconbitmap('graphicon.ico')
    about_wdw.geometry('250x250')
    about_wdw.grab_set()

    about_txt = [
        'Multiplexer Manager v.1.3.0',
        ' ',
        'made by', 
        'Dr. Steven Linfield',
        ' ',
        'with support from:', 
        'Dr. Oliver Rodriguez', 
        'Maria Wroblewska', 
        'Dr. Marcin Szymon Filipiak']

    for ix in about_txt:
        tk.Label(about_wdw, text = ix).pack()


'''FUCTIONS - FILES'''

'''File management'''
def importdata():
    '''Opens a dialog box which allows users to import files into the /data folder'''
    global ifp
    global import_menu

    root.filenames = filedialog.askopenfilenames(initialdir = ifp, title = 'Select data file(s) to import', filetypes = (('.csv files','*.csv'),('all files','*.*')))
    
    for ix in root.filenames:
        if ix != '' and ix[-4:] == '.csv':
            ifp = os.path.dirname(root.filenames[-1])
            for ix in root.filenames:
                fn = os.path.basename(ix)
                if fn not in import_list: 
                    import_list.append(fn)
                else:
                    pass 
                shutil.copyfile(ix, cwd + '/data/' + fn)
        else:
            pass
    
    updatefileselection()

def updatefileselection():
    '''Detects changes in the list of uploaded files and activates/deactivates the import menu accordingly'''
    global import_menu
    
    if len(import_list) > 1:
        import_menu.destroy()
        import_menu = tk.OptionMenu(import_frm, import_var, *import_list)
        import_menu.grid(row = 1, column = 0, columnspan = 4, pady = 2, sticky = tk.NSEW)
        import_menu['state'] = tk.NORMAL
    
    if len(import_list) == 1:
        import_menu.destroy()
        import_menu = tk.OptionMenu(import_frm, import_var, *import_list)
        import_menu.grid(row = 1, column = 0, columnspan = 4, pady = 2, sticky = tk.NSEW)
        import_menu['state'] = tk.DISABLED

def deletedata():
    '''Deletes the selected file from the imported data list'''
    try:
        os.remove(cwd + '/data/' + import_var.get())
        import_list.remove(import_var.get())
        import_var.set(import_list[0])
        updatefileselection()

    except:
        messagebox.showerror('File error','No file was selected for deletion')

def updatefiledetails(*args):
    
    if import_var.get() == import_list[0]:
        clear_btn['state'] = tk.DISABLED
        delete_btn['state'] = tk.DISABLED
        bipot_option1['state'] = tk.DISABLED
        bipot_option2['state'] = tk.DISABLED
        channels_option['state'] = tk.DISABLED
        upload_btn['state'] = tk.DISABLED
    
    if import_var.get() != import_list[0]:
        import_btn['state'] = tk.NORMAL
        import_menu['state'] = tk.NORMAL
        clear_btn['state'] = tk.NORMAL
        delete_btn['state'] = tk.NORMAL
        bipot_option1['state'] = tk.NORMAL
        bipot_option2['state'] = tk.NORMAL
        channels_option['state'] = tk.NORMAL
        upload_btn['state'] = tk.NORMAL


def uploaddata():
    global instance
    global array
    global elec1set
    global elec2set
    global channelset
    global expset
    
    try:
        instance = fo.Multiplexer(cwd + '/data/' + import_var.get(), bipot_var.get(), int(channels_var.get()))
        array = instance.array
        updatedatafunctions()
        retract_btn['state'] = tk.NORMAL
        
        import_btn['state'] = tk.DISABLED
        import_menu['state'] = tk.DISABLED
        clear_btn['state'] = tk.DISABLED
        delete_btn['state'] = tk.DISABLED
        bipot_option1['state'] = tk.DISABLED
        bipot_option2['state'] = tk.DISABLED
        channels_option['state'] = tk.DISABLED
        upload_btn['state'] = tk.DISABLED

        elec1set = 1
        elec2set = 1
        channelset = []
        for ix in range(0, array.shape[0]):
            channelset.append(1)
        expset = []
        for ix in range(0, array.shape[1]):
            expset.append(1)

    except:
        messagebox.showerror('File error','No file was selected for upload')

def retractdata():
    global instance
    global array

    instance = None
    array = None

    retract_btn['state'] = tk.DISABLED
    data_check_btn['state'] = tk.DISABLED
    data_select_btn['state'] = tk.DISABLED
    plot_experiments['state'] = tk.DISABLED
    plot_channels['state'] = tk.DISABLED
    plot_btn['state'] = tk.DISABLED
    updatefiledetails()

def updatedatafunctions():
    '''Activates all of the file buttons after upload'''
    data_check_btn['state'] = tk.ACTIVE
    data_select_btn['state'] = tk.ACTIVE
    plot_experiments['state'] = tk.ACTIVE
    plot_channels['state'] = tk.ACTIVE
    plot_btn['state'] = tk.ACTIVE


def open_checker():
    '''Opens'''
    global checker
    global cc_box
    global ce_box
    global cw_box
    global data
    global array
    global checkercanvas
    
    checker = tk.Toplevel()
    checker.title('Data checker')
    checker.iconbitmap('graphicon.ico')
    checker.geometry('900x600')
    checker.grab_set()

    try:
        plt.close
        checkercanvas.destroy()
    except: pass

    tk.Label(checker, text = 'Channel:').grid(row = 0, column = 0)
    tk.Label(checker, text = 'Experiment:').grid(row = 1, column = 0)
    tk.Label(checker, text = 'WE:').grid(row = 2, column = 0)
    
    cc_var = tk.StringVar()
    cc_box = tk.Entry(checker, textvariable = cc_var, width = 15)
    cc_box.insert(0, '1')
    cc_box.grid(row = 0, column = 1)
    cc_var.trace("w", updatechecker)

    ce_var = tk.StringVar()
    ce_box = tk.Entry(checker, textvariable = ce_var, width = 15)
    ce_box.insert(0, '1')
    ce_box.grid(row = 1, column = 1)
    ce_var.trace("w", updatechecker)
    
    cw_var = tk.StringVar()
    cw_box = tk.Entry(checker, textvariable = cw_var, width = 15)
    cw_box.insert(0, '1')
    cw_box.grid(row = 2, column = 1)
    cw_var.trace("w", updatechecker)

    if array.shape[2] == 2:
        cw_box['state'] = tk.DISABLED

    tk.Button(checker, text = 'Update', command = updatechecker).grid(row = 3, column = 0, columnspan = 2)

    data = ttk.Treeview(checker)

    data['columns'] = ('Voltage', 'Current')

    data.column("#0", width = 0, stretch = tk.NO)
    data.column("Voltage", anchor = tk.CENTER, width = 100, minwidth = 50)
    data.column("Current", anchor = tk.CENTER, width = 100, minwidth = 50)

    data.heading("#0", text="", anchor = tk.CENTER)
    data.heading("Voltage", text="E / V", anchor = tk.CENTER)
    data.heading("Current",text="i / A", anchor = tk.CENTER)
    
    iw = int(cc_box.get()) - 1
    ix = int(ce_box.get()) - 1
    if int(cw_box.get()) == 1:
        iy = 0
    elif int(cw_box.get()) == 2:
        iy = 2
    else: iy = None

    for iz in range(array.shape[3]):
        data.insert(parent = '', index = 'end', iid = iz, text = '', 
        values = (array[iw,ix,iy,iz],array[iw,ix,iy + 1,iz]))

    data.grid(row = 4, column = 0, columnspan = 2)
   
    x = array[iw,ix,iy,:]
    y = array[iw,ix,iy + 1,:]

    fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
    ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
    ax.plot(x, y, linestyle = '-', color = 'red', marker = None, label = '')

    checkercanvas = tk.Canvas(checker)
    checkercanvas.grid(row = 0, column = 2, rowspan = 5)
    checkergraph = FigureCanvasTkAgg(fig, checkercanvas)
    checkergraph.draw()
    checkergraph.get_tk_widget().pack()


def updatechecker(*args):
    global checker 
    global cc_box
    global ce_box
    global cw_box
    global data
    global array
    global checkercanvas
    
    try:
        data.destroy()
        checkercanvas.destroy()
        plt.close()

        data = ttk.Treeview(checker)

        data['columns'] = ('Voltage', 'Current')

        data.column("#0", width = 0, stretch = tk.NO)
        data.column("Voltage", anchor = tk.CENTER, width = 100, minwidth = 50)
        data.column("Current", anchor = tk.CENTER, width = 100, minwidth = 50)

        data.heading("#0", text="", anchor = tk.CENTER)
        data.heading("Voltage", text="E / V", anchor = tk.CENTER)
        data.heading("Current",text="i / A", anchor = tk.CENTER)
        
        iw = int(cc_box.get()) - 1
        ix = int(ce_box.get()) - 1
        if int(cw_box.get()) == 1:
            iy = 0
        elif int(cw_box.get()) == 2:
            iy = 2
        else: iy = None

        for iz in range(array.shape[3]):
            data.insert(parent = '', index = 'end', iid = iz, text = '', 
            values = (array[iw,ix,iy,iz],array[iw,ix,iy + 1,iz]))

        data.grid(row = 4, column = 0, columnspan = 2)

        x = array[iw,ix,iy,:]
        y = array[iw,ix,iy + 1,:]

        fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
        ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        ax.plot(x, y, linestyle = '-', color = 'red', marker = None, label = '')

        checkercanvas = tk.Canvas(checker)
        checkercanvas.grid(row = 0, column = 2, rowspan = 5)
        checkergraph = FigureCanvasTkAgg(fig, checkercanvas)
        checkergraph.draw()
        checkergraph.get_tk_widget().pack()
    except:
        pass


def dataselect():
    '''Opens a window that allows users to select data to plot'''
    global selector
    global elec1var
    global elec2var
    global chanvarlist
    global expvarlist
    global elec1set
    global elec2set
    global channelset
    global expset

    selector = tk.Toplevel()
    selector.title('Data selection')
    selector.iconbitmap('graphicon.ico')
    selector.grab_set()
    tk.Button(selector, text = 'Select all', command = select).pack(fill = 'x', expand = True)
    tk.Button(selector, text = 'Deselect all', command = deselect).pack(fill = 'x', expand = True)
    electrode_frame = tk.LabelFrame(selector, text = 'Electrodes')
    electrode_frame.pack()
    channel_frame = tk.LabelFrame(selector, text = 'Channels')
    channel_frame.pack()
    experiments_frame = tk.LabelFrame(selector, text = 'Experiments')
    experiments_frame.pack()
    
    elec1var = tk.IntVar()
    elec2var = tk.IntVar()
    we1 = tk.Checkbutton(electrode_frame, text = 'WE1', variable = elec1var)
    we1.grid(row = 0, column = 0)
    we2 = tk.Checkbutton(electrode_frame, text = 'WE2', variable = elec2var)
    we2.grid(row = 0, column = 1)

    chanvarframe = tk.Frame(channel_frame)
    chanvarframe.grid(row = 0, column = 0, rowspan = 2)
    chanvarlist = {}
    for ix in range(1, array.shape[0] + 1):
        n = (ix -1) % 8
        m = (ix - 1) // 8
        chanvarlist[ix] = tk.IntVar()
        tk.Checkbutton(chanvarframe, text = str(ix), variable = chanvarlist[ix]).grid(row = m, column = n)
    all_channels = tk.Button(channel_frame, text = 'Select all', command = setchantrue)
    all_channels.grid(row = 0, column = 1)
    none_channels = tk.Button(channel_frame, text = 'Deselect all', command = setchanfalse)
    none_channels.grid(row = 1, column = 1)
  

    expvarframe = tk.Frame(experiments_frame)
    expvarframe.grid(row = 0, column = 0, rowspan = 2)
    expvarlist = {}
    for ix in range(1, array.shape[1] + 1):
        n = (ix -1) % 8
        m = (ix - 1) // 8
        expvarlist[ix] = tk.IntVar()
        tk.Checkbutton(expvarframe, text = str(ix), variable = expvarlist[ix]).grid(row = m, column = n)
    all_exp = tk.Button(experiments_frame, text = 'Select all', command = setexptrue)
    all_exp.grid(row = 0, column = 1)
    none_exp = tk.Button(experiments_frame, text = 'Deselect all', command = setexpfalse)
    none_exp.grid(row = 1, column = 1)

    elec1var.set(elec1set)
    elec2var.set(elec2set)
    for ix in chanvarlist:
        iy = channelset[ix - 1]
        chanvarlist[ix].set(iy)
    for ix in expvarlist:
        iy = expset[ix - 1]
        expvarlist[ix].set(iy)

    tk.Button(selector, text = 'Use selected experiments', command = extractselection).pack(fill = 'x', expand = True)


def select():
    global elec1var
    global elec2var
    global chanvarlist
    global expvarlist

    elec1var.set(1)
    elec2var.set(1)
    for ix in chanvarlist:
        chanvarlist[ix].set(1)
    for iy in expvarlist:
        expvarlist[iy].set(1)

def deselect():
    global elec1var
    global elec2var
    global chanvarlist
    global expvarlist

    elec1var.set(0)
    elec2var.set(0)
    for ix in chanvarlist:
        chanvarlist[ix].set(0)
    for iy in expvarlist:
        expvarlist[iy].set(0)

def setchantrue():
    global chanvarlist

    for ix in chanvarlist:
        chanvarlist[ix].set(1)

def setchanfalse():
    global chanvarlist

    for ix in chanvarlist:
        chanvarlist[ix].set(0)

def setexptrue():
    global expvarlist

    for ix in expvarlist:
        expvarlist[ix].set(1)

def setexpfalse():
    global expvarlist

    for ix in expvarlist:
        expvarlist[ix].set(0)

def extractselection():
    global ex
    global ey
    global ez
    global elec1set
    global elec2set
    global channelset
    global expset

    warning1 = False
    warning2 = False
    warning3 = False 
    if elec1var.get() == 1 and elec2var.get() == 0:
        ex = [0,1]

    if elec1var.get() == 0 and elec2var.get() == 1:
        ex = [2,3]
    if elec1var.get() == 1 and elec2var.get() == 1:
        ex = [0,1,2,3]
    if elec1var.get() == 0 and elec2var.get() == 0:
        warning1 = True

    chanvalue = []
    ey = []
    for ix in chanvarlist:
        chanvalue.append(chanvarlist[ix].get())
        if chanvarlist[ix] == 1:
            ey.append(ix)
    if 1 not in chanvalue:
        warning2 = True

    expvalue = []
    ez = []
    for ix in expvarlist:
        expvalue.append(expvarlist[ix].get())
        if expvarlist[ix] == 1:
            ez.append(ix)
    if 1 not in expvalue:
        warning3 = True

    elec1set = elec1var.get()
    elec2set = elec2var.get()
    channelset = chanvalue
    expset = expvalue

    if warning1 == False and warning2 == False and warning3 == False:
        selector.destroy()

def experiments():
    pass

def channels():
    for ix in ey:    
        fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
        ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        ax.set_title('Channel ' + str(ix + 1), loc = 'center', pad = 20, fontsize = 15)
            
        for iy in ex:
            ax.plot(input[ix,iy,ez[0],:], input[ix,iy,ez[1],:], linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None )
            try:
                ax.plot(input[ix,iy,ez[2],:], input[ix,iy,ez[3],:], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = str(iy+1))
            except:
                pass

        plt.legend(loc = 'best')
        plt.show()
    plt.close()
   
    #FigureCanvasTkAgg(figure, root).pack()

def plotter(x,y):
    global plt
    global fig
    global ax
    global canvas 
    
          
    fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
    ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
    ax.plot(array[x,y,2,:], array[x,y,3,:], linestyle = '-', color = 'red', marker = None, label = '')

    canvas = FigureCanvasTkAgg(fig, canvas)
    canvas.draw()
    canvas.get_tk_widget().pack()

'''FUNCTIONS - VIEWING'''
def previous():
    pass

def next():
    pass

def plotsettings():
    pass

def saveimage():
    pass

def savepdf():
    pass


'''FUNCTIONS - OPERATIONS'''


'''FUNCTIONS - CALCULATOR'''





"""ROOT"""
# Create the main graphical interface under the root variable
root = tk.Tk()
# Set the title of the main graphical interface
root.title('Multiplexer Manager')
# Set the icon displayed next to the grahical interface title
root.iconbitmap('graphicon.ico')
root.geometry('1065x540')


"""FRAMES"""
title = tk.Frame(root, text = None, borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 3)
title.grid(row = 0, column = 0, padx = 4, pady = 2, sticky = tk.NSEW)
options = tk.Frame(root, text = None, borderwidth = 4, relief = tk.GROOVE, padx = 0, pady = 0)
options.grid(row = 0, column = 1, columnspan = 4, padx = 4, pady = 2, sticky = tk.NSEW)
file = tk.Frame(root, text = None, borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
file.grid(row = 1, column = 0, padx = 2, pady = 2, rowspan = 2, sticky = tk.NSEW)
viewer = tk.Frame(root, text = None, borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
viewer.grid(row = 1, column = 1, rowspan = 2, padx = 2, pady = 2, sticky = tk.NSEW)
operators = tk.LabelFrame(root, text = 'Operations', borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
operators.grid(row = 1, column = 2, padx = 2, pady = 2, sticky = tk.NSEW)
calculator = tk.LabelFrame(root, text = 'Calculator', borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
calculator.grid(row = 2, column = 2, padx = 2, pady = 2, sticky = tk.NSEW)


"""TITLE"""
tk.Label(title, text = 'Multiplexer Manager v1.3.0', pady = 2).pack()


"""OPTIONS"""
tk.Button(options, text = 'Settings', padx = 5, command = settings).grid(row = 0, column = 0, padx = 2, sticky = tk.NSEW)
tk.Button(options, text = 'Help', padx = 5, command = guide).grid(row = 0, column = 1, padx = 2, sticky = tk.NSEW)
tk.Button(options, text = 'About', padx = 5, command = about).grid(row = 0, column = 2, padx = 2, sticky = tk.NSEW)


"""FILE"""

'''File management frame'''
import_frm = tk.LabelFrame(file, text = 'File management', padx = 1, pady = 1)
import_frm.grid(row = 0, column = 0, sticky = tk.NSEW, pady = 4)

'''File management widgets'''
import_btn = tk.Button(import_frm, text = 'Import file(s)', command = importdata, padx = 10, width = 40)
import_btn.grid(row = 0, column = 0, columnspan = 4, sticky = tk.NSEW, pady = 2)

import_list = ['Select a file']
import_var = tk.StringVar()
import_var.set(import_list[0])
import_menu = tk.OptionMenu(import_frm, import_var, *import_list)
import_menu.grid(row = 1, column = 0, columnspan = 4, sticky = tk.NSEW, pady = 2) 
import_menu['state'] = tk.DISABLED
import_var.trace("w", updatefiledetails)

clear_btn = tk.Button(import_frm, text = 'Clear File',command = lambda: import_var.set(import_list[0]))
clear_btn.grid(row = 2, column = 0, columnspan = 2, pady = 2, sticky = tk.NSEW)
clear_btn['state'] = tk.DISABLED
delete_btn = tk.Button(import_frm, text = 'Delete File',command = deletedata)
delete_btn.grid(row = 2, column = 2, columnspan = 2, sticky = tk.NSEW, pady = 2)
delete_btn['state'] = tk.DISABLED

bipot_label = tk.Label(import_frm, text = 'Bipot?')
bipot_label.grid(row = 3, column = 0, columnspan = 2)
channel_label = tk.Label(import_frm, text = 'No. of channels:')
channel_label.grid(row = 3, column = 2, columnspan = 2)

bipot_var = tk.BooleanVar()
bipot_option1 = tk.Radiobutton(import_frm, text = 'Yes', variable = bipot_var, value = True)
bipot_option1.grid(row = 4, column = 0, columnspan = 2) 
bipot_option1['state'] = tk.DISABLED
bipot_option2 = tk.Radiobutton(import_frm, text = 'No', variable = bipot_var, value = False)
bipot_option2.grid(row = 5, column = 0, columnspan = 2) 
bipot_option2['state'] = tk.DISABLED

channels_var = tk.StringVar()
channels_option = tk.Spinbox(import_frm, from_ = 1, to = 16, textvariable = channels_var, wrap = False)
channels_option.grid(row = 4, column = 2, rowspan = 2, columnspan = 2)
channels_option['state'] = tk.DISABLED

upload_btn = tk.Button(import_frm, text = 'Upload File', command = uploaddata)
upload_btn.grid(row = 6, column = 0, columnspan = 4, sticky = tk.NSEW)
upload_btn['state'] = tk.DISABLED

retract_btn = tk.Button(import_frm, text = 'Retract file', command = retractdata)
retract_btn.grid(row = 7, column = 0, columnspan = 4, sticky = tk.NSEW)
retract_btn['state'] = tk.DISABLED

'''Data checking frame'''
checker_frm = tk.LabelFrame(file, text = 'Data checker', padx = 1, pady = 1)
checker_frm.grid(row = 1, column = 0, columnspan = 4, pady = 4, sticky = tk.NSEW)

'''Data checking widgets'''
data_check_btn = tk.Button(checker_frm, text = 'Open data checker', command = open_checker)
data_check_btn.pack(fill = 'x', expand = True)
data_check_btn['state'] = tk.DISABLED


'''Data selection frame'''
data_select_frm = tk.LabelFrame(file, text = 'Data selection', padx = 1, pady = 1)
data_select_frm.grid(row = 2, column = 0, pady = 4, sticky = tk.NSEW)

'''Data selection widgets'''
data_select_btn = tk.Button(data_select_frm, text = 'Select data sets to plot', command = dataselect)
data_select_btn.pack(fill = 'x', expand = True)
data_select_btn['state'] = tk.DISABLED


'''Data plotting frame'''
data_plotting_frm = tk.LabelFrame(file, text = 'Data plotting', padx = 1, pady = 1)
data_plotting_frm.grid(row = 3, column = 0, pady = 4, sticky = tk.NSEW)

'''Data plotting widgets'''
plot_channels = tk.Button(data_plotting_frm, text = 'Compare experiments')
plot_channels.pack(fill = 'x', expand = True)
plot_channels['state'] = tk.DISABLED
plot_experiments = tk.Button(data_plotting_frm, text = 'Compare channels', command = channels)
plot_experiments.pack(fill = 'x', expand = True)
plot_experiments['state'] = tk.DISABLED
plot_btn = tk.Button(data_plotting_frm, text = 'Plot all selected data', command = plotter)
plot_btn.pack(fill = 'x', expand = True)
plot_btn['state'] = tk.DISABLED



"""VIEWER"""
back_btn = tk.Button(viewer, text = '<')
back_btn.grid(row = 0, column = 0)
canvas = tk.Canvas(viewer, width = 400, height = 400)
canvas.grid(row = 0, column = 1, columnspan = 2)
forward_btn = tk.Button(viewer, text = '>')
forward_btn.grid(row = 0, column = 3)

fig_set = tk.Button(viewer, text = 'Plot settings')
fig_set.grid(row = 1, column = 0, columnspan = 4, sticky = tk.NSEW)

clear_fig = tk.Button(viewer, text = 'Clear figures')
clear_fig.grid(row = 2, column = 0, columnspan = 4, sticky = tk.NSEW)

image_btn = tk.Button(viewer, text = 'Save figures as images')
image_btn.grid(row = 3, column = 0, columnspan = 2, sticky = tk.NSEW)
pdf_btn = tk.Button(viewer, text = 'Save figures to PDF')
pdf_btn.grid(row = 3, column = 2, columnspan = 2, sticky = tk.NSEW)



"""OPERATORS"""
tk.Label(operators, text ='Blank').pack()


"""CALCULATOR"""
tk.Label(calculator, text ='Select dataset:').grid(row = 0, column = 0, sticky = tk.NSEW)
variable = tk.StringVar()
data_names = ['']
data_OM = tk.OptionMenu(calculator, variable, *data_names)
data_OM.grid(row = 1, column = 0, sticky = tk.NSEW) 
tk.Button(calculator, text = 'Upload').grid(row = 1, column = 1, sticky = tk.NSEW)

tk.Label(calculator, text = '     ').grid(row = 2, column = 0)

tk.Label(calculator, text = 'Select a variable:').grid(row = 3, column = 0, sticky = tk.NSEW)
tk.Entry(calculator).grid(row = 3, column = 1)
variables = ['A', 'V']
d = tk.StringVar()
variables_OM = tk.OptionMenu(calculator, d, *variables)
variables_OM.grid(row = 3, column = 2)

tk.Button(calculator, text = 'Calculate').grid(row = 4, column = 0, columnspan = 3)


"""END"""
plt.close()
root.mainloop()
plt.close()