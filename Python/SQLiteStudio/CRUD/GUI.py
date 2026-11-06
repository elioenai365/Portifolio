# Esse código tem por objetivo importar o tkinter e definir o paddle:O Tkinter é a biblioteca padrão do Python para a
# criação de interfaces gráficas (telas, botões, janelas). Quando falamos em "definição do paddle" (raquete) nesse
# contexto, estamos nos referindo à criação de um objeto visual


from tkinter import * #modulo para desenvolver uma interface gráfica.


class Gui():# Graphical user interface
    """Classe da Interface Gráfica"""

    #variaveis que estabelece distanciamento entre o conteúdo e a sua borda

    x_pad =5
    y_pad =3
    width_entry = 30# largura da janela

# Para criar uma Janela
    #pysql sera o nome fantasia da aplicação
    window = Tk()
    window.wm_title("PYSQL  versão 1.0")

# Definição das variáveis que recebem os dados inseridos pelo user
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

# Criando os objetos que farão parte das Janelas

    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")

    entNome = Entry(window, textvariable=txtNome, width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
    entSobrenome= Entry(window, textvariable=txtSobrenome, width=width_entry)
    entCPF = Entry(window, textvariable=txtCPF, width=width_entry)

    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)

    btnViewAll = Button(window, text="Ver Todos" )
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDelete = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

#Associar os objetos criados ao GRID da Janela

    lblnome.grid(row=0, column=0)
    lblsobrenome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblcpf.grid(row=3, column=0)

    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)

    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDelete.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

#União do Scrollbar com a Listbox

    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

#Adicionar SWAG(aparência) a interface

    for child in window.winfo_children():
        widget_class = child.winfo_class()
        if widget_class == "Button":
            child.grid_configure(sticky = "WE", padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0 , sticky="NS")
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky="NS")
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky="N")

    def run(self):
        Gui.window.mainloop()