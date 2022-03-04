import os
import sys
import time
from pathlib import Path
import re

regex = re.compile(r'[0-3]?\d\/[0-1]?\d\/[12]\d\d\d', )

path = os.path.join(os.getcwd(),'arquivo/')
dir = sorted(os.listdir(path))


#================================================
# recebe um número de arquivo pelo input e 
# confirma se o numero é valido.

number_of_files = input("Passe um numero maior que zero:")
if number_of_files == '':
    number_of_files = -1
elif number_of_files <= "0":
    sys.exit()

#================================================
# recebe a data pelo input, confirma se a data
# está no formato correto e caso não haja data,
# faz com que funcione pegando todas as datas.

date_modification = input("data de Modificação no formato D/M/AAAA:")
teste_date = regex.findall(date_modification)
if date_modification == "":
    date = 1
else:
    try:
        date = str(teste_date[0])
    except:
        print("data invalida")
        sys.exit()

#================================================
# recebe o nome dos arquivos pelo input

new_name = input("Novo nome do arquivo:")

#================================================
# recebe o tamanho do arquiveo pelo input
# e caso o valor seja nulo, ele é trocado por um 
# valor muito alto que abranje todos os arquivos. 

file_size = input("Tamanho do arquivo em KBytes:")
if file_size == '':
    file_size = 10000000

#================================================
# função que passa os arquivos por todos os filtros,
# renomeia, e printa no terminal

def classification():
    menos = 0
    for index, files in enumerate(dir):

        #================================================
        # pega a data de modificação dos arquivos e 
        # converte os resultados para string.

        time_modification = os.path.getmtime(path+files)
        modification_time = time.gmtime(time_modification)
        result_modification= ("{}/{}/{}".format(modification_time.tm_mday,
        modification_time.tm_mon,modification_time.tm_year))
    
        #================================================
        # pega o tamanho dos arquivo em bytes e os converte
        # em KBytes.

        f_path = os.path.join(path, files)
        f_size = os.path.getsize(f_path)
        f_size_kb = (f_size / 1024)

        #================================================
        # confere se os arquivo terminam com .pdf,
        # a quantia de arquivo que ja passaram,
        # se a data é compativel com a data pedida
        # e se o tamanho do arquivo é compativel com o pedido.
        
        if (files.endswith(".pdf") and float(f_size_kb) <= float(file_size)):
            if result_modification == date or date_modification == "":                             
                if float(number_of_files) != float(index-menos):
                    
                    #====================================================
                    # printa no terminal o número e o tamanho do arquivo.
                        
                    print("========================================================")
                    print((index+1)-menos, result_modification)
                    print(f_size_kb, "Kb")
                
                    #=====================================================
                    # monta o nome dos arquivo e confere se o nome do arquivo 
                    # ja existe, caso exista o nome do arquivo não é alterado
                    # e printa uma mensagem avisando que não houve alteração
                    # se não, altera o nome do arquivo e printa no terminal.

                    result_new_name = new_name+str((index+1)-menos)+".pdf"
                    result_old_name = files
                    if result_new_name not in dir:
                        os.rename(path+result_old_name, path+result_new_name)
                        print("Você mudou o arquivo {} por {}".format(result_old_name, result_new_name))
                        print("========================================================")
                    else:
                        print("O arquivo {} já existe".format(result_old_name))
                        print("========================================================")
            
                else:
                    break
            else:
                menos += 1
        else:
            menos +=1
            
classification()
        
