# IMPORTAÇÃO DE BIBLIOTECAS
from ast import Try
from cProfile import label
import cProfile
from cgitb import text
from email import message
from logging import root
from setuptools import Command
from bibliotecas import *
import keyboard

# CIRAÇÃO DA TELA DE GERENCIAMENTO DE DADOS DOS ALUNOS
def tela_alunos():
    co0 = "#2e2d2b"
    co1 = "#feffff"

    from tkinter import Menu
    global tree
    global imagem, imagem_string, l_imagem

    # CRIAÇÃO DA TELA DE ALUNOS
    root = Tk()
    root.title('SDGA - Sistema De Gestão Acadêmica')
    root.state('zoomed')
    root.iconbitmap('icones/livro.ico')
    menubar = Menu(root)
    root.config(menu=menubar)
    root.geometry('900x600') 
    root.configure(background="#DCDCDC")

# CRIAÇÃO DA CLASSE E FUNÇÕES QUE SERVIRÃO PARA IMPRIMIR OS DADOS DO ALUNO
    class Relatorios():
        def __init__(self,lista_campos,lista_rotulos):
            self.matricula = e_mtr.get()
            self.nome = e_nome.get()
            self.cpf = e_cpf.get()
            self.serie = e_serie.get()
            self.turno = e_turno.get()
            self.c = canvas.Canvas('Dados de' + str(e_mtr.get()) + '.pdf')
            self.c.setFont("Helvetica-Bold", 24)
            self.c.drawString(140, 780, 'Cadastro do aluno: ' + e_nome.get())
            self.c.setFont("Helvetica-Bold", 18)
            self.c.drawString(50, 700, 'Matrícula: ' + self.matricula)
            self.c.drawString(50, 670, 'Nome.....: ' + self.nome)
            self.c.drawString(50, 630, 'CPF......: ' + self.cpf)
            self.c.drawString(50, 600, 'Série....: ' + self.serie)
            self.c.drawString(50, 570, 'Turno....: ' + self.turno)
            self.c.showPage()
            self.c.save()
            self.printAlunos()
        def printAlunos(self):
            webbrowser.open('Dados de'+ str(e_mtr.get()) +'.pdf')
        def geraRelatorioAlunos(self):
            self.c.canvas.Canvas('Dados de'+ str(e_mtr.get()) +'.pdf')

    # FUNÇÃO QUE LIMPA TODOS OS DADOS DA TELA
    def limpa():
        TrvLista_aluno.delete(*TrvLista_aluno.get_children())
        e_mtr.delete(0,END)
        e_nome.delete(0, END)
        e_cpf.delete(0, END)
        e_turno.delete(0, END)
        e_serie.delete(0, END)
    # FUNÇÃO QUE CHAMA A CLASSE E FUNÇÕES ACIMA PARA CONCLUIR A IMPRESSÃO DOS DADOS
    def imprimir():
        if str(e_mtr.get) == '' or str(e_nome.get()) == '' or str(e_cpf.get()) == '' or str(e_serie.get()) == '' or str(e_turno.get()) == '':
            messagebox.showerror('', 'Preencha os campos corretamente.')
        else:
            cmp_valores = (e_mtr.get(),e_nome.get(),e_cpf.get(),e_serie.get(),e_turno.get())
            lst_NomesCampos = ['MATRICULA', 'NOME', 'CPF', 'SERIE', 'TURNO']
            rRelatorio = Relatorios(cmp_valores,lst_NomesCampos)
    # FUNÇÃO QUE CRIA NOVAMENTE A TELA DE LOGIN
    def telalogin2(): 
        root.destroy()
        root1 = Tk()
        root1.title('SDGA - Sistema De Gestão Acadêmica') 
        root1.iconbitmap('icones/livro.ico')
        root1.geometry('900x600') 
        root1.configure(background="#F5F5F5")
        root1.resizable(width=FALSE, height=FALSE) 
 
        # FUNÇÃO DO BOTÃO QUE CHAMA A CRIAÇÃO DA TELA DE CADASTRO
        def botaocadastrar():
            root1.destroy()
            telacadastro()
            pass
        # CRIAÇÃO DO FRAME PARA REALIZAR O LOGIN 
        frame_login = Frame(root1, background='#DCDCDC', highlightthickness=3, highlightbackground='gray',relief=GROOVE)
        frame_login.place(relx=0.33, rely=0.15, relheight=0.60, relwidth=0.40) 

        # IMAGENS
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


        # LABEL's
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

        # ENTRYS
        usuariostring = StringVar()
        e_usuario = Entry(frame_login, textvariable=usuariostring)
        e_usuario.place(x=104, y=109, relwidth=0.4)

        senhastring = StringVar()
        e_senha = Entry(frame_login, textvariable=senhastring)
        e_senha.place(x=104, y=148, relwidth=0.4)

        # Função para testar se se o usuario e senha sao validos e se for, realizar o login
        def botaoentrar():
                try:
                    import sqlite3 as lite
                    con = lite.connect('db.sistema-academico.db')
                    with con:
                        cur = con.cursor()
                        cur.execute("SELECT * FROM CADASTRO_USUARIO WHERE USUARIO = " + str(e_usuario.get()))
                        consulta = cur.fetchall()[0]
                except IndexError:
                    messagebox.showerror('', 'Usuário ou senha inválido, cheque todos os carácteres.')
                    e_usuario.delete(0, END)
                    e_senha.delete(0, END)
                except lite.OperationalError:
                    messagebox.showerror('', 'Preencha todos os campos.')
                    e_usuario.delete(0, END)
                    e_senha.delete(0, END)

                else:
                    user_senha = []
                    for i in consulta:
                        user_senha.append(i)
                    if str(user_senha[1]) != str(e_senha.get()):
                        messagebox.showerror('', 'Senha incorreta .')
                        e_senha.delete(0, END)
                    else:
                        root1.destroy()
                        tela_alunos()

        # BOTÕES
        borda_ent = LabelFrame(frame_login, bd = 2, bg = "black")
        borda_ent.pack(pady = 10)
        borda_ent.place(relx=0.37, rely=0.51)
        b_login = Button(borda_ent, borderwidth=0.5, text='ENTRAR', font=('Ivy 9 bold'), image=img_entrar, bg='#2E8B57', fg='#000000',
                        compound=RIGHT, width=80, overrelief=RIDGE, relief=GROOVE, anchor=CENTER, command=botaoentrar)
        b_login.pack()

        borda_cdst = LabelFrame(frame_login, bd = 2, bg = "black")
        borda_cdst.pack(pady = 10)
        borda_cdst.place(relx=0.34, rely=0.8)
        b_cadastrar = Button(borda_cdst, borderwidth=0.5, text='CADASTRAR-SE', font=('Ivy 9 bold'), image=img_cadastrar, bg='#2E8B57', fg='#000000',command=botaocadastrar,
                        compound=RIGHT, width=102, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
        b_cadastrar.pack()
        root1.mainloop()

    # FUNÇÃO QUE ATUALIZA OS DADOS DO ALUNO    
    def atualizar():
        int_atualizar = messagebox.askquestion("",
                           "Você deseja ATUALIZAR?")
        if int_atualizar == 'yes':
            try: 
                import sqlite3 as lite
                con = lite.connect('db.sistema-academico.db')
                with con:
                    cur = con.cursor()
                    cur.execute('SELECT * FROM CADASTRO_ALUNO WHERE MATRICULA =' + str(e_mtr.get()))
                    consulta_atualizar = cur.fetchall()[0]
            except IndexError:
                messagebox.showerror('', 'Matrícula não encontrada')

            except lite.OperationalError:
                messagebox.showerror('', 'Matrícula não encontrada')
            else:
                try: 
                    import sqlite3 as lite
                    con = lite.connect('db.sistema-academico.db')
                    with con:
                        cur = con.cursor()
                        cur.execute('UPDATE CADASTRO_ALUNO SET NOME =' + '"' + str(e_nome.get()) +'"' + ', CPF =' + str(e_cpf.get()) + ', SERIE =' + '"' + str(e_serie.get()) + '"' + ', TURNO =' + '"' + str(e_turno.get()) +'"' + ' WHERE MATRICULA =' + str(e_mtr.get()))
                except lite.OperationalError:
                    messagebox.showerror('', 'Preencha os campos corretamente')
                else:
                        con.commit()
                        messagebox.showinfo('SUCESSO!', 'Dados atualizados')
                        e_mtr.delete(0, END)
                        e_nome.delete(0, END)
                        e_cpf.delete(0, END)
                        e_serie.delete(0, END)
                        e_turno.delete(0, END)
                        visualiza()
    # FUNÇÃO QUE INSERE OS DADOS DE UM ALUNO AO SISTEMA
    def incluir():
        int_incluir = messagebox.askquestion("",
                           "Você deseja INCLUIR?")
        if int_incluir == 'yes':
                try: 
                    import sqlite3 as lite
                    con = lite.connect('db.sistema-academico.db')
                    with con:
                        mtr = e_mtr.get()
                        nom = e_nome.get()
                        cpf = e_cpf.get()
                        ser = e_serie.get()
                        tur = e_turno.get()
                        cur = con.cursor()
                        #INSERT INTO CADASTRO_ALUNO (MATRICULA, NOME, CPF, SERIE, TURNO) VALUES( 1, 'douglas', 12345678910, '1b', 'mat');
                        cur.execute('INSERT INTO CADASTRO_ALUNO (MATRICULA, NOME, CPF, SERIE, TURNO) values(' + str(mtr) + ',' + '"' + str(nom) + '" ,' + str(cpf) + ',' + '"' + str(ser) + '" ,' + '"' + str(tur) + '")' )
                except lite.OperationalError:
                        messagebox.showerror('', 'Preencha os campos corretamente.')
                except lite.IntegrityError:
                        messagebox.showerror('', 'Matrícula em uso, tente outra.')
                        e_mtr.delete(0, END)
                else:
                        con.commit()
                        messagebox.showinfo('SUCESSO!', 'Dados inseridos.')
                        e_nome.delete(0, END)
                        visualiza()
    # FUNÇÃO PARA BUSCAR OS DADOS DE UM ALUNO (PODE USAR QUALQUER CAMPO PARA PESQUISAR)
    def buscar():
        import sqlite3
        conn = sqlite3.connect("db.sistema-academico.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM CADASTRO_ALUNO WHERE NOME LIKE '" + str(e_buscar.get()) + "%' " + "OR MATRICULA LIKE '" + str(e_buscar.get()) + "%' OR CPF LIKE '" + str(e_buscar.get()) + "%' OR SERIE LIKE '" + str(e_buscar.get()) +"%' OR TURNO LIKE '" + str(e_buscar.get()) + "%'" )
        visualiza_buscar()
        e_buscar.delete(0, END)
        conn.close()

    # FUNÇÃO QUE MOSTRA NA TELA DE DADOS OS DADOS CORRESPONDENTE À PESQUISA
    def visualiza_buscar():
        TrvLista_aluno.delete(*TrvLista_aluno.get_children())
        linhas = seleciona_buscar()
        for dados in linhas:
           TrvLista_aluno.insert("", END, values=dados)

    # FUNÇÃO QUE ADICIONA À LISTA DE DADOS OS DADOS CORRESPONDENTE À PESQUISA
    def seleciona_buscar():
        import sqlite3
        conn = sqlite3.connect("db.sistema-academico.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM CADASTRO_ALUNO WHERE NOME LIKE '" + str(e_buscar.get()) + "%' " + "OR MATRICULA LIKE '" + str(e_buscar.get()) + "%' OR CPF LIKE '" + str(e_buscar.get()) + "%' OR SERIE LIKE '" + str(e_buscar.get()) +"%' OR TURNO LIKE '" + str(e_buscar.get()) + "%'" )
        linhas_buscar = cur.fetchall()
        conn.close()
        return linhas_buscar
        for dados in linhas_buscar:
            TrvLista_aluno.insert("", END, values=dados)

    # FUNÇÃO RESPONSÁVEL POR MOSTRAR TODOS OS DADOS DO BANCO NA LISTA DE DADOS
    def visualiza():
        TrvLista_aluno.delete(*TrvLista_aluno.get_children())
        linhas = seleciona()
        for dados in linhas:
           TrvLista_aluno.insert("", END, values=dados)

    # FUNÇÃO RESPONSÁVEL POR ADICIONAR TODOS OS DADOS DO BANCO À LISTA DE DADOS
    def seleciona():
        import sqlite3
        conn = sqlite3.connect("db.sistema-academico.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM CADASTRO_ALUNO ORDER BY SERIE")
        linhas = cur.fetchall()
        conn.close()
        return linhas
    # FUNÇÃO QUE DELETA TODOS OS DADOS DE UM ALUNO
    def excluir():
        int_excluir = messagebox.askquestion("",
                           "Você deseja EXCLUIR?")
        if int_excluir == 'yes':
            try: 
                import sqlite3 as lite
                con = lite.connect('db.sistema-academico.db')
                with con:
                    cur = con.cursor()
                    cur.execute('SELECT * FROM CADASTRO_ALUNO WHERE MATRICULA =' + str(e_mtr.get()))
                    consulta_excluir = cur.fetchall()[0][0]
            except IndexError:
                messagebox.showerror('', 'Matrícula não encontrada')

            except lite.OperationalError:
                messagebox.showerror('', 'Matrícula não encontrada')
            else:
                try: 
                    import sqlite3 as lite
                    con = lite.connect('db.sistema-academico.db')
                    with con:
                        mtr = e_mtr.get()
                        cur = con.cursor()
                        cur.execute('DELETE FROM CADASTRO_ALUNO WHERE MATRICULA =' + str(mtr))
                except lite.OperationalError:
                        messagebox.showerror('', 'Preencha o campo "Matrícula" corretamente')
                except IndexError:
                        messagebox.showerror('', 'Preencha o campo "Matrícula" corretamente')
                else:
                        con.commit()
                        messagebox.showinfo('SUCESSO!', 'Dados excluídos')
                        e_mtr.delete(0, END)
                        e_nome.delete(0, END)
                        e_cpf.delete(0, END)
                        e_serie.delete(0, END)
                        e_turno.delete(0, END)
                        visualiza()
    # CRIAÇÃO DO FRAME QUE FICARÁ A LISTA DE DADOS DO BANCO
    frm_lista_aluno = Frame(root, bg='#DFE3EE', highlightbackground='#000000', highlightthickness=2)
    frm_lista_aluno.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.5)

    # VARIÁVEIS QUE SERÃO UTILIZADAS PARA CONFECCIONAR O TREEVIEW
    colunas = ('col0', 'col1', 'col2', 'col3', 'col4', 'col5')
    cabecalho = ('', 'MATRÍCULA', 'NOME', 'CPF', 'SÉRIE', 'TURNO')
    largura = (0, 100, 100, 10, 10, 10)

    # FUNÇÃO PARA QUE SEJA POSSÍVEL O PREENCHIMENTO DOS CAMPOS DE ENTRADA COM APENAS DOIS QLIQUES EM CIMA DA TELA DE DADOS
    def duplo_clique(event):
        e_mtr.delete(0,END)
        e_nome.delete(0, END)
        e_cpf.delete(0, END)
        e_serie.delete(0, END)
        e_turno.delete(0, END)
        c_mtr = ''
        c_nome = ''
        c_cpf = ''
        c_serie = ''        
        c_turno = ''
        TrvLista_aluno.selection()
        for i in TrvLista_aluno.selection():
            c_mtr, c_nome, c_cpf, c_serie, c_turno = TrvLista_aluno.item(i,'values')
        e_mtr.insert(END,c_mtr)
        e_nome.insert(END,c_nome)
        e_cpf.insert(END,c_cpf)
        e_turno.insert(END,c_turno)
        e_serie.insert(END,c_serie)

    # CRIAÇÃO DO TREEVIEW, ONDE FICARÁ VISUALMENTE OS DADOS DO BANCO
    TrvLista_aluno = ttk.Treeview(frm_lista_aluno, height=3, column=colunas, selectmode="extended")
    TrvLista_aluno.bind("<Double-1>", duplo_clique)
    TrvLista_aluno.place(relx=0, rely=0.25, relwidth=0.99, relheight=0.75)
    scr_lstaluno = Scrollbar(frm_lista_aluno, orient='vertical', command=TrvLista_aluno.yview)
    scr_lstaluno.place(relx=0.98, rely=0.25, relwidth=0.02, relheight=0.75)
    TrvLista_aluno.configure(yscroll=scr_lstaluno.set)
    conta = 0
    # REPETIÇÃO FEITA PARA O PREENCHIMENTO DO CABEÇALHO E COLUNAS
    for i in colunas:
        coluna = "#" + str(conta)
        TrvLista_aluno.heading(coluna, text=cabecalho[conta], anchor=CENTER)
        TrvLista_aluno.column(coluna, width=largura[conta])
        conta += 1

    # IMAGENS
    img_aluno = Image.open('icones/alunos.png')
    img_aluno = img_aluno.resize ((80,50))
    img_aluno = ImageTk.PhotoImage(img_aluno)

    img_adc = Image.open('icones/adicionar.png')
    img_adc = img_adc.resize ((20,20))
    img_adc = ImageTk.PhotoImage(img_adc)

    img_atualizar = Image.open('icones/atualizar.png')
    img_atualizar = img_atualizar.resize ((20,20))
    img_atualizar = ImageTk.PhotoImage(img_atualizar)

    img_excluir = Image.open('icones/deletar.png')
    img_excluir = img_excluir.resize ((20,20))
    img_excluir = ImageTk.PhotoImage(img_excluir)

    img_excluir = Image.open('icones/deletar.png')
    img_excluir = img_excluir.resize ((20,20))
    img_excluir = ImageTk.PhotoImage(img_excluir)

    img_todos = Image.open('icones/todos.png')
    img_todos = img_todos.resize ((20,20))
    img_todos = ImageTk.PhotoImage(img_todos)

    img_impressora = Image.open('icones/impressora.png')
    img_impressora = img_impressora.resize((20,20))
    img_impressora = ImageTk.PhotoImage(img_impressora)

    img_x = Image.open('icones/fechar.png')
    img_x = img_x.resize((20,20))
    img_x = ImageTk.PhotoImage(img_x)

    img_lupa = Image.open('icones/lupa.png')
    img_lupa = img_lupa.resize ((14,14))
    img_lupa = ImageTk.PhotoImage(img_lupa)

    frame_controle = Frame(root, background='#DCDCDC', highlightthickness=1.5, highlightbackground='#000000',relief=GROOVE)
    frame_controle.place(relx=0.37, rely=0.13, relheight=0.2, relwidth=0.25) 
    titulocontrole = Label(frame_controle, background='#2E8B57', text='CENTRAL DE CONTROLE', font=('ivy 15 bold'), compound=RIGHT)
    titulocontrole.place(relx=0, rely=0, relheight=0.15, relwidth=1)
    linha_controle = Label(frame_controle, bg='#000000')
    linha_controle.place(relx=0.00, rely=0.14, relheight=0.02, relwidth=1)
    titulo_cadastrados = Label(frm_lista_aluno, background='#2E8B57', text='DADOS CADASTRADOS', font=('ivy 15 bold'), compound=RIGHT)
    titulo_cadastrados.place(relx=0, rely=0, relheight=0.1, relwidth=1)
    linha_cadastrados = Label(frm_lista_aluno, bg='#000000')
    linha_cadastrados.place(relx=0.00, rely=0.1, relheight=0.01, relwidth=1)

    # ÁREA DE CONFECCIONAMENTO DO TÍTULO
    tituloaluno = Label(root, background='#2E8B57', relief=GROOVE, text='TELA DE ALUNOS', font=('ivy 25 bold'), image=img_aluno, compound=RIGHT)
    tituloaluno.place(relx=0, rely=0, relheight=0.1, relwidth=1)
    linha = Label(root, bg='#000000')
    linha.place(relx=0.00, rely=0.09, relheight=0.01, relwidth=1)

    #LABELS 
    l_matricula = Label(root, background='#2E8B57', text='MATRÍCULA', font=('ivy 15 bold'), highlightthickness=1, highlightbackground='black')
    l_matricula.place(x=60, y=109, height=25, width=130)
    l_nome = Label(root, background='#2E8B57', text='NOME', font=('ivy 15 bold'), highlightthickness=1, highlightbackground='black')
    l_nome.place(x=60, y=150, height=25, width=130)
    l_cpf = Label(root, background='#2E8B57', text='CPF', font=('ivy 15 bold'), highlightthickness=1, highlightbackground='black')
    l_cpf.place(x=60, y=191, height=25, width=130)
    l_serie = Label(root, background='#2E8B57', text='SÉRIE', font=('ivy 15 bold'), highlightthickness=1, highlightbackground='black')
    l_serie.place(x=60, y=232, height=25, width=130)
    l_turno = Label(root, background='#2E8B57', text='TURNO', font=('ivy 15 bold'), highlightthickness=1, highlightbackground='black')
    l_turno.place(x=60, y=273, height=25, width=130)
    l_buscar = Label(frm_lista_aluno, background='#DFE3EE', text='BUSCAR', font=('ivy 10 bold'))
    l_buscar.place(relx=0.77, rely=0.12, height=25, width=150)

    #ENTRYS
    s_mtr = StringVar()
    e_mtr = Entry(root, textvariable=s_mtr, font=('ivy 13 '))
    e_mtr.place(x=200, y=109, relwidth=0.1)

    s_nome = StringVar()
    e_nome = Entry(root, textvariable=s_nome, font=('ivy 13 '))
    e_nome.place(x=200, y=150, relwidth=0.2)

    s_cpf = StringVar()
    e_cpf = Entry(root, textvariable=s_cpf, font=('ivy 13'))
    e_cpf.place(x=200, y=191, relwidth=0.1)

    s_serie = StringVar()
    e_serie = Entry(root, textvariable=s_serie, font=('ivy 13 '))
    e_serie.place(x=200, y=232, relwidth=0.1)

    s_turno = StringVar()
    e_turno = Entry(root, textvariable=s_turno, font=('ivy 12 '))
    e_turno.place(x=200, y=273, relwidth=0.1)

    s_buscar = StringVar()
    e_buscar = Entry(frm_lista_aluno, textvariable=s_buscar, font=('ivy 9 '))
    e_buscar.place(relx=0.75, rely=0.18, relwidth=0.15)

    #BOTÕES
    borda_inserir = LabelFrame(frame_controle, bd = 1, bg = "black")
    borda_inserir.pack(pady = 10)
    borda_inserir.place(relx=0.05, rely=0.22)
    botao_inserir = Button (borda_inserir, image=img_adc, compound=RIGHT, anchor=CENTER, command=incluir, 
     text=" INSERIR",
                        overrelief=RIDGE, font=('ivy 10 bold'), bg=co1, fg=co0, highlightthickness=1, highlightbackground='black')
    botao_inserir.place(relwidth=0.11)
    botao_inserir.pack()

    borda_atualizar = LabelFrame(frame_controle, bd = 1, bg = "black")
    borda_atualizar.pack(pady = 10)
    borda_atualizar.place(relx=0.33, rely=0.22)
    botao_atualizar = Button (borda_atualizar, image=img_atualizar, compound=RIGHT, anchor=CENTER, text="ATUALIZAR ",
                        overrelief=RIDGE, font=('ivy 10 bold'), bg=co1, fg=co0, highlightthickness=1, highlightbackground='black', command=atualizar)
    botao_atualizar.place(relwidth=0.11)
    botao_atualizar.pack()

    borda_excluir = LabelFrame(frame_controle, bd = 1, bg = "black")
    borda_excluir.pack(pady = 10)
    borda_excluir.place(relx=0.67, rely=0.22)
    botao_excluir = Button (borda_excluir, image=img_excluir, compound=RIGHT, anchor=CENTER, text="DELETAR",command=excluir,
                        overrelief=RIDGE, font=('ivy 10 bold'), bg=co1, fg=co0, highlightthickness=1, highlightbackground='black')
    botao_excluir.place(relwidth=0.11)
    botao_excluir.pack()

    borda_todos = LabelFrame(frame_controle, bd = 1, bg = "black")
    borda_todos.pack(pady = 10)
    borda_todos.place(relx=0.67, rely=0.47)
    botao_todos = Button (borda_todos, image=img_todos, compound=RIGHT, anchor=CENTER, text="  TODOS ", command=visualiza,
                        overrelief=RIDGE, font=('ivy 10 bold'), bg=co1, fg=co0, highlightthickness=1, highlightbackground='black')
    botao_todos.place(relwidth=0.11)
    botao_todos.pack()

    borda_imprimir = LabelFrame(frame_controle, bd = 1, bg = "black")
    borda_imprimir.pack(pady = 10)
    borda_imprimir.place(relx=0.33, rely=0.47)
    botao_imprimir = Button (borda_imprimir, image=img_impressora, compound=RIGHT, anchor=CENTER, command=imprimir, 
     text="  IMPRIMIR  ",
                        overrelief=RIDGE, font=('ivy 10 bold'), bg=co1, fg=co0, highlightthickness=1, highlightbackground='black')
    botao_imprimir.pack()


    borda_limpar = LabelFrame(frame_controle, bd = 1, bg = "black")
    borda_limpar.pack(pady = 10)
    borda_limpar.place(relx=0.05, rely=0.47)
    botao_limpar = Button (borda_limpar, image=img_x, compound=RIGHT, anchor=CENTER, command=limpa, 
     text=" LIMPAR ",
                        overrelief=RIDGE, font=('ivy 10 bold'), bg=co1, fg=co0, highlightthickness=1, highlightbackground='black')
    botao_limpar.pack()

    borda_lupa = LabelFrame(frm_lista_aluno, bd = 1, bg = "black")
    borda_lupa.pack(pady = 10)
    borda_lupa.place(relx=0.89, rely=0.18)
    botao_lupa = Button (borda_lupa, image=img_lupa, compound=RIGHT, anchor=CENTER, command=buscar,
                        overrelief=RIDGE, font=('ivy 9 bold'), bg=co1, fg=co0, highlightthickness=1, highlightbackground='black')
    botao_lupa.pack()
    visualiza()
    root.mainloop()
