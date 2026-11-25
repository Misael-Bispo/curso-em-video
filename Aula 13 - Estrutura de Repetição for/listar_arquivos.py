import os

# 1. Pega a pasta exata onde ESTE arquivo .py está localizado
pasta_atual = os.path.dirname(os.path.realpath(__file__))

# 2. Define o nome do arquivo TXT que será criado nessa mesma pasta
arquivo_saida = os.path.join(pasta_atual, 'lista_de_arquivos.txt')

# 3. Nome do próprio script para ignorar na lista
nome_do_script = os.path.basename(__file__)

# 4. Lê o conteúdo da pasta
itens = os.listdir(pasta_atual)

# 5. Cria e escreve no arquivo .txt
with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
    # Grava só o nome da pasta, sem o caminho completo do PC
    arquivo.write(f'--- LISTA DE ARQUIVOS EM: {os.path.basename(pasta_atual)} ---\n\n')
    
    for item in itens:
        # Ignora o próprio script e o arquivo txt gerado para não poluírem a lista
        if item != nome_do_script and item != 'lista_de_arquivos.txt':
            arquivo.write(f'{item}\n')

print('Lista criada com sucesso em "lista_de_arquivos.txt"!')
