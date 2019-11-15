## Samlet offentlige grensnitt for klassene til prosjektoppgave i IN1000, høst 2019
#
# * Denne teksten fjernes og klassene fordeles på filer før implementasjon*
# Grensesnittet er dokumentert i samme standard format som læreboken benytter.
# Det finnes mange alternative formater og verktøy for dokumentasjon av
# programmer, og en arbeidsplass eller kunde vil gjerne ha en standard man
# må tilpasse seg.
# Merk at informasjonen som er oppgitt her tilsvarer klassenes *offentlige
# grensesnitt* (public interface) - den informasjonen brukerne av klassen har
# behov for. Du bestemmer *implementasjonen* - og vil kunne endre den i
# ettertiden uten at programmer som bruker klassene påvirkes.


## Klasse for representasjon av et datasenter
#
class Datasenter:

	## Oppretter et datasenter
	#
	def __init__(self):
		pass

	## Leser inn data om en regneklynge fra fil og legger
	# den til i ordboken
	# @param filnavn filene der dataene for regneklyngen ligger
	def lesInnRegneklynge(self, filnavn):
		pass

	## Skriver ut informasjon om alle regneklyngene
	#
	def skrivUtAlleRegneklynger(self): 
		pass

	## Skriver ut informasjon om en spesifikk regeklynge
	# @param navn navnet på regnekyngen
	def skrivUtRegneklynge(self, navn):
		pass

## Klasse for representasjon av regneklynge i et datasenter.
#
class Regneklynge:
	## Oppretter en regneklynge og setter maks antall
	# det er plass til i et rack
	# @param noderPerRack max antall noder per rack
	def __init__(self, noderPerRack):
		pass

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
		pass

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
		pass

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		pass

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		pass

## Klasse for representasjon av racks i en regneklynge.
#
class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
	def __init__(self):
		pass

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		pass

	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		pass

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		pass

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		pass

## Klasse for representasjon av noder i en regneklynge
#
class Node:
	## Oppretter en node med gitt minne-storrelse og antall prosessorer
	#  @param minne GB minne i den nye noden
	#  @param antPros antall prosessorer i den nye noden
	def __init__(self, minne, antPros):
		pass

	## Henter antall prosessorer i noden
	#  @return antall prosessorer i noden
	def antProsessorer(self):
		pass

	## Sjekker om noden har tilstrekkelig minne for et program
	#  @param paakrevdMinne GB minne som kreves for programmet
	#  @return True hvis noden har minst så mye minne
	def nokMinne(self, paakrevdMinne):
		pass
