from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Instancia import *



def main():
    ins = Instancia()
    mt_modelo, mt = ins.le_personagem('personagens\per1.txt')
    ins.monta_modelo(mt_modelo, mt)
   





































if __name__ == '__main__':
    main()
















