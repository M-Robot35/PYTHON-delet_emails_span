from imap_tools import MailBox, AND


# Documentação imap
#  https://pypi.org/project/imap-tools/

"""
Rodar o comando =>  pip install imap-tools
para instalar os repositorios
"""

login = 'seuEmail@gmail.com'
senha = '***********'  # SUA SENHA ALEATORIA GERADA PELO GMAIL

hostGmail = 'smtp.gmail.com'

# LISTA E EMAIL PARA SEREM EXCLUIDOS
emailDelete = ['mailing@newfaceinfo.com.br', 
               'no-reply@news.loggi.com',
               'newsletter@investingmail.com', 
               'newsletter@allnations.com.br',
               'selecoes@selecoesbrasil.com.br',
               'support@codepen.io',
               'ead@dio.me',              
               'news@comunicacao.mensmarket.com.br',
               'info@twitter.com',
               'jobs-listings@linkedin.com',
               'jobalerts-noreply@linkedin.com',
               'alert@indeed.com',
               'hello@coingecko.com',
               'info@trabajo.org',
               'updates-noreply@linkedin.com',
               'info@novadax.com',
               'info@infojobs.com.br',
               'vendas@ceitel.com.br',
               'promotions@blaze.com',
               'contato@e-mail.sorteonline.com.br',
               'voude99@99app.com',
               'suporte@ignicaodigital.com.br',
               'relacionamento@camisetasimportadas.com',
               'naoresponder@monetizze.com.br',
               'Vendadireta@relacionarede.oboticario.com.br',
               'nao-responder@mercadolivre.com',
               'delivery@dispatch.academiadoimportador.com',
               'smartdesk@lge.com',
               'vendas04@webseguranca.com',
               'noreply@eobot.com',
               'support@zencard.zendesk.com',
               'noreply@youtube.com',
               'contato@traderbinario.com.br',
               'next@campanhas.next.b.br',
               'atom@atomeducacional.com.br',
               'indicaai@mailer.indicaai.quintoandar.com.br',
                'noreply@iqoption.com',
                'contato@cftvclub.com.br',
                'no-reply@notification.bitcibrasil.com',
                'alert@notification.bebee.com',
                'carolpaiffer@atomeducacional.com.br',
                'jobemail@jobbydoo.com.br',
                'info@rollercoin.com',
                'newsletter@deals.banggood.com',
                'noreply@comunicacao.bancointer.com.br',
                'espetinhosmineiro@hotmail.com',
                'reply@crm.sumup.com.br',
                'ame@news.amedigital.com',
                'contato@fullstackagency.club',
                'contato@minascap.com',
               ]

   
class EmailConfig:
    def __init__(self):
        self.connect_imap = MailBox(host= hostGmail).login(login, senha) 
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
        


# imapLib = EmailConfig()
# imapLib.deleteEmail(emailDelete)






















