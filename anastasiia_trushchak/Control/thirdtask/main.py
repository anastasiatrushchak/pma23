
class FrenchLocalizer:

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def localize(self, msg):


		return self.translations.get(msg, msg)

class SpanishLocalizer:


	def __init__(self):

		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def localize(self, msg):


		return self.translations.get(msg, msg)

class EnglishLocalizer:


	def localize(self, msg):
		return msg

if __name__ == "__main__":


	f = FrenchLocalizer()
	e = EnglishLocalizer()
	s = SpanishLocalizer()


	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))