#Função para testar se se o usuario e senha sao validos e se for, realizar o login
def botaoentrar():
            try:
                import sqlite3 as lite
                con = lite.connect('db.sistema-academico.db')
                with con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM CADASTRO_USUARIO WHERE USUARIO = " + str(e_usuario.get()))
                    consulta = cur.fetchall()[0]
            except IndexError:
                messagebox.showerror('', 'Usuário ou senha inválido, cheque todos os carácteres.')
                e_usuario.delete(0, END)
                e_senha.delete(0, END)

            except lite.OperationalError:
                messagebox.showerror('', 'Preencha todos os campos corretamente.')
                e_usuario.delete(0, END)
                e_senha.delete(0, END)

            else:
                user_senha = []
                for i in consulta:
                    user_senha.append(i)
                if str(user_senha[1]) != str(e_senha.get()):
                    messagebox.showerror('', 'Senha incorreta .')
                    e_senha.delete(0, END)
                else:
                    telalog.destroy()
                    tela_alunos()
# FUNÇÃO RESPONSÁVEL PELA CRIAÇÃO DA TELA DE LOGIN
def telalogin(): 
    root = Tk() 
    root.title('SDGA - Sistema De Gestão Acadêmica') 
    root.iconbitmap('icones/livro.ico')
    root.geometry('900x600') 
    root.configure(background="#F5F5F5")
    root.resizable(width=FALSE, height=FALSE) 
    style = ttk.Style(root)
    style.theme_use("clam")

    # FUNÇÃO DO BOTÃO QUE CHAMA A TELA DE CADASTRO
    def botaocadastrar():
        root.destroy()
        telacadastro()
        pass

    # CRIAÇÃO DO FRAME PARA REALIZAR O LOGIN 
    frame_login = Frame(root, background='#DCDCDC', highlightthickness=3, highlightbackground='gray',relief=GROOVE)
    frame_login.place(relx=0.33, rely=0.15, relheight=0.60, relwidth=0.40) 

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
    usuariostring = StringVar()
    e_usuario = Entry(frame_login, textvariable=usuariostring)
    e_usuario.place(x=104, y=109, relwidth=0.4)

    senhastring = StringVar()
    e_senha = Entry(frame_login, textvariable=senhastring)
    e_senha.place(x=104, y=148, relwidth=0.4)

    #Função para testar se se o usuario e senha sao validos e se for, realizar o login
    def botaoentrar():
            try:
                import sqlite3 as lite
                con = lite.connect('db.sistema-academico.db')
                with con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM CADASTRO_USUARIO WHERE USUARIO = " + str(e_usuario.get()))
                    consulta = cur.fetchall()[0]
            except IndexError:
                messagebox.showerror('', 'Usuário ou senha inválido, cheque todos os carácteres.')
                e_usuario.delete(0, END)
                e_senha.delete(0, END)
            except lite.OperationalError:
                messagebox.showerror('', 'Preencha todos os campos.')
                e_usuario.delete(0, END)
                e_senha.delete(0, END)

            else:
                user_senha = []
                for i in consulta:
                    user_senha.append(i)
                if str(user_senha[1]) != str(e_senha.get()):
                    messagebox.showerror('', 'Senha incorreta .')
                    e_senha.delete(0, END)
                else:
                    root.destroy()
                    tela_alunos()

    #BOTÕES
    borda_ent = LabelFrame(frame_login, bd = 1, bg = "black")
    borda_ent.pack(pady = 10)
    borda_ent.place(relx=0.37, rely=0.51)
    b_login = Button(borda_ent, text='ENTRAR', font=('Ivy 9 bold'), image=img_entrar, bg='#2E8B57', fg='#000000',
                    compound=RIGHT, width=80, overrelief=RIDGE, relief=GROOVE, anchor=CENTER, command=botaoentrar)
    b_login.pack()

    borda_cdst = LabelFrame(frame_login, bd = 1, bg = "black")
    borda_cdst.pack(pady = 10)
    borda_cdst.place(relx=0.34, rely=0.8)
    b_cadastrar = Button(borda_cdst, text='CADASTRAR-SE', font=('Ivy 9 bold'), image=img_cadastrar, bg='#2E8B57', fg='#000000',command=botaocadastrar,
                    compound=RIGHT, width=102, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_cadastrar.pack()
    root.mainloop()

#CRIAÇÃO DA TELA DE CADASTRO 
def telacadastro(): 
    #Criação da janela
    cadastro = Tk() 
    cadastro.title('SDGA - Sistema De Gestão Acadêmica') 
    cadastro.iconbitmap('icones/livro.ico')
    cadastro.geometry('900x600') 
    cadastro.configure(background="#F5F5F5") 
    cadastro.resizable(width=FALSE, height=FALSE) 
    style = ttk.Style(cadastro) 
    style.theme_use("clam")

    #FUNÇÃO RESPONSÁVEL POR ANALISAR OS DADOS E CRIAR UM USUÁRIO
    def botaofinalizar():
                try:
                    import sqlite3 as lite
                    con = lite.connect('db.sistema-academico.db')
                    cur = con.cursor()
                    cur.execute("INSERT INTO DADOS_CADASTRADOS(USUARIO, NOME, CPF, DATA_NASCIMENTO) VALUES (" + str(e_user.get()) + ',' + " '" + str(e_nome.get()) + "'" + "," + str(e_cpf.get()) + ',' + "'" + str(e_cal.get()) + "'" + ')')
                except lite.IntegrityError:
                    messagebox.showerror('', 'Usuário em uso. Tente outro ou faça login, caso seja o seu.')
                    e_user.delete(0, END)
                except lite.OperationalError:
                    messagebox.showerror('', 'Preencha todos os campos corretamente. (O campo usuário deve ser preenchido apenas por números)')
                else:
                    if len(e_cpf.get()) > 11 or len(e_cpf.get()) < 11:
                        messagebox.showerror('', 'Preencha um CPF válido.')
                        e_cpf.delete(0, END)
                    else:
                        id_cadastro = int(e_user.get()) + 100
                        cur.execute("INSERT INTO CADASTRO_USUARIO(ID_CADASTRO, USUARIO, SENHA) VALUES (" + str(id_cadastro) + ' ,' + e_user.get() + ',' + "'" + e_senha.get() + "'" + ')')
                        con.commit()
                        messagebox.showinfo('', 'Conta criada com sucesso!')
                        cadastro.destroy()
                        telalogin()
    # FUNÇÃO QUE CHAMA A CRIAÇÃO DA TELA DE LOGIN
    def botaologin():
        cadastro.destroy()
        telalogin()

    #Criação do frame principal
    frame_cadastro = Frame(cadastro, background='#DCDCDC', highlightthickness=3, highlightbackground='gray',relief=GROOVE)
    frame_cadastro.place(relx=0.30, rely=0.10, relheight=0.80, relwidth=0.40)

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

    img_senha = Image.open('icones/chave.png')
    img_senha = img_senha.resize ((25,20))
    img_senha = ImageTk.PhotoImage(img_senha)

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
    img_entrar = img_entrar.resize ((20,20))
    img_entrar = ImageTk.PhotoImage(img_entrar)


    #CONFECCIONAMENTO DO TÍTULO
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
    l_txt.place(relx=0.35, rely=0.86)

    l_senha = Label (frame_cadastro, text="CRIE UMA SENHA: ", height=1, anchor=NW, font=('Ivy 8 bold'), bg='#DCDCDC', fg='#000000' )
    l_senha.place(relx=0.15, rely=0.6)
    l_imgsenha = Label(frame_cadastro, bg='#DCDCDC', image=img_senha)
    l_imgsenha.place(relx=0.07, rely=0.63)

    #Entrys
    e_cal = DateEntry (frame_cadastro, width=12, background='#2E8B57', foreground='white', borderwidth=2, year=2022)
    e_cal.place(relx=0.17, rely=0.44)

    e_cpf = Entry (frame_cadastro, width=30)
    e_cpf.place(relx=0.17, rely=0.34)

    e_nome = Entry (frame_cadastro, width=30)
    e_nome.place(relx=0.17, rely=0.24)

    e_user = Entry (frame_cadastro, width=30)
    e_user.place(relx=0.17, rely=0.54)

    e_senha = Entry (frame_cadastro, width=30)
    e_senha.place(relx=0.17, rely=0.64)

    #Botões
    borda_cdstr = LabelFrame(frame_cadastro, bd = 1, bg = "black")
    borda_cdstr.pack(pady = 10)
    borda_cdstr.place(relx=0.35, rely=0.75)
    b_cadastro = Button(borda_cdstr, text='FINALIZADO!', font=('Ivy 9 bold'), image=img_check, bg='#2E8B57', fg='#000000', command=botaofinalizar,
                    compound=RIGHT, width=102, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
    b_cadastro.pack()

    borda_ent = LabelFrame(frame_cadastro, bd = 1, bg = "black")
    borda_ent.pack(pady = 10)
    borda_ent.place(relx=0.34, rely=0.90)
    b_login = Button(borda_ent, text='FAZER LOGIN', font=('Ivy 9 bold'), image=img_entrar, command=botaologin, bg='#2E8B57', fg='#000000',
                    compound=RIGHT, width=110, overrelief=RIDGE, relief=GROOVE, anchor=CENTER, height=12)
    b_login.pack()
    cadastro.mainloop()

#FUNÇÃO RESPONSÁVEL POR CHAMAR A TELA DE CADASTRO
def botaocadastrar():
    telacadastro()

# CRIAÇÃO TELA DE LOGIN
telalog = Tk() 
telalog.title('SDGA - Sistema De Gestão Acadêmica')
telalog.geometry('900x600') 
telalog.configure(background="#F5F5F5")
telalog.iconbitmap('icones/livro.ico')
telalog.resizable(width=FALSE, height=FALSE) 

#FUNÇÃO RESPONSÁVEL POR CHAMAR A TELA DE CADASTRO
def botaocadastrar():
    telalog.destroy()
    telacadastro()

 # CRIAÇÃO DO FRAME PARA REALIZAR O LOGIN 
frame_login = Frame(telalog, background='#DCDCDC', highlightthickness=3, highlightbackground='black',relief=GROOVE)
frame_login.place(relx=0.33, rely=0.15, relheight=0.60, relwidth=0.40) 

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
l_usuario = Label (frame_login, text="USUÁRIO", height=1, anchor=NW, font=('Ivy 8 bold'), bg='#DCDCDC', fg='#000000' )
l_usuario.place(x=104, y=93)
l_imgusuario = Label(frame_login, bg='#DCDCDC', image=img_usuario)
l_imgusuario.place(x=72, y=106)

l_senha = Label (frame_login, text="SENHA", height=1, anchor=NW, font=('Ivy 8 bold'), bg='#DCDCDC', fg='#000000' )
l_senha.place(x=104, y=133)
l_imgsenha = Label(frame_login, bg='#DCDCDC', image=img_senha)
l_imgsenha.place(x=71, y=146)

l_login = Label(frame_login, image=img_login, compound=RIGHT, anchor=CENTER,
                     font=('ivy 17 bold'), bg='#2E8B57', relief=GROOVE)
l_login.place(relwidth=1, relheight=0.1)

l_txt = Label(frame_login, anchor=CENTER, bg='#DCDCDC', text='Não tem um usuário?', fg='#000000')
l_txt.place(relx=0.32, rely=0.74)
linha = Label(frame_login, bg='black')
linha.place(relx=0.00, rely=0.09, relheight=0.01, relwidth=1)

#ENTRYS
e_usuario = Entry(frame_login)
e_usuario.place(x=104, y=109, relwidth=0.4)

e_senha = Entry(frame_login)
e_senha.place(x=104, y=148, relwidth=0.4)

#BOTÕES
borda_ent = LabelFrame(frame_login, bd = 1, bg = "black")
borda_ent.pack(pady = 10)
borda_ent.place(relx=0.37, rely=0.51)
b_login = Button(borda_ent, text='ENTRAR', font=('Ivy 9 bold'), image=img_entrar, bg='#2E8B57', fg='#000000',
                    compound=RIGHT, width=80, overrelief=RIDGE, relief=GROOVE, anchor=CENTER, command=botaoentrar)
b_login.pack()

borda_cdst = LabelFrame(frame_login, bd = 2, bg = "black")
borda_cdst.pack(pady = 10)
borda_cdst.place(relx=0.34, rely=0.8)
b_cadastrar = Button(borda_cdst, text='CADASTRAR-SE', font=('Ivy 9 bold'), image=img_cadastrar, bg='#2E8B57', fg='#000000',command=botaocadastrar,
                    compound=RIGHT, width=102, overrelief=RIDGE, relief=GROOVE, anchor=CENTER)
b_cadastrar.pack()

telalog.mainloop()