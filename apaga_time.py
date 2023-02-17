textos = []
f = open("texto_limpo.txt", "w+")


with open( 'Minicamp - Prof  Guilherme Assis - aula teórica - 1.1 (português_ASR) .txt', 'r+',encoding="utf-8")as arquivo:
            texto = arquivo.readlines()
            for linha in texto :
                        if linha != '\n':
                                    try:
                                                int(linha[0])
                                    except:
                                                f.writelines(linha)                                                            
            arquivo.close()





from fpdf import FPDF 
   
pdf = FPDF()    
   
pdf.add_page() 
   
pdf.set_font("Arial", size = 15) 
f = open("texto_limpo.txt", "r") 
for x in f: 
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
   
pdf.output("texto_limpo.pdf")
f.close()
print('fim')
