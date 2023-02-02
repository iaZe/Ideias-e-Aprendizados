class Aluno:
    nome: None
    dataNasc = ""
    curso = None
    nota1Bimestre = 0.0
    nota2Bimestre = 0.0
    provaFinal = 0.0
    situacao = None

def __init__(self, nome, dataNasc, curso, nota1Bimestre, nota2Bimestre, provaFinal, situacao):
    self.setNome(nome)
    self.setDataNasc(dataNasc)
    self.setCurso(curso)
    self.setNota1Bimestre(nota1Bimestre)
    self.setNota2Bimestre(nota2Bimestre)
    self.setProvaFinal(provaFinal)
    self.setSituacao(situacao)


def setNome(self, nome, nomeAluno):
    nome == nomeAluno
    if nome is None:
     nome = "Não informado"
    else:
     self.nome = nome 

def getNome(self):
    return self.nome

def setNota1Bimestre(self, nota1Bimestre):
    if type(nota1Bimestre) != float:
     self.nota1Bimestre = 0.0
    elif nota1Bimestre < 0:
     self.nota1Bimestre= 0
    else:
     self.nota1Bimestre = nota1Bimestre

def getNota1Bimestre(self):
    return self.nota1Bimestre   


def setNota2Bimestre(self, nota2Bimestre):
    if type(nota2Bimestre) != float:
     self.nota2Bimestre = 0.0
    elif nota2Bimestre < 0:
     self.nota2Bimestre= 0
    else:
     self.nota2Bimestre = nota2Bimestre

def getNota2Bimestre(self):
    return self.nota2Bimestre


def setProvaFinal(self, provaFinal):
    if type(provaFinal) != float:
     self.provaFinal = 0.0
    elif provaFinal < 0:
     self.provaFinal= 0
    else:
     self.provaFinal = provaFinal

def getprovaFinal(self):
    return self.provaFinal 


def setCurso(self, curso):
    if curso is None:
     curso = "Não informado"
    else:
     self.curso = curso

def getCurso(self):
    return self.curso

def setSituacao(self, situacao):
    if situacao is None:
     situacao = "indefinida"
    else:
     self.situacao = situacao

def getSituacao(self):
    return self.situacao


def setMediaParcial(self, mediaParcial):
    self.mediaParcial = mediaParcial

def getMediaParcial(self):
    return self.mediaParcial

def CalcularMediaParcial(self):
    valorMediaParcial = (self.getNota1Bimestre+self.getNota2Bimestre)/2
    self.setMediaParcial(valorMediaParcial)
    return valorMediaParcial

def ValidarProvaFinal (self):
    if self.getMediaParcial > 6.9:
        self.setprovaFinal = 0
    else:
        self.setprovaFinal = self.setprovaFinal
        return self.getprovaFinal 

def setMediaFinal(self, mediaFinal):
    self.mediaFinal = mediaFinal

def getMediaFinal(self):
    return self.mediaFinal

def CalcularMediaFinal(self):
    if self.getMediaParcial > 6.9:
        valorMediaFinal = self.getMediaParcial
    else:
        valorMediaFinal = self.getprovaFinal
    self.setMediaFinal(valorMediaFinal)
    return valorMediaFinal

def AnalisarSituacao(self):
    if self.getMediaFinal >= 6:
        AnalisarSituacao = "Aprovado"
    else:
        AnalisarSituacao = "Reprovado"
    self.setSituacao(AnalisarSituacao)
    return AnalisarSituacao

# def setDataNasc(self, dataNasc):

if __name__ == "__main__":
    nomeAluno = ""
    curso = ""
    nota1 = 0.0
    nota2 = 0.0
    nomeAluno = input("Digite o nome do aluno")
    setNome(nomeAluno)
    print()
    nota1.getNota1Bimestre(float(input("Informe a nota do 1° Bimestre")))
    print()
    nota2.getNota2Bimestre(float(input("Informe a nota do 2° Bimestre")))
    print()
    input("Media parcial:", getMediaParcial)
    input("Media final:", getMediaFinal)
    input("Situação: ", getSituacao)
