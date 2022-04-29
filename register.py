#!/usr/bin/env python3
# coding = utf-8

# https://www.youtube.com/watch?v=quSM7kHEy9k&t=77s
# Original Credit -> Rangesh @ Web Code
# 12:10, 14:29, 15:56, 28:37, 30:53

# Craig Miles

import tkinter
import os                         # directory paths
from PIL import Image, ImageTk    # pip install Pillow / background images
from tkinter import font          # that would be for fonts
from tkinter import ttk           # combo box
from tkinter import messagebox    # error / information messages

BASE_DIR = os.path.dirname( os.path.abspath( __file__ ))  # This directory

class Register:
    def __init__( self, parent ):
        self.root = parent
        self.initUI()

    def initUI( self ):
        self.root.title( 'Registeration Window' )
        self.geometry = self.screen_size( size = 0.75 )
        # print( self.geometry )
        self.root.geometry( self.geometry )
        self.center_root()
        self.root.configure( background = 'deep sky blue' )
        self.root.resizable( False, False )
        self.setup_fonts()
        self.setup_variables()
        self.setup_background_image()
        self.setup_left_image()
        self.setup_frames()
                
    def screen_size( self, size ):
        # Obtain desired screen size
        width = self.root.winfo_screenwidth() * size
        height = self.root.winfo_screenheight() * size
        return( '{}x{}+{}+{}' 
        .format( int( width ), int( height ), 0, 0 ))

    def center_root( self ):
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        pos_right = \
        int( self.root.winfo_screenwidth() // 2 - window_width // 2 )
        pos_down = \
        int( self.root.winfo_screenheight() // 2 - window_height // 2 )
        self.root.geometry( '{}x{}+{}+{}'
        .format( window_width, window_height, pos_right, pos_down ))
        
    def setup_fonts( self ):
        self.title_font = font.Font( family = 'DejaVu Serif',
                                   size = 10,
                                   weight = 'bold' )
        
        self.lbl_font = font.Font( family = 'DejaVu Serif',
                                   size = 16,
                                   weight = 'bold' )
        
        self.ent_font = font.Font( family = 'FreeSerif',
                                   size = 18,
                                   weight = 'bold' )
        
        self.btn_font = font.Font( family = 'FreeMono',
                                   size = 16,
                                   weight = 'bold' )
        
        self.message_font = font.Font( family = 'Bitstream Charter',
                                       size = 26,
                                       weight = 'bold' )
        self.test_font = font.Font( family = 'Liberation Serif',
                                    size = 26,
                                    weight = 'normal' )
        
    def setup_variables( self ):
        self.bg_image = os.path.join( BASE_DIR, r'images/176236.jpg' )
        self.left_image = os.path.join( BASE_DIR, r'images/1114690.jpg' )
        self.reg_btn_image = os.path.join( BASE_DIR, r'images/button_register.png' )
        self.login_btn_image = os.path.join( BASE_DIR, r'images/log-in.png' )
        self.var_fname = tkinter.StringVar()
        self.var_lname = tkinter.StringVar()
        self.var_contact = tkinter.StringVar()
        self.var_email = tkinter.StringVar()
        self.var_security = tkinter.StringVar()
        self.var_answer = tkinter.StringVar()
        self.var_password = tkinter.StringVar()
        self.var_confirm = tkinter.StringVar()
        
        
    def setup_background_image( self ):
        #print( self.root.winfo_width(), self.root.winfo_height() )
        w = self.root.winfo_width()   # 1440
        h = self.root.winfo_height()  # 810
        img_tmp = Image.open( self.bg_image )
        img = img_tmp.resize(( w, h ), Image.Resampling.LANCZOS )
        self.bg_tmp =  ImageTk.PhotoImage( img )
        bg = tkinter.Label( self.root, image = self.bg_tmp )
        bg.place( x = 0, y = 0, relwidth = 1, relheight = 1 )
        
    def setup_left_image( self ):
        w = int( 400 )
        h = int( 550 )
        tmp_img = Image.open( self.left_image )
        resize_img = tmp_img.resize(( w, h ), Image.Resampling.LANCZOS )
        # Resampling.LANCZOS  Image.ANTIALIAS
        self.final_image = ImageTk.PhotoImage( resize_img )
        left = tkinter.Label( self.root, image = self.final_image )
        left.place( x = 90, y = 130, width = 400, height = 550 )
        
    def setup_frames( self ):
        self.frm_register = tkinter.Frame( self.root )
        self.frm_register.place( x = 490, y = 130, width = 850, height = 550 )
        self.lbl_title = tkinter.Label( self.frm_register,
                                        font = self.test_font,
                                        foreground = 'green',
                                        text = 'REGISTER HERE' )
        self.lbl_title.place( x = 50, y = 30 )
        
        self.lbl_fname = tkinter.Label( self.frm_register,
                                        font = self.lbl_font,
                                        foreground = 'grey',
                                        text = 'First Name:' )
        self.lbl_fname.place( x = 50, y = 90 )
        
        self.ent_fname = tkinter.Entry( self.frm_register,
                                        font = self.ent_font,
                                        borderwidth = 6,
                                        width = 21,
                                        relief = tkinter.RIDGE,
                                        textvariable = self.var_fname,
                                        background = 'PaleTurquoise3',
                                        foreground = 'blue' )
        self.ent_fname.place( x = 50, y = 130 )
        self.ent_fname.focus()
        
        self.lbl_lname = tkinter.Label( self.frm_register,
                                        font = self.lbl_font,
                                        foreground = 'grey',
                                        text = 'Last Name:' )
        self.lbl_lname.place( x = 400, y = 90 )
        
        self.ent_lname = tkinter.Entry( self.frm_register,
                                        font = self.ent_font,
                                        borderwidth = 6,
                                        width = 21,
                                        relief = tkinter.RIDGE,
                                        textvariable = self.var_lname,
                                        background = 'PaleTurquoise3',
                                        foreground = 'blue' )
        self.ent_lname.place( x = 400, y = 127 )
        
        self.lbl_contact = tkinter.Label( self.frm_register,
                                          font = self.lbl_font,
                                          foreground = 'grey',
                                          text = 'Contact Number:' )
        self.lbl_contact.place( x = 50, y = 190 )
        
        self.ent_contact = tkinter.Entry( self.frm_register,
                                          font = self.ent_font,
                                          borderwidth = 6,
                                          width = 21,
                                          relief = tkinter.RIDGE,
                                          textvariable = self.var_contact,
                                          background = 'PaleTurquoise3',
                                          foreground = 'blue' )
        self.ent_contact.place( x = 50, y = 230 )
        
        self.lbl_email = tkinter.Label( self.frm_register,
                                          font = self.lbl_font,
                                          foreground = 'grey',
                                          text = 'Email Address:' )
        self.lbl_email.place( x = 400, y = 190 )
        
        self.ent_email = tkinter.Entry( self.frm_register,
                                        font = self.ent_font,
                                        borderwidth = 6,
                                        width = 21,
                                        relief = tkinter.RIDGE,
                                        textvariable = self.var_email,
                                        background = 'PaleTurquoise3',
                                        foreground = 'blue' )
        self.ent_email.place( x = 400, y = 230 )
        
        self.lbl_security = tkinter.Label( self.frm_register,
                                           font = self.lbl_font,
                                           foreground = 'grey',
                                           text = 'Security Question:' )
        self.lbl_security.place( x = 50, y = 290 )
        
        self.cbx_security = ttk.Combobox( self.frm_register,
                                          state = 'readonly',
                                          font = self.ent_font,
                                          width = 21,
                                          textvariable = self.var_security )
                                          
        self.cbx_security.place( x = 50, y = 330 )
        self.cbx_security['values'] = ( '',
                                        'First Pet Name',
                                        'Place Of Birth',
                                        'Name Of Best Friend',
                                        'Life, The Universe, Everything' )
        style = ttk.Style()
        style.configure( 'TCombobox',
                         fieldbackground = 'PaleTurquoise3',
                         selectbackground = 'PaleTurquoise3',
                         selectforeground = 'blue',
                         background = 'PaleTurquoise3',
                         foreground = 'blue' )
        
        self.lbl_answer = tkinter.Label( self.frm_register,
                                         font = self.lbl_font,
                                         foreground = 'grey',
                                         text = 'Security Answer:' )
        self.lbl_answer.place( x = 400, y = 285 )
        
        self.ent_answer = tkinter.Entry( self.frm_register,
                                         font = self.ent_font,
                                         borderwidth = 6,
                                         width = 21,
                                         relief = tkinter.RIDGE,
                                         textvariable = self.var_answer,
                                         background = 'PaleTurquoise3',
                                         foreground = 'blue' )
        self.ent_answer.place( x = 400, y = 323 )
        
        self.lbl_password = tkinter.Label( self.frm_register,
                                           font = self.lbl_font,
                                           foreground = 'grey',
                                           text = 'Enter Password:' )
        self.lbl_password.place( x = 50, y = 380 )
        
        self.ent_password = tkinter.Entry( self.frm_register,
                                           show = '*',
                                           font = self.ent_font,
                                           borderwidth = 6,
                                           width = 21,
                                           relief = tkinter.RIDGE,
                                           textvariable = self.var_password,
                                           background = 'PaleTurquoise3',
                                           foreground = 'blue' )
        self.ent_password.place( x = 50, y = 420 )
        
        self.lbl_confirm = tkinter.Label( self.frm_register,
                                          font = self.lbl_font,
                                          foreground = 'grey',
                                          text = 'Confirm Password:' )
        self.lbl_confirm.place( x = 400, y = 380 )
        
        self.ent_confirm = tkinter.Entry( self.frm_register,
                                          show = '*',
                                          font = self.ent_font,
                                          borderwidth = 6,
                                          width = 21,
                                          relief = tkinter.RIDGE,
                                          textvariable = self.var_confirm,
                                          background = 'PaleTurquoise3',
                                          foreground = 'blue' )
        self.ent_confirm.place( x = 400, y = 420 )
        
        w = int( 270 )
        h = int( 48 )
        tmp_img = Image.open( self.reg_btn_image )
        resize_img = tmp_img.resize(( w, h ), Image.Resampling.LANCZOS )
        self.btn_img =  ImageTk.PhotoImage( resize_img  )
        
        self.btn_register = tkinter.Button( self.frm_register,
                                            font = self.btn_font,
                                            borderwidth = 6,
                                            #width = 51,
                                            background = 'PaleTurquoise3',
                                            foreground = 'green',
                                            activebackground = 'yellow',
                                            relief = tkinter.RAISED,
                                            cursor = 'hand2',
                                            image = self.btn_img,
                                            #text = 'Register Now',
                                            command = self.register_now_callback )
        self.btn_register.place( x = 195, y = 473 )
        
        
        w = int( 200 )
        h = int( 88 )
        tmp_img = Image.open( self.login_btn_image )
        resize_img = tmp_img.resize(( w, h ), Image.Resampling.LANCZOS )
        self.btn_login_img =  ImageTk.PhotoImage( resize_img  )
        
        self.btn_login = tkinter.Button( self.root,
                                         font = self.btn_font,
                                         borderwidth = 6,
                                         #background = 'PaleTurquoise3',
                                         background = 'Black',
                                         foreground = 'green',
                                         activebackground = 'yellow',
                                         relief = tkinter.RAISED,
                                         cursor = 'hand2',
                                         image = self.btn_login_img,
                                         #text = 'Register Now',
                                         command = self.login_now_callback )
        self.btn_login.place( x = 168, y = 560 )
                                         
        
        
    def register_now_callback( self ):
        if self.var_fname.get() == '' or self.var_lname.get() == '':
            messagebox.showerror( 'Error',
                                  'All Fields Are Required',
                                  parent = self.root )

        #print( 'Register Button Clicked' )
        print( self.var_fname.get())
        print( self.var_lname.get())
        print( self.var_contact.get())
        print( self.var_email.get())
        print( self.var_security.get())
        print( self.var_answer.get())
        print( self.var_password.get())
        print( self.var_confirm.get())
        
    def login_now_callback( self ):
        messagebox.showinfo( 'Information',
                             'You have successfully pressed the Login Button!',
                             parent = self.root )
    
        

if __name__ == '__main__':
    root = tkinter.Tk()
    app = Register( root )
    root.mainloop()
