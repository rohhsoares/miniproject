import customtkinter as ctk
from banco import conectar
from tkinter import messagebox


def salvar(nome, codigo, preco, quantidade, categoria):

    try:

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO medicamentos
        (nome, codigo, preco, quantidade, categoria)
        VALUES (?, ?, ?, ?, ?)
        """, (nome, codigo, preco, quantidade, categoria))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sucesso",
            "Medicamento cadastrado!"
        )

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            f"Erro ao cadastrar:\n{erro}"
        )


def abrir_tela_cadastro():

    tela = ctk.CTkToplevel()

    tela.title("Cadastro de Medicamentos")
    tela.geometry("700x700")

    titulo = ctk.CTkLabel(
        tela,
        text="💊 Cadastro de Medicamentos",
        font=("Arial", 30, "bold")
    )

    titulo.pack(pady=30)

    frame = ctk.CTkFrame(tela)
    frame.pack(padx=40, pady=20, fill="both", expand=True)

    # NOME

    ctk.CTkLabel(
        frame,
        text="Nome do Medicamento",
        font=("Arial", 18)
    ).pack(pady=10)

    entry_nome = ctk.CTkEntry(
        frame,
        width=400,
        height=45
    )

    entry_nome.pack()

    # CÓDIGO

    ctk.CTkLabel(
        frame,
        text="Código",
        font=("Arial", 18)
    ).pack(pady=10)

    entry_codigo = ctk.CTkEntry(
        frame,
        width=400,
        height=45
    )

    entry_codigo.pack()

    # PREÇO

    ctk.CTkLabel(
        frame,
        text="Preço",
        font=("Arial", 18)
    ).pack(pady=10)

    entry_preco = ctk.CTkEntry(
        frame,
        width=400,
        height=45
    )

    entry_preco.pack()

    # QUANTIDADE

    ctk.CTkLabel(
        frame,
        text="Quantidade",
        font=("Arial", 18)
    ).pack(pady=10)

    entry_quantidade = ctk.CTkEntry(
        frame,
        width=400,
        height=45
    )

    entry_quantidade.pack()

    # CATEGORIA

    ctk.CTkLabel(
        frame,
        text="Categoria",
        font=("Arial", 18)
    ).pack(pady=10)

    entry_categoria = ctk.CTkEntry(
        frame,
        width=400,
        height=45
    )

    entry_categoria.pack()

    # BOTÃO

    btn_salvar = ctk.CTkButton(
        frame,
        text="Salvar Medicamento",
        height=60,
        font=("Arial", 20, "bold"),
        fg_color="green",
        hover_color="#006400",
        command=lambda: salvar(
            entry_nome.get(),
            entry_codigo.get(),
            entry_preco.get(),
            entry_quantidade.get(),
            entry_categoria.get()
        )
    )

    btn_salvar.pack(
        pady=40,
        padx=50,
        fill="x"
    )