from Cola import Cola
class Clinica:
    def __init__(self):
        self.dict = {}
    def agregarMedico(self,medico,pacientes):
        #self.dict[medico] = Cola()
        self.dict[medico] = pacientes

    def actualizarMedico(self,medico,cola):
        self.dict[medico] = cola
    def registrarPaciente(self,medico,paciente):
        mCola = self.dict[medico] #Saca cola de paciente medico
        mCola.enqueue(paciente) # Ingresa un nuevo paciente
        self.actualizarMedico(medico,mCola) #Actualiza la cola de pacientes del medico
    def siguiente(self,medico):
        mCola = self.dict[medico] #Saca cola de pacientes del medico
        paciente = mCola.dequeue() #Saca el siguiente paciente en la cola
        self.actualizaMedico(medico,mCola) #Actualiza la cola de pacientes del medico
        return paciente
    def test(self):
        cola = Cola() #Define médico y cola
        cola.enqueue("Pedro") #Ingresa un paciente en la cola de Pablo
        cola.enqueue("Marco") #Ingresa un paciente en la cola de Pablo
        self.agregarMedico("Pablo",cola) #Ingresa a Pablo y su cola de pacientes
        mCola = self.dict["Pablo"] #Saca cola de pacientes de Pablo
        print(mCola.dequeue()) #Saca el siguiente paciente en la cola
        print(mCola.dequeue()) #Saca el siguiente paciente en la cola
        
