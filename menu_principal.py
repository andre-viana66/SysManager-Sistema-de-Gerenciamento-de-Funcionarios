from tkinter import *
import customtkinter as ctk
from customtkinter import CTkButton
from PIL import Image
import pandas as pd
import os

ctk.set_appearance_mode("dark")


def menu_principal():
    #criando janela de menu principal
    janela_principal = ctk.CTkToplevel()
    janela_principal.geometry("1100x600")
    janela_principal.resizable(width=False, height=False)
    janela_principal.title("Sistema de gerenciamento")

    #importando blackground
    imagem_blackground = ctk.CTkImage(dark_image=Image.open("images_projeto/fundo_roxo.jpg")
                                      , size=(1100, 600)
                                      )
    ctk.CTkLabel(janela_principal, text=None, image=imagem_blackground).place(x=0, y=0)

    #criando frame de funcionalidades
    frame_funcionalidades = ctk.CTkFrame(janela_principal,
                                         width=240,
                                         height=580,
                                         corner_radius=20,
                                         fg_color="#290247",
                                         border_color="#330458",
                                         border_width=5,
                                         bg_color="transparent"
                                         )

    frame_funcionalidades.place(x=10, y=10)

    #criando frame de conteudos
    frame_conteudo = ctk.CTkFrame(janela_principal,
                                  width=835,
                                  height=580,
                                  corner_radius=20,
                                  fg_color="#290247",
                                  border_color="#330458",
                                  border_width=5,
                                  bg_color="transparent"
                                  )
    frame_conteudo.place(x=260, y=10)

    #adicionando texto no frame de funcionalidades
    ctk.CTkLabel(frame_funcionalidades,
                 font=("Consolas", 18, "bold"),
                 text="FUNCIONALIDADES",
                 text_color="white",
                 bg_color="#290247"
                 ).place(relx=0.5, rely=0.07, anchor="center")

    #adicionando texto no frame de conteudos
    ctk.CTkLabel(frame_conteudo,
                 font=("Consolas", 18, "bold"),
                 text="SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS",
                 text_color="white",
                 bg_color="#290247"
                 ).place(relx=0.5, rely=0.07, anchor="center")

    #criando botão home
    botao_home = ctk.CTkButton(frame_funcionalidades,
                               text="Home",
                               corner_radius=20,
                               bg_color="#290247",
                               fg_color="#5c0f8b",
                               hover_color="#330458",
                               )
    botao_home.place(relx=0.5, rely=0.20, anchor="center")

    #criando botao cadastro
    botao_cadastro = ctk.CTkButton(frame_funcionalidades,
                               text="Cadastro",
                               corner_radius=20,
                               bg_color="#290247",
                               fg_color="#5c0f8b",
                               hover_color="#330458",
                               )
    botao_cadastro.place(relx=0.5, rely=0.30, anchor="center")

    #criando botao dashboard
    botao_dashboard = ctk.CTkButton(frame_funcionalidades,
                               text="Dashboard",
                               corner_radius=20,
                               bg_color="#290247",
                               fg_color="#5c0f8b",
                               hover_color="#330458",
                               )
    botao_dashboard.place(relx=0.5, rely=0.40, anchor="center")

    #criando botao de configuração
    botao_config = ctk.CTkButton(frame_funcionalidades,
                               text="Configuração",
                               corner_radius=20,
                               bg_color="#290247",
                               fg_color="#5c0f8b",
                               hover_color="#330458",
                               )
    botao_config.place(relx=0.5, rely=0.85, anchor="center")




