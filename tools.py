import os, re

def removePastaVazia(diretorio):
    caminho = os.listdir(diretorio)
    for pasta in caminho:
        try:
            caminho_completo= os.path.join(diretorio,pasta)
            os.rmdir(caminho_completo)
        except:
            continue
        
        
def clearCharacters(string): 
    if type(string) == str:
        clear = re.sub(r"[\<\>\:\\\/\|\?\@]","__", string)
        return clear
    
    return False
    

    
    
    