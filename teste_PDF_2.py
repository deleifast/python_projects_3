from fpdf import FPDF

title = 'Relatório IMPRESSORA'

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 20)
        # Calcular ancho del texto (title) y establecer posición
        w = self.get_string_width(title) + 20
        self.set_x((210 - w) / 2)
        # Colores del marco, fondo y texto
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Grosor del marco (1 mm)
        self.set_line_width(0)
        # Titulo
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Salto de línea
        self.ln(10)

    def footer(self):
        # Posición a 1.5 cm desde abajo
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Color de texto en gris
        self.set_text_color(128)
        # Numero de pagina
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Color de fondo
        self.set_fill_color(200, 220, 255)
        # Titulo
        self.cell(0, 6, 'Loja %d %s' % (num, label), 0, 1, 'L', 1)
        # Salto de línea
        self.ln(4)

    def chapter_body(self, name):
        # Leer archivo de texto
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Emitir texto justificado
        self.multi_cell(0, 5, txt)
        # Salto de línea
        self.ln()
        # Mención en italic -cursiva-
        self.set_font('', 'I')
        self.cell(0, 5, '(fim)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

pdf = PDF()
pdf.set_title(title)
pdf.set_author('Vanderlei')
pdf.print_chapter(1, ' ' , 'relimp_loja01.txt')
pdf.print_chapter(2, ' ', 'relimp_loja02.txt')
pdf.print_chapter(3, ' ', 'relimp_loja03.txt')
pdf.print_chapter(4, ' ', 'relimp_loja04.txt')
pdf.print_chapter(6, ' ', 'relimp_loja06.txt')
pdf.print_chapter(7, ' ', 'relimp_loja07.txt')
pdf.print_chapter(8, ' ', 'relimp_loja08.txt')
pdf.print_chapter(9, ' ', 'relimp_loja09.txt')
pdf.print_chapter(10, ' ', 'relimp_loja10.txt')
pdf.print_chapter(11, ' ', 'relimp_loja11.txt')
pdf.print_chapter(12, ' ', 'relimp_loja12.txt')
pdf.print_chapter(13, ' ', 'relimp_loja13.txt')
pdf.print_chapter(14, ' ', 'relimp_loja14.txt')
pdf.print_chapter(15, ' ', 'relimp_loja15.txt')
pdf.print_chapter(16, ' ', 'relimp_loja16.txt')
pdf.print_chapter(17, ' ', 'relimp_loja17.txt')
pdf.print_chapter(18, ' ', 'relimp_loja18.txt')
pdf.print_chapter(19, ' ', 'relimp_loja19.txt')
pdf.print_chapter(20, ' ', 'relimp_loja20.txt')
pdf.print_chapter(21, ' ', 'relimp_loja21.txt')
pdf.print_chapter(22, ' ', 'relimp_loja22.txt')
pdf.print_chapter(23, ' ', 'relimp_loja23.txt')
pdf.print_chapter(24, ' ', 'relimp_loja24.txt')
pdf.print_chapter(25, ' ', 'relimp_loja25.txt')
pdf.print_chapter(26, ' ', 'relimp_loja26.txt')
pdf.print_chapter(27, ' ', 'relimp_loja27.txt')
pdf.print_chapter(28, ' ', 'relimp_loja28.txt')
pdf.print_chapter(29, ' ', 'relimp_loja29.txt')
pdf.print_chapter(30, ' ', 'relimp_loja30.txt')
pdf.print_chapter(31, ' ', 'relimp_loja31.txt')
pdf.print_chapter(32, ' ', 'relimp_loja32.txt')
pdf.print_chapter(33, ' ', 'relimp_loja33.txt')
pdf.print_chapter(34, ' ', 'relimp_loja34.txt')
pdf.print_chapter(35, ' ', 'relimp_loja35.txt')
pdf.print_chapter(36, ' ', 'relimp_loja36.txt')
pdf.print_chapter(37, ' ', 'relimp_loja37.txt')
pdf.print_chapter(38, ' ', 'relimp_loja38.txt')
pdf.print_chapter(39, ' ', 'relimp_loja39.txt')
pdf.print_chapter(40, ' ', 'relimp_loja40.txt')
pdf.print_chapter(41, ' ', 'relimp_loja41.txt')
pdf.print_chapter(42, ' ', 'relimp_loja42.txt')
pdf.print_chapter(43, ' ', 'relimp_loja43.txt')
pdf.print_chapter(44, ' ', 'relimp_loja44.txt')
pdf.print_chapter(45, ' ', 'relimp_loja45.txt')
pdf.print_chapter(46, ' ', 'relimp_loja46.txt')
pdf.print_chapter(47, ' ', 'relimp_loja47.txt')
pdf.print_chapter(48, ' ', 'relimp_loja48.txt')
pdf.print_chapter(49, ' ', 'relimp_loja49.txt')
pdf.print_chapter(52, ' ', 'relimp_loja52.txt')

pdf.output('lojas_printer.pdf', 'F')
