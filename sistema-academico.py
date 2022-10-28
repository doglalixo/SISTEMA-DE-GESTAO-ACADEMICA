# IMPORTAÇÃO DE BIBLIOTECAS
from bibliotecas import *
from criardb import *

# CRIAÇÃO TELA DE LOGIN 
def telalogin(): 
    root = Tk() 
    root.title('Tela de login') 
    root.geometry('900x600') 
    root.configure(background="#F5F5F5")
    root.resizable(width=FALSE, height=FALSE) 
    style = ttk.Style(root)
    style.theme_use("clam")
    
    # CRIAÇÃO DO FRAME PARA REALIZAR O LOGIN 
    frame_login = Frame(root, background='#DCDCDC', highlightthickness=3, highlightbackground='black',relief=GROOVE)
    frame_login.place(relx=0.33, rely=0.15, relheight=0.60, relwidth=0.40) 

    # CRIAÇÃO DOS LABEL's, ENTRYS, BOTÕES E IMAGENS:

    #IMAGENS
    img_usuario = Image.open('icones/usuariopng.png')
    img_usuario = img_usuario.resize ((20,20))
    img_usuario = ImageTk.PhotoImage(img_usuario)

    img_senha = Image.open('icones/chave.png')
    img_senha = img_senha.resize ((25,20))
    img_senha = ImageTk.PhotoImage(img_senha)

    img_login = Image.open('icones/imglogin.png')
    img_login = img_login.resize ((270,200))
    img_login = ImageTk.PhotoImage(img_login)

    img_entrar = Image.open('icones/loginpng.png')
    img_entrar = img_entrar.resize ((30,30))
    img_entrar = ImageTk.PhotoImage(img_entrar)

    img_cadastrar = Image.open('icones/cadastrar.png')
    img_cadastrar = img_cadastrar.resize ((15,15))
    img_cadastrar = ImageTk.PhotoImage(img_cadastrar)

    #LABEL's
    l_usuario = Label (frame_login, text="USUÁRIO: ", height=1, anchor=NW, font=('Ivy 8 bold'), bg='#DCDCDC', fg='#000000' )
    l_usuario.place(x=104, y=93)
    l_imgusuario = Label(frame_login, bg='#DCDCDC', image=img_usuario)
    l_imgusuario.place(x=72, y=106)

    l_senha = Label (frame_login, text="SENHA: ", height=1, anchor=NW, font=('Ivy 8 bold'), bg='#DCDCDC', fg='#000000' )
    l_senha.place(x=104, y=133)
    l_imgsenha = Label(frame_login, bg='#DCDCDC', image=img_senha)
    l_imgsenha.place(x=71, y=146)

    l_login = Label(frame_login, image=img_login, compound=RIGHT, anchor=CENTER,
                     font=('ivy 17 bold'), bg='#2E8B57', relief=GROOVE)
    l_login.place(relwidth=1, relheight=0.1)

    l_txt = Label(frame_login, anchor=CENTER, font=('ivy 9 bold'), bg='#DCDCDC', text='Não tem um usuário?', fg='#000000')
    l_txt.place(relx=0.32, rely=0.74)
    linha = Label(frame_login, bg='#000000')
    linha.place(relx=0.00, rely=0.09, relheight=0.01, relwidth=1)

    #ENTRYS
    e_usuario = Entry(frame_login)
    e_usuario.place(x=104, y=109, relwidth=0.4)

    e_senha = Entry(frame_login)
    e_senha.place(x=104, y=148, relwidth=0.4)

    #BOTÕES
    borda_ent = LabelFrame(frame_login, bd = 2, bg = "black")
    borda_ent.pack(pady = 10)
    borda_ent.place(relx=0.37, rely=0.51)
    b_login = Button(borda_ent, borderwidth=0, text='ENTRAR', font=('Ivy 9 bold'), image=img_entrar, bg='#2E8B57', fg='#000000',
                    compound=RIGHT, width=80, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_login.pack()

    borda_cdst = LabelFrame(frame_login, bd = 2, bg = "black")
    borda_cdst.pack(pady = 10)
    borda_cdst.place(relx=0.34, rely=0.8)
    b_cadastrar = Button(borda_cdst, borderwidth=0, text='CADASTRAR-SE', font=('Ivy 9 bold'), image=img_cadastrar, bg='#2E8B57', fg='#000000',
                    compound=RIGHT, width=102, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_cadastrar.pack()

    root.mainloop()
telalogin()