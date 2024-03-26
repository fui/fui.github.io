---
layout: default
title: Processing workshop
permalink: /processing/
modeline: " vim: set spl=nb: "
---

# Processing workshop

2024-03-26 @ Limbo

FUI x Mikro

## Hva er Processing | Hensikt

> Processing is a flexible software sketchbook and a language for learning how to code.

Processing lar deg skrive kode som blir gjort om til former på et lerret (_og mye mye mer_).

Det finnes "dialekter" i Javascript og Python, mens den opprinnelige versjonen bygget på Java. Det er denne vi fil fokusere på, siden de fleste på ifi kjenner Java fra IN1010.

## How 2 get started

Man trenger Processing sitt utviklingsmiljø (IDE). Dette kan man enten:

1. Laste ned gratis [på nettsiden til Processing](https://processing.org/download), eller
1. Nå via ifi sine RHEL-maskiner.

## Strukturen til et Processing-program

På samme måte som at alle Java-programmer trenger å ha en main-metode, trenger alle Processing-programmer å ha en `setup()` og `draw()`.

## `void setup()`

Setup-prosedyren vil kjøre **én** gang, hver gang du starter programmet ditt.
Her vil man typsik sette størrelsen på lerrettet og initialisere globale variabler.

_Demokoden under er ikke testkompilert, ta den med en klype salt._

```java
List<Integer> xCoordinates;
final int nBoxes = 10;
void setup() {
    size(400, 400);
    xCoordinates = new ArrayList<>();
    for(int i = 0; i < nBoxes; i++) {
        xCoordinates.add(0);
    }
}
```

## `void draw()`

Draw-prosedyren kjører for hver _frame_, altså hver gang programmet oppdateres. Det er her man har selve "innholdet" i progarmmet.

```java
void draw() {
    for(int i = 0; i < xCoordinates.size(); i++) {
        // Hent posisjonsn
        final int posX = xCoordinates.get(i);
        // Tegn en firkant på x-posisjonen
        rect(posX, i * 10, 10, 10);
        // Øk størrelsen slik at man ikke tegner en boks på samme sted i hver frame
        xCoordinates.set(i, posX + 10);
    }
}
```

## Prosedyrer for å komme i gang - `hello Processing`

Det finnes meget god dokumentasjon [på de offisielle nettsidene](https://processing.org/reference). Dette er en oversikt over alt Processing har utover standard Java. All standard Java er gyldig\*, samt denne ekstra funksjonaliteten.

Under følger en oversikt over de viktigste grunnleggende prosedyrene.

### Firkant - `rect(x, y, høyde, bredde)`

For å tegne en firkant kan man bruke `rect(x, y, høyde, bredde);`

### Farge - `fill(r, g, b)`

For å endre hvilken farge som er aktiv kan man ta `fill(r, g, b)`.

Så hvis man vil ha rød farge tar men `rgb(255, 0, 0)`.

Det er også mulig å bare gi den ett argument, i så fall vil den være en grånyanse mellom hvitt og svart. `fill(0)` setter aktiv farge til svart, mens `fill(255)` setter fargen til hvit.

### Størrelse på lerrettet - `size(høyde, bredde)`

For å sette størrelse på lerrettet må man bruke `size(høyde, bredde)`-prosedyren. Denne funker _kun_ i `setup()` (man kan ikke resize lerretet mens programmet kjører)

Typisk er det fint å ha et kvadrat à størrelse 400-800 avhengig av hva slags skjerm man bruker.

```java
void setup() {
    size(400, 400);
}
```

### Få et tilfeldig tall - `rand(spenn)`

Dersom man ønsker å få et vilkårlig tall kan man ta `rand(spenn)`.
Så dersom man har en boks og så vil man at den skal hoppe "litt", kan man oppdatere posisjonen med f.x. `rand(10)`, og få tilbake en verdi mellom 0 og 10.

### Innebygde variabler - `height` og `width`

Kjekt å vite at Processing tilgjengegliggjør variabler for størrelsen på lerretet.

Man kan bruke tallverdiene fra `height` og `width` direkte globalt i programmet, som er praktisk om man har en for-løkke som skal stoppe ved kanten av lerrettet.

## Programmet er skrevet - hvordan kjøre?

### Play-button

Øverst til venstre i Processing-IDEen vil man se en play-knapp. Ved å trykke på denne vil man starte programmet. Det vil komme opp i en boks midt på skjermen by default.

### Snareveier

Det er også mulig å emulere et trykk på play-knappen ved å taste inn `CTRL+R`. CMD for CTRL på Mac.

### Formattering

Et protip er å ta `CTRL+T`. Dette for kjøre automatisk formattering av programmet du har skrevet.
Dersom formatteringen ikke funker er det trolig en syntaksfeil i programmet, som vil si at det uansett ikke ville ha fungert å kjøre det. Derfor kan det være gunstig å alltid formattere før man kjører (det går mye raskere å formattere enn å kompilere osv)

## Further reading

Dersom du syntes Processing var gøy er det masse Nice ressurser på nettet.

Imo er [`The coding train`](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw) på Youtube en av de beste. Han progger masse kult i processing og har en veldig pedagogisk tilnærming til hvordan han forklarer det han gjør. Skylder ham en ikke uvesentlig del av ifi-bacheloren :D

Ellers er det bare å la fantasien løpe løpsk og lese dokumentasjon fortløpene for å finne ut hvordan man kan gjøre det man ønsker å gjøre.
