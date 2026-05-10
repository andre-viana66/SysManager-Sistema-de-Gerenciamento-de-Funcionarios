from tkinter import *
import customtkinter as ctk
from customtkinter import CTkButton
from PIL import Image
import pandas as pd
import os
from banco_de_senhas import banco_senhas

ctk.set_appearance_mode("dark")

def cadastro_usuario():
    #criando janela de cadastro
    janela_cadastro = ctk.CTkToplevel()
    janela_cadastro.geometry("700x400")
    janela_cadastro.resizable(width=False, height=False)
    janela_cadastro.title("Janela de cadastro")
    #importando blackground
    imagem_blackground = ctk.CTkImage(dark_image=Image.open("images_projeto/fundo_roxo.jpg")
                                      ,size=(700,400)
                                      )
    ctk.CTkLabel(janela_cadastro, text=None, image=imagem_blackground).place(x=0 , y=0)

    #criando Frame para o login
    frame_login = ctk.CTkFrame(janela_cadastro,
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
    ctk.CTkLabel(janela_cadastro, text=None, image=imagem_key).place(relx=0.5, rely=0.17, anchor="center")

    #adicionando texto principal
    ctk.CTkLabel(janela_cadastro, font=("Consolas", 18, "bold"),
                 text="CADASTRO DE USUARIO", text_color="white",
                 bg_color="#290247").place(relx=0.5, rely=0.28, anchor="center")

    #adicionando caixa de entrada para o usuario
    usuario = ctk.CTkEntry(janela_cadastro,
                           width=200,
                           placeholder_text="Usuário:",
                           corner_radius=20,
                           bg_color="#290247"
                           )
    usuario.place(relx=0.5, rely=0.42, anchor="center")

    #adicionando caixa de entrada para a senha
    senha = ctk.CTkEntry(janela_cadastro,
                         width=200,
                         placeholder_text="Senha:",
                         corner_radius=20,
                         bg_color="#290247",
                         show="*"
                         )
    senha.place(relx=0.5, rely=0.54, anchor="center")

    #adionando caixa de entrada para repetir a senha
    senha_repeticao = ctk.CTkEntry(janela_cadastro,
                         width=200,
                         placeholder_text="Repita a senha:",
                         corner_radius=20,
                         bg_color="#290247",
                         show="*"
                         )
    senha_repeticao.place(relx=0.5, rely=0.67, anchor="center")

    #verificando entradas do usuario antes do envio
    def verificar_cadastro():
        if senha.get() != senha_repeticao.get():
            erro = ctk.CTkLabel(janela_cadastro,
                                text="Usuário ou senhas incorretas",
                                text_color="red",
                                font=("Consolas", 11),
                                bg_color="#290247"
                                )
            erro.place(relx=0.5, rely=0.76, anchor="center")
        elif usuario.get() == "" or senha.get() == "" or senha_repeticao.get() == "":
            erro = ctk.CTkLabel(janela_cadastro,
                                text="Usuário ou senhas incorretas",
                                text_color="red",
                                font=("Consolas", 11),
                                bg_color="#290247"
                                )
            erro.place(relx=0.5, rely=0.76, anchor="center")
        else:
            banco_senhas(usuario, senha, senha_repeticao)

    #adicionando botao de enviar cadastro
    enviar_cadastro = ctk.CTkButton(janela_cadastro,
                             text="Enviar cadastro",
                             corner_radius=20,
                             bg_color="#290247",
                             fg_color="#5c0f8b",
                             hover_color="#330458",
                            command=verificar_cadastro
                             )
    enviar_cadastro.place(relx=0.5, rely=0.83, anchor="center")


    janela_cadastro.mainloop()

