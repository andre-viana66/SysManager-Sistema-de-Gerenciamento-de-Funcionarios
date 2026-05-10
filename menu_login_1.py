from tkinter import *
import customtkinter as ctk
from customtkinter import CTkButton
from PIL import Image
import pandas as pd
import os
from menu_cadastro_2 import cadastro_usuario
from menu_principal import menu_principal

ctk.set_appearance_mode("dark")


def login():
    #criando a janela de login
    janela_login = ctk.CTk()
    janela_login.geometry("700x400")
    janela_login.resizable(width=False, height=False)
    janela_login.title("Janela de login")

    #importando blackground
    imagem_blackground = ctk.CTkImage(dark_image=Image.open("images_projeto/fundo_roxo.jpg")
                                      ,size=(700,400)
                                      )
    ctk.CTkLabel(janela_login, text=None, image=imagem_blackground).place(x=0 , y=0)

    #criando Frame para o login
    frame_login = ctk.CTkFrame(janela_login,
                               width=280,
                               height=320,
                               corner_radius=20,
                               fg_color="#290247",
                               border_color="#330458",
                               border_width=5,
                               bg_color="transparent"
                               )

    frame_login.place(x=210, y=40)

    #adicionando imagem ao blackground
    imagem_key = ctk.CTkImage(dark_image=Image.open("images_projeto/chave_icon.jpg"), size=(30, 30))
    ctk.CTkLabel(janela_login, text=None, image=imagem_key).place(relx=0.5, rely=0.17, anchor="center")

    #adicionando texto principal
    ctk.CTkLabel(janela_login, font=("Consolas", 18, "bold"),
                 text="SISTEMA DE LOGIN", text_color="white",
                 bg_color="#290247").place(relx=0.5, rely=0.28, anchor="center")


    #adicionando caixa de entrada para o usuario
    usuario = ctk.CTkEntry(janela_login, placeholder_text="Usuário:",
                           corner_radius=20,
                           bg_color="#290247",
                           width=200
                           )
    usuario.place(relx=0.5, rely=0.42, anchor="center")

    #adicionando caixa de entrada para a senha
    senha = ctk.CTkEntry(janela_login, placeholder_text="Senha:",
                         corner_radius=20,
                         bg_color="#290247",
                         show="*",
                         width=200
                         )
    senha.place(relx=0.5, rely=0.54, anchor="center")

    #verificando entradas de usuario antes do envio
    def verificar_login():
        #abrindo arquivo com o pandas e verificando se existe no banco de senhas
        arquivo = "dados_projeto/lista_de_senhas.csv"

        if usuario.get() == "" or senha.get() == "":
            erro = ctk.CTkLabel(frame_login,
                                      text="Usuário ou senha incorretos",
                                      text_color="red",
                                      font=("Consolas", 11),
                                      bg_color="#290247"
                                      )
            erro.place(relx=0.5, rely=0.64, anchor="center")
            return

        if not os.path.exists(arquivo):
            erro = ctk.CTkLabel(frame_login,
                                      text="Usuário ou senha incorretos",
                                      text_color="red",
                                      font=("Consolas", 11),
                                      bg_color="#290247"
                                      )
            erro.place(relx=0.5, rely=0.64, anchor="center")
            return

        df = pd.read_csv(arquivo, dtype=str)
        resultado = df[
            (df["usuario"] == usuario.get()) &
            (df["senha"] == senha.get())
            ]

        if not resultado.empty:
            menu_principal()
            usuario.delete(0, END)
            senha.delete(0, END)
        else:
            erro = ctk.CTkLabel(frame_login,
                                      text="Usuário ou senha incorretos",
                                      text_color="red",
                                      font=("Consolas", 11),
                                      bg_color="#290247"
                                      )
            erro.place(relx=0.5, rely=0.64, anchor="center")




    #adicionando botão de entrar no sistema
    entrar = ctk.CTkButton(janela_login,
                           text="Entrar",
                           corner_radius=20,
                           bg_color="#290247",
                           fg_color="#5c0f8b",
                           hover_color="#330458",
                           command=verificar_login
                           )
    entrar.place(relx=0.5, rely=0.69, anchor="center")


    #adicionando botao de cadastro
    cadastro = ctk.CTkButton(janela_login,
                             text="Cadastrar Usuário",
                             corner_radius=20,
                             bg_color="#290247",
                             fg_color="transparent",
                             border_color="#330458",
                             hover_color="#330458",
                             command= cadastro_usuario
                             )
    cadastro.place(relx=0.5, rely=0.80, anchor="center")


    janela_login.mainloop()


login()