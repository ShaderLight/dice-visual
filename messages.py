class Msg():
    def __init__(self,language):
        if language == "EN":
            self.load_EN()
        elif language == "PL":
            self.load_PL()

    def load_EN(self):
        self.msg_1 = "How many dice ? "
        self.msg_2 = "How many rolls ? "
        self.msg_3 = "How many sides on die "
        self.msg_4 = "Result"
        self.msg_5 = "Frequency of values"

    def load_PL(self):
        self.msg_1 = "Ile kości ? "
        self.msg_2 = "Ile rzutów ? "
        self.msg_3 = "Ile ścian na kości "
        self.msg_4 = "Wynik"
        self.msg_5 = "Częstotliwość występowania wartości"
