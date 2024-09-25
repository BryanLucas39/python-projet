import os 
# para criar uma funçao em python, iremos utilizar o comando def(definição)

arquivo_original = input ("digite o nome do arquivo que será renomeado\n")
novo_arquivo = input("Digite o novo nome do arquivo\n")
def mudarNome(ar_or,nv_ar):    
    """
    A função mudarNome altera o nome de um arquivo que o usuário escolher
    o usuário deve inserir o nome original do arquivo e posteriormente, escolher 
    e inserir o nome do arquivo escolhido.
    args:
        ar_or (str): o nome original do arquivo.
        nv_ar (str): o novo nome do arquivo.
        returns
    """ 
    os.rename(ar_or,nv_ar)
    msg = "O nome do arquivo foi alterado com sucesso"
    return msg

rs= mudarNome(arquivo_original, novo_arquivo)
print (rs)