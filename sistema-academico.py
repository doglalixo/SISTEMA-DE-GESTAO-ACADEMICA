# IMPORTAÇÃO DE BIBLIOTECAS
from cProfile import label
import cProfile
from email import message
from logging import root

from setuptools import Command
from bibliotecas import *
from criardb import *
#CRIAÇÃO TELA DE CADASTRO
def telalogin(): 
    root = Tk() 
    root.title('Tela de login') 
    root.geometry('900x600') 
    root.configure(background="#F5F5F5")
    root.resizable(width=FALSE, height=FALSE) 
    style = ttk.Style(root)
    style.theme_use("clam")

    #Funções
    def botaoajuda():
        messagebox.showinfo('Ajuda', """PARA REALIZAR LOGIN: Preencha os campos de usuário e senha, em seguida, clique no botão "Entrar" para realizar login.


PARA REALIZAR CADASTRO: Clicar em "Cadastrar-se". """)

    def botaocadastrar():
        root.destroy()
        telacadastro()
        pass
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

    img_ajuda = Image.open('icones/ajuda.png')
    img_ajuda = img_ajuda.resize ((25,25))
    img_ajuda = ImageTk.PhotoImage(img_ajuda)

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

    l_txt = Label(frame_login, anchor=CENTER, bg='#DCDCDC', text='Não tem um usuário?', fg='#000000')
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
    b_login = Button(borda_ent, borderwidth=0.5, text='ENTRAR', font=('Ivy 9 bold'), image=img_entrar, bg='#2E8B57', fg='#000000',
                    compound=RIGHT, width=80, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_login.pack()

    borda_cdst = LabelFrame(frame_login, bd = 2, bg = "black")
    borda_cdst.pack(pady = 10)
    borda_cdst.place(relx=0.34, rely=0.8)
    b_cadastrar = Button(borda_cdst, borderwidth=0.5, text='CADASTRAR-SE', font=('Ivy 9 bold'), image=img_cadastrar, bg='#2E8B57', fg='#000000',command=botaocadastrar,
                    compound=RIGHT, width=102, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_cadastrar.pack()
    b_ajuda = Button(frame_login, borderwidth=0, font=('Ivy 9 bold'), image=img_ajuda, bg='#DCDCDC', fg='#000000', command=botaoajuda,
                    compound=RIGHT, width=40, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_ajuda.pack()
    b_ajuda.place(relx=0.87, rely=0.15)

    root.mainloop()
#CRIAÇÃO DA TELA DE CADASTRO 
def telacadastro(): 
    #Criação da janela
    cadastro = Tk() 
    cadastro.title('Tela de cadastro') 
    cadastro.geometry('900x600') 
    cadastro.configure(background="#F5F5F5") 
    cadastro.resizable(width=FALSE, height=FALSE) 
    style = ttk.Style(cadastro) 
    style.theme_use("clam")

    #Funções
    def botaoajudar():
        messagebox.showinfo('Ajuda', """Para criar um usuário novo, preencha todos os campos e clique em "Finalizado". 
        
Caso já tenha um, clique em "Entrar". """)
    def botaologin():
        cadastro.destroy()
        telalogin()
    #Criação do frame principal
    frame_cadastro = Frame(cadastro, background='#DCDCDC', highlightthickness=3, highlightbackground='black',relief=GROOVE)
    frame_cadastro.place(relx=0.33, rely=0.10, relheight=0.80, relwidth=0.40)

    #Imagens
    img_cadastrar = Image.open('icones/cadastro.png')
    img_cadastrar = img_cadastrar.resize ((30,30))
    img_cadastrar = ImageTk.PhotoImage(img_cadastrar)

    img_usuario = Image.open('icones/usuariopng.png')
    img_usuario = img_usuario.resize ((25,25))
    img_usuario = ImageTk.PhotoImage(img_usuario)

    img_cpf = Image.open('icones/cpf.png')
    img_cpf = img_cpf.resize ((25,25))
    img_cpf = ImageTk.PhotoImage(img_cpf)

    img_calendario = Image.open('icones/calendario.png')
    img_calendario = img_calendario.resize ((25,25))
    img_calendario = ImageTk.PhotoImage(img_calendario)

    img_user = Image.open('icones/matricula.png')
    img_user = img_user.resize ((25,25))
    img_user = ImageTk.PhotoImage(img_user)

    img_check = Image.open('icones/check.png')
    img_check = img_check.resize ((20,20))
    img_check = ImageTk.PhotoImage(img_check)

    img_entrar = Image.open('icones/loginpng.png')
    img_entrar = img_entrar.resize ((30,30))
    img_entrar = ImageTk.PhotoImage(img_entrar)

    img_ajuda = Image.open('icones/ajuda.png')
    img_ajuda = img_ajuda.resize ((25,25))
    img_ajuda = ImageTk.PhotoImage(img_ajuda)

    #Criação do título
    titulo_cadastro = Label(frame_cadastro, image=img_cadastrar, compound=RIGHT, anchor=CENTER, text='CADASTRO ',
                     font=('ivy 17 bold'), bg='#2E8B57', relief=GROOVE)
    titulo_cadastro.place(relwidth=1, relheight=0.1)
    linha_cadastro = Label(frame_cadastro, bg='#000000')
    linha_cadastro.place(relx=0.00, rely=0.09, relheight=0.01, relwidth=1)

    #Labels

    l_imgusuario = Label(frame_cadastro, bg='#DCDCDC', image=img_usuario)
    l_imgusuario.place(relx=0.07, rely=0.23)

    l_imgcpf = Label(frame_cadastro, bg='#DCDCDC', image=img_cpf)
    l_imgcpf.place(relx=0.07, rely=0.33)

    l_imgcalendario = Label(frame_cadastro, bg='#DCDCDC', image=img_calendario)
    l_imgcalendario.place(relx=0.07, rely=0.43)

    l_imguser = Label(frame_cadastro, bg='#DCDCDC', image=img_user)
    l_imguser.place(relx=0.07, rely=0.53)

    l_user = Label (frame_cadastro, text="USUÁRIO: ", height=1, anchor=NW, font=('Ivy 9 bold'), bg='#DCDCDC', fg='#000000' )
    l_user.place(relx=0.15, rely=0.5)

    l_nome = Label (frame_cadastro, text="NOME: ", height=1, anchor=NW, font=('Ivy 9 bold'), bg='#DCDCDC', fg='#000000' )
    l_nome.place(relx=0.15, rely=0.2)

    l_cpf = Label (frame_cadastro, text="CPF: ", height=1, anchor=NW, font=('Ivy 9 bold'), bg='#DCDCDC', fg='#000000' )
    l_cpf.place(relx=0.15, rely=0.3)

    l_cal = Label (frame_cadastro, text="DATA DE NASCIMENTO: ", height=1, anchor=NW, font=('Ivy 9 bold'), bg='#DCDCDC', fg='#000000' )
    l_cal.place(relx=0.15, rely=0.4)

    l_txt = Label(frame_cadastro, anchor=CENTER, bg='#DCDCDC', text='Já tem um usuário?', fg='#000000')
    l_txt.place(relx=0.35, rely=0.79)

    #Entrys
    e_cal = DateEntry (frame_cadastro, width=12, background='#2E8B57', foreground='white', borderwidth=2, year=2022)
    e_cal.place(relx=0.17, rely=0.44)

    e_cpf = Entry (frame_cadastro, width=30)
    e_cpf.place(relx=0.17, rely=0.34)

    e_nome = Entry (frame_cadastro, width=30)
    e_nome.place(relx=0.17, rely=0.24)

    e_user = Entry (frame_cadastro, width=30)
    e_user.place(relx=0.17, rely=0.54)

    #Botões
    borda_cdstr = LabelFrame(frame_cadastro, bd = 2, bg = "black")
    borda_cdstr.pack(pady = 10)
    borda_cdstr.place(relx=0.35, rely=0.65)
    b_cadastro = Button(borda_cdstr, borderwidth=0.5, text='FINALIZADO!', font=('Ivy 9 bold'), image=img_check, bg='#2E8B57', fg='#000000',command=botaocadastrar,
                    compound=RIGHT, width=102, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_cadastro.pack()

    borda_ent = LabelFrame(frame_cadastro, bd = 2, bg = "black")
    borda_ent.pack(pady = 10)
    borda_ent.place(relx=0.37, rely=0.83)
    b_login = Button(borda_ent, borderwidth=0.5, text='ENTRAR', font=('Ivy 9 bold'), image=img_entrar, command=botaologin, bg='#2E8B57', fg='#000000',
                    compound=RIGHT, width=80, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_login.pack()

    b_ajuda = Button(frame_cadastro, borderwidth=0, font=('Ivy 9 bold'), image=img_ajuda, bg='#DCDCDC', fg='#000000', command=botaoajudar,
                    compound=RIGHT, width=40, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_ajuda.pack()
    b_ajuda.place(relx=0.87, rely=0.15)
    cadastro.mainloop()
def botaocadastrar():
    telacadastro()
# CRIAÇÃO TELA DE LOGIN
root = Tk() 
root.title('Tela de login') 
root.geometry('900x600') 
root.configure(background="#F5F5F5")
root.resizable(width=FALSE, height=FALSE) 
style = ttk.Style(root)
style.theme_use("clam")

#Funções
def botaoajuda():
    messagebox.showinfo('Ajuda', """PARA REALIZAR LOGIN: Preencha os campos de usuário e senha, em seguida, clique no botão "Entrar" para realizar login.


PARA REALIZAR CADASTRO: Clicar em "Cadastrar-se". """)

def botaocadastrar():
    root.destroy()
    telacadastro()
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

img_ajuda = Image.open('icones/ajuda.png')
img_ajuda = img_ajuda.resize ((25,25))
img_ajuda = ImageTk.PhotoImage(img_ajuda)

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

l_txt = Label(frame_login, anchor=CENTER, bg='#DCDCDC', text='Não tem um usuário?', fg='#000000')
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
b_login = Button(borda_ent, borderwidth=0.5, text='ENTRAR', font=('Ivy 9 bold'), image=img_entrar, bg='#2E8B57', fg='#000000',
                    compound=RIGHT, width=80, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
b_login.pack()

borda_cdst = LabelFrame(frame_login, bd = 2, bg = "black")
borda_cdst.pack(pady = 10)
borda_cdst.place(relx=0.34, rely=0.8)
b_cadastrar = Button(borda_cdst, borderwidth=0.5, text='CADASTRAR-SE', font=('Ivy 9 bold'), image=img_cadastrar, bg='#2E8B57', fg='#000000',command=botaocadastrar,
                    compound=RIGHT, width=102, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
b_cadastrar.pack()
b_ajuda = Button(frame_login, borderwidth=0, font=('Ivy 9 bold'), image=img_ajuda, bg='#DCDCDC', fg='#000000', command=botaoajuda,
                compound=RIGHT, width=40, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
b_ajuda.pack()
b_ajuda.place(relx=0.87, rely=0.15)

root.mainloop()