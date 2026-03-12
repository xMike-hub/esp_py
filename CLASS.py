
class Cane:
     
     def __init__ (self, nome_scelto):
          self.nome = nome_scelto


     def abbaia(self):
      print(f"{self.nome} dice: baubau")

mio_cane = Cane("fido")

cane_del_vicino = Cane("rex")

cane_della_nonna = Cane("Pupo")

mio_cane.abbaia()

cane_del_vicino.abbaia()

cane_della_nonna.abbaia()
