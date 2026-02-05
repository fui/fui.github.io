---
layout: page
title: Om FUI
permalink: /fagutvalget/
modeline: " vim: set spl=nb: "

semester: Vår 2026
members:
  - name: Thor Oscar Akre
    uioid: thoroak
  - name: Sapnil Aditya Ayman
    uioid: sapnilaa
  - name: Bashir Ahmad Atal
    uioid: bashiraa
  - name: Jonas Frømyr Evang
    uioid: jonasfev
  - name: Julie Grihamar
    uioid: juliegri
  - name: Hanne Alexandersdatter Hugem
    uioid: hanneahu
  - name: Vårin Sørlie
    uioid: vaarinso
  - name: Ka Thas
    uioid: kavint
  - name: Nha Benjamin Dang Tong
    uioid: nbtong

---

# Om FUI

---

{{ site.full_name }} (FUI) er informatikkstudentenes eget
organ, og skal fungere som et bindeledd mellom studentene, instituttet og
universitetet forøvrig. FUI har mellom 10 og 13 medlemmer, og møtes som regel
en gang i måneden. Medlemmene velges på et valgallmøte for instituttets
studenter i begynnelsen av hvert semester.

{{ site.title }} har noen faste oppgaver og arbeider ellers med saker studentene ved
instituttet ønsker å ta opp. Blant de faste oppgavene er plassfordeling på
lesesalene, administrasjon av bokskap, kursevaluering på nett og representasjon
i styrer og utvalg.

- {{ site.full_name }} jobber til enhver tid med
  å forbedre studiehverdagen til studentene ved instituttet.
- Kontakt oss hvis du har problemer i forbindelse med fag eller studier slik
  som urettferdige frister for obligatoriske oppgaver, dårlige kurs, eller kun
  detaljer rundt ved kurs som du ønsker å forbedre. Vi behandler alle saker
  anonymt med mindre du ønsker noe annet.
- Vi har medlemmer i de fleste styrer og utvalg, inkludert
  Undervisningsutvalget og Instituttstyret.
- Gjennom faste møter med undervisningsleder på instituttet får vi vite det
  meste som foregår på instituttet til en hver tid.
- Vi har medlemmer fra mange ulike studieprogrammer, og i mange ulike stadier
  i utdannelsen.
- Hvert semester utarbeider vi instituttets kursevalueringsrapport, og gjennom
  det arbeidet får vi full oversikt over kvaliteten på alle kurs hvor studenter
  har tatt seg tid til å bidra med sin mening.
  <br><br>

## Hovedvirksomhet

---

### Bokskap

FUI tilbyr bokskap som studenter kan ta i bruk. Skapene kan du finne fra 3. etasje til 9. etasje i Ole-Johan Dahls hus.

### Kursevaluering

Kursevaluering (KE) gjøres på slutten av hvert semester for alle kursene på
IFI. Det sendes ut invitasjoner til alle studentene påmeldt hvert kurs. En
oversikt over tilgjengelige skjemaer finnes på `nettskjema.no`

Nettskjema som brukes for å samle inn data er utviklet av
[USIT](http://usit.uio.no/). Dette systemet garanterer anonymitet for de som
svarer.
<br><br>

## Medlemmer

---

<table class="table">
  <thead>
    <tr>
      <th scope="col">Sentrale verv</th>
      <th scope="col">Innehaver</th>
      <th scope="col">UiO-ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Leder</td>
      <td>Liza Nagmadin Karim</td>
      <td><a href="https://personer.uio.no/lizana">lizana</a></td>
    </tr>
    <tr>
      <td>Nestleder</td>
      <td>Peter Hjelle Petersen-Øverleir</td>
      <td><a href="https://personer.uio.no/peterhp">peterhp</a></td>
    </tr>
    <tr>
      <td>Økonomiansvarlig</td>
      <td><i>Ubesatt</i></td>
      <td><a href="https://personer.uio.no/nobody">nobody</a></td>
    </tr>
  </tbody>
</table>

{{ site.title }}s øvrige medlemmer fra og med {{ page.semester }} er:

<ul>

{% assign sorted_members = page.members | sort: "name" %}

{% for member in sorted_members %}
  <li>{{ member.name }} (<a href="https://personer.uio.no/{{ member.uioid }}">{{ member.uioid }}</a>)</li>
{% endfor %}
</ul>
