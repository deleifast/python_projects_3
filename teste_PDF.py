# Python program to convert 
# text file to pdf file 
  
  
from fpdf import FPDF 
   
# save FPDF() class into  
# a variable pdf 
pdf = FPDF()    
   
# Add a page 
pdf.add_page() 
   
# set style and size of font  
# that you want in the pdf 
pdf.set_font("Arial", size = 5) 
  
# open the text file in read mode 
f = open("relsat_loja01.txt", "r") 
  
# insert the texts in pdf 
for x in f: 
    pdf.cell(150, 10, txt = x, ln = 1, align = 'C') 
   
# save the pdf with name .pdf 
pdf.output("mygfg.pdf") 
