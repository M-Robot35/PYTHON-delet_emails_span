from imap_tools import MailBox, AND
from banco.bd_connexao import *
from tqdm import tqdm
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
senha = 'bzbojshrctcyfjni'  # sua senha unica gmail

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
        
        for i in tqdm(emailDelete):           
                
            def recursiva(email_list):                
                
                id = []
                            
                for msg in self.connect_imap.fetch(AND(from_ = email_list)):
                    id.append(msg.uid)
                    
                self.connect_imap.delete(id)                   
            
            recursiva(i)       
        
    def foldersDownload(self, download= False):  
           
        for arquivo in tqdm(self.connect_imap.fetch()):
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
        for msg in self.connect_imap.fetch(AND(from_ = inemail)):
                for email in msg.attachments:
                    nome_arquivo = email.filename
                    nome, extensao = os.path.splitext(nome_arquivo)          
                    
                    arquivo_payload = email.payload
                    setName =  clearCharacters(msg.from_)                
                    setArquivo = clearCharacters(nome_arquivo)
                
                    path_complet = os.path.join(self.path_arquiv, setName, setArquivo)                    
                    
                    if not os.path.exists(os.path.dirname(path_complet)): os.mkdir(os.path.dirname(path_complet))
                    
                    if not os.path.exists(path_complet):
                        try:
                            with open(path_complet, "bw") as file:
                                file.write(arquivo_payload)
                        except:
                            print('Arquivo não baixado: ',nome_arquivo)
                    
                        print("\t",nome_arquivo)
                        
                    removePastaVazia(self.path_arquiv)               
        

def main():
    while True:
        imapLib = EmailConfig()
        tamanho = 50
        print('*'*tamanho)
        print('escolha uma das opções'.center(tamanho," "))
        print('*'*tamanho)
        print('escolha um Nº das opções \n'.ljust(tamanho," "))
        print('1 - Inserir um e-mail .')
        print('2 - Deletar emails de Span .')
        print('3 - Faz Download de todos anexos do E-mail .')
        print('4 - Faz download de anexos em 1 E-mail .')
        print('5 - Deleta E-mail salvo no Bd .')
        print('6 - ----------- .\n')
        print('0 - sair (exit) .\n')
        
        
        options = input("Digite sua opção: ")
        if options == "1":
            int_bd = input('Insira o email: ')
            banco.inserirConteudo(int_bd)
            
        elif options == "2":
            # DELETAR EMAILS DE SPAN
            emailDelete = Bd_select_emails
            imapLib.deleteEmail(emailDelete)
            
        elif options == "3":
            # Busca anexos em todos os emails
            imapLib.foldersDownload()
                
            
        elif options == "4":
            #  Busca anexos em um único email
            entradaEmail = str(input("digite email para bucar anexos: "))
            imapLib.download_for_email(entradaEmail)

        elif options == "5":
            # DELETA email do Bd por  ID
            digitID = int(input('Digite o Id do Email: '))
            banco.deletaData(digitID)
            
        elif options == "6":
            for i in tqdm(range(10)):
                sleep(1)
            pass
        elif options == "0":
            print('\nespero que tenha gostado Obrigado Volte sempre\n'.capitalize())
            exit()
            
        
        else:
            print('opção invalida')
        
        
            
            
if __name__ == "__main__":  
    main()
    

   
  
