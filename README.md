# 🖥️ SysManager — Sistema de Gerenciamento de Funcionários

Sistema desktop com interface gráfica desenvolvido em Python, com tela de login segura e painel de gerenciamento de funcionários. Projeto em desenvolvimento ativo.

---

## 🚧 Status do Projeto

> **Em desenvolvimento** — funcionalidades sendo adicionadas progressivamente.

---

## ✅ Funcionalidades implementadas

- **Login de usuário** — autenticação com usuário e senha via banco de dados CSV
- **Cadastro de usuário** — criação de novos acessos ao sistema com validação de campos
- **Menu principal** — painel com sidebar de navegação e área de conteúdo
- **Validação de formulários** — mensagens de erro exibidas diretamente na janela

## 🔜 Funcionalidades em desenvolvimento

- [ ] Cadastro de funcionários
- [ ] Listagem de funcionários
- [ ] Dashboard com indicadores
- [ ] Configurações do sistema

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3 | Linguagem principal |
| CustomTkinter | Interface gráfica moderna |
| Pillow (PIL) | Carregamento de imagens |
| Pandas | Leitura e escrita do banco de dados CSV |
| OS | Verificação e manipulação de arquivos |

---

## 📁 Estrutura do projeto

```
📦 projeto-sistema-login-pt3
 ┣ 📂 dados_projeto
 ┃ ┗ 📄 lista_de_senhas.csv           # Banco de dados de usuários (gerado automaticamente)
 ┣ 📂 images_projeto
 ┃ ┣ 🖼️ chave_icon.jpg                # Ícone da tela de login
 ┃ ┣ 🖼️ fundo_roxo.jpg                # Background da tela de login
 ┃ ┣ 🖼️ linha_1.png                   # Elemento decorativo
 ┃ ┗ 🖼️ retro_purple_blackground.jpg  # Background alternativo
 ┣ 📄 banco_de_senhas.py              # Lógica de salvamento de usuários
 ┣ 📄 menu_cadastro_2.py              # Janela de cadastro de usuário
 ┣ 📄 menu_login_1.py                 # Janela principal de login (ponto de entrada)
 ┗ 📄 menu_principal.py               # Painel principal do sistema
```

---

## ⚙️ Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/sysmanager.git
cd sysmanager
```

### 2. Instale as dependências
```bash
pip install customtkinter pillow pandas
```

### 3. Execute o programa
```bash
python menu_login_1.py
```

---

## 🚀 Como usar

### Tela de Login
1. Digite seu **usuário** e **senha**
2. Clique em **Entrar**
3. Caso não tenha cadastro, clique em **Cadastrar Usuário**

### Tela de Cadastro
1. Digite o **usuário** desejado
2. Digite a **senha** e **repita a senha**
3. Clique em **Enviar cadastro**
4. O usuário será salvo automaticamente em `dados_projeto/lista_de_senhas.csv`

### Menu Principal
- Navegue pelas funcionalidades pelo **menu lateral esquerdo**

---

## ⚠️ Observações

- O arquivo `lista_de_senhas.csv` é criado automaticamente na primeira vez que um usuário é cadastrado
- As senhas são armazenadas em **texto puro** — para uso em produção recomenda-se aplicar criptografia como `bcrypt`
- Todas as imagens devem estar na pasta `images_projeto/`

---

## 📌 Melhorias futuras

- [ ] Criptografia de senhas com `bcrypt`
- [ ] Migração do banco de dados CSV para SQLite
- [ ] Tela de recuperação de senha
- [ ] Relatórios exportáveis em PDF

---

## 👤 Autor

Feito por **seu-nome** — sinta-se à vontade para contribuir!
