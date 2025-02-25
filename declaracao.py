import smtplib
import pandas as pd
import os
from email.message import EmailMessage

# Configuração do e-mail remetente

EMAIL_REMETENTE = "xxxxx"
SENHA = "xxx"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

#Para pegar a senha do Gmail
"""
Passo a passo para corrigir
Ativar a verificação em duas etapas do Google

Vá para Minha Conta Google.
Ative a opção Verificação em duas etapas.
Gerar uma senha de aplicativo

Acesse Senhas de Aplicativo do Google.
Escolha o tipo de aplicativo como "E-mail" e o dispositivo como "Outro (Nome personalizado)".
Digite um nome (exemplo: "Python Automation") e clique em Gerar.
Copie a senha gerada.
Substituir no código

No seu código, substitua a senha comum pela senha de aplicativo:


EMAIL_REMETENTE = "seuemail@gmail.com"
SENHA = "senha-gerada-aqui"  # Use a senha de aplicativo gerada
Executar o código novamente
Após essas configurações, o Gmail permitirá o envio dos e-mails pelo script.
"""

# Carregar a planilha com os dados
caminho_arquivo = "/content/dados.csv"

# Lendo os dados corretamente, ignorando espaços em branco nos nomes das colunas
planilha = pd.read_csv(caminho_arquivo, delimiter=";")  # Ajuste o delimitador se necessário

# Renomear corretamente as colunas com base na planilha
planilha.columns = ["Data_Hora", "Nome", "Email", "Curso", "Periodo", "Palestra", "Palavra_Chave"]

# Caminho das declarações
pasta_declaracoes = "/content/declaracoes/"

# Função para enviar o e-mail
def enviar_email(destinatario, nome, palestra, arquivo):
    msg = EmailMessage()
    msg['Subject'] = "Sua Declaração de Participação"
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = destinatario
    msg.set_content(f"Olá {nome},\n\nSegue em anexo sua declaração de participação na palestra '{palestra}'.\n\nAtenciosamente,\nOrganização do Evento")

    # Adicionar anexo (assumindo que os arquivos sigam a numeração de 1 a 47)
    with open(arquivo, "rb") as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(arquivo))

    # Enviar o e-mail
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_REMETENTE, SENHA)
        server.send_message(msg)
        print(f"E-mail enviado para {destinatario}")

# Enviar e-mails apenas para os 47 primeiros alunos
for index, row in planilha.head(47).iterrows():
    arquivo = f"{pasta_declaracoes}Declarações-{index+1}.pdf"  # Nome dos arquivos das declarações
    if os.path.exists(arquivo):  # Verifica se o arquivo existe antes de enviar
        enviar_email(row["Email"], row["Nome"], row["Palestra"], arquivo)
    else:
        print(f"Arquivo não encontrado: {arquivo}")

"""# Nova seção"""