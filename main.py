from imap_tools import MailBox, AND
from banco.bd_connexao import *
from tools import *
import os
from time import sleep


# Documentação imap
#  https://pypi.org/project/imap-tools/

"""
* Rodar o comando =>   pip install pip install imap-tools
* criar venv // python -m venv [ venv ou nome desejado ]

para instalar os repositorios

download Sqlit para visualizar Bd

https://sqlitebrowser.org/dl/

"""

login = 'thiago.teles725@gmail.com'  # seu email
senha = 'ozuefpmckttt'  # exemplo sua senha unica gmail

hostGmail = 'smtp.gmail.com'

class EmailConfig:
    def __init__(self):
        self.connect_imap = MailBox(host= hostGmail).login(username=login, password=senha) 
        self.path_arquiv = "./download" #default
        if not os.path.exists(self.path_arquiv): os.mkdir(self.path_arquiv)
        print('--- Online  ---')
    
    def deleteEmail(self, deletList):
        #  --- SHORT DELETE ---
        # print('buscando...')
        # dell  = [self.connect_imap.delete([msg.uid for msg in self.connect_imap.fetch(AND(from_ = email))]) for email in deletList ]         
        # print('Finalizado')        
        
        emailDelete = deletList        
        
        for index, i in enumerate(emailDelete, start=1):
    
            email_Repeat = emailDelete.count(i)
            
            if email_Repeat > 1:
                print(f"O E-mail: {i} se repete {email_Repeat} Vezes")
                
            def recursiva(email_list):                
                
                id = []
                            
                for msg in self.connect_imap.fetch(AND(from_ = email_list)):
                    id.append(msg.uid)
                    
                self.connect_imap.delete(id) 
                
                if len(id) > 0:           
                    print(f"E-mail: {email_list} ","Deleted: ", f"[{len(id)}]")
                else:
                    print(f'Pesquisando {index} {len(emailDelete)}')     
            
            recursiva(i)       
        
    def foldersDownload(self, download= False):  
           
        for arquivo in self.connect_imap.fetch():
            for conteudo in arquivo.attachments:
                nome_arquivo  = conteudo.filename  
                              
                arquivo_payload = conteudo.payload    
                            
                nome, extensao = os.path.splitext(nome_arquivo)  
                 
                setName = clearCharacters(arquivo.from_)    
                           
                setArquivo = clearCharacters(nome_arquivo)
                
                path_complet = os.path.join(self.path_arquiv, setName, setArquivo)
                print(nome)
                
                if not os.path.exists(os.path.dirname(path_complet)): os.mkdir(os.path.dirname(path_complet))               
                                        
                if extensao != "":
                    if os.path.exists(os.path.dirname(path_complet)):
                        if not os.path.exists(path_complet):
                            try:
                                with open(path_complet, "bw") as file:
                                    file.write(arquivo_payload)
                            except:
                                print('Arquivo não baixado: ',nome_arquivo)                                
                    
                                
                    else:
                        print('*',50)
                        print('O caminho não existe: ',arquivo.from_ )  
                        print('*',50)
                        sleep(3)
                        continue  
                                 
                removePastaVazia(self.path_arquiv)
                
    def download_for_email(self, inemail):  
        print(inemail)
        for msg in self.connect_imap.fetch(AND(from_ = inemail)):
                for email in msg.attachments:
                    nome_arquivo = email.filename
                    nome, extensao = os.path.splitext(nome_arquivo)          
                    
                    arquivo_payload = email.payload
                    setName =  clearCharacters(msg.from_)                
                    setArquivo = clearCharacters(nome_arquivo)
                
                    path_complet = os.path.join(self.path_arquiv, setName, setArquivo)                    
                    print(path_complet)
                    
                    if not os.path.exists(os.path.dirname(path_complet)): os.mkdir(os.path.dirname(path_complet))
                    
                    if not os.path.exists(path_complet):
                        try:
                            with open(path_complet, "bw") as file:
                                file.write(arquivo_payload)
                        except:
                            print('Arquivo não baixado: ',nome_arquivo)
                    
                        print("\t",nome_arquivo)
                        
                    removePastaVazia(self.path_arquiv)               
        
            
if __name__ == "__main__":  
    while True:   
        inserir = input("Deseja inserir um email: [Y]->[SIM] e [N]->[NÃO]").lower().startswith("y")
        
        if inserir:
            int_bd = input('Insira o email: ')
            banco.inserirConteudo(int_bd)
            
        else:
            break
        
    
    emailDelete = Bd_select_emails

    imapLib = EmailConfig()
    imapLib.deleteEmail(emailDelete)
    
    # imapLib.foldersDownload()
    
    # imapLib.download_for_email("noreply@nfe.io")
    
    # deleteID = banco.deletaData(55)

   
  
