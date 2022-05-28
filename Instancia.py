# ************************************************
#   Instancia.py
#   Define a classe Instancia
#   Autor: Márcio Sarroglia Pinho
#       pinho@pucrs.br
# ************************************************

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import mat
from Ponto import *
from Poligonos import *
from Cores import *

""" Classe Instancia """
class Instancia:   
    def __init__(self):
        self.cores = {} #cores do personagens
        self.posicao = Ponto (0,0,0) 
        self.escala = Ponto (5,5,5)
        self.rotacao:float = 0.0
        self.modelo = []
        self.t = 0.0
    
    """ Imprime os valores de cada eixo do ponto """
    # Faz a impressao usando sobrecarga de funcao
    # https://www.educative.io/edpresso/what-is-method-overloading-in-python
    def imprime(self, msg=None):
        if msg is not None:
            pass 
        else:
            print ("Rotacao:", self.rotacao)

    """ Define o modelo a ser usada para a desenhar """
    def setModelo(self, func):
        self.modelo = func

    def Desenha(self):
        glPushMatrix()
        glTranslatef(self.posicao.x, self.posicao.y, 0)
        glRotatef(self.rotacao, 0, 0, 1)
        glScalef(self.escala.x, self.escala.y, self.escala.z)
        for i in self.modelo:
            if i.cor != 1:
                cor = self.cores[i.cor]
                glColor3f(cor.r,cor.b,cor.g) 
                i.desenhaQuadrado()
        glPopMatrix()

    def le_personagem(self, caminho):
        with open(caminho, 'r') as stream:
            arq = stream.readlines()
        mt_modelo = []
        linhas : int 
        colunas : int
        for ln in range(len(arq)):
            splt = arq[ln].split()
            if re.search('^#Cores$', splt[0]) is not None:
                num_cores =  int(arq[ln+1])
                for i,item in enumerate(arq[ln+2:ln+2+num_cores]):
                    strg = item.split()
                    cor_id = int(strg[0])
                    cor = Cor(r=int(strg[1]), g=int(strg[2]), b=int(strg[3]))
                    self.cores[cor_id] = cor
                
            if re.search('^#Objeto$', splt[0]) is not None:
                st = arq[ln+1].split()
                linhas, colunas = (int(st[0]), int(st[1]))
                for i, item in enumerate(arq[ln+2:ln+2+linhas]):
                    mt_modelo.append([int(x) for x in item.split()])
                
        
        return mt_modelo, [linhas, colunas]

    def monta_modelo(self, modelo, matriz):
        delta = 1
        for i in range(matriz[0]):
            for j in range(matriz[1]):
                p = Polygon()
                p.monta_quad(j-(matriz[1]/2), matriz[0]-i-(matriz[0]/2), delta)
                self.modelo.append(p)
                p.cor = modelo[i][j]
        
        

                



        
        
