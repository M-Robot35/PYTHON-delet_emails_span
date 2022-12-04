import sqlite3
import os

db_path = "./banco/emails.db"    

class BancoDeDados:
    def __init__(self):        
        self.connexao = sqlite3.Connection(db_path)
        self.cursor = self.connexao.cursor()        
       
    def createTable(self):
        query = """
            CREATE TABLE IF NOT EXISTS emails_deleted(id INTEGER PRIMARY KEY AUTOINCREMENT, email UNIQUE);        
        """
        self.cursor.execute(query)
        print("Table Sucess !")

    def select(self):
        query = """
            SELECT * FROM emails_deleted;        
        """
        x = self.cursor.execute(query).fetchall()
        if x == None or x == []:
            print("A tabela esta vazia")
            
        # print(x)
        return x
    
    
    def inserirConteudo(self, insertEmail, msg='inserido com Sucesso !!!'):
        insert = insertEmail
        try:
            query = f"""
                INSERT INTO emails_deleted(email) VALUES('{insert}');
            """ 
            self.cursor.execute(query)
            self.connexao.commit()
            
            msg.center(50, "*")
            print(msg)    
            
            
        except:
            msg = 'já existe no banco de dados'.center(50, "*")
            print(msg)
            
    def deletaData(self, id):
        
        if not ('int' in str(type(id))): return False
        
        try:
            query = f"""
                DELETE FROM emails_deleted WHERE id={id};       
            """
            
            self.cursor.execute(query)        
            self.connexao.commit()
            
            msg = "deleted".center(50, "_")
            print(msg)
            
        except:
            msg = 'Não foi possivel deletar o E-mail'.center(50, "*")
            print(msg)
    
    
banco = BancoDeDados()

banco.createTable()     

Bd_select_emails = [email[1] for email in banco.select() if banco.select() != []]

    
# ----------- Emails Pre inseridos -------------

def defaultSpan():    
    default = ['mailing@newfaceinfo.com.br', 
                'newsletter@investingmail.com', 
                'newsletter@allnations.com.br',
                'relacionamento@anhanguera.com',
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
                'no-reply@youtube.com'
                ]
    
    for email in default:    
        banco.inserirConteudo(email, "up Default Db")
        # print(email)
    

if (banco.select() == []):
     defaultSpan()






