---
layout: page
title: Referater
permalink: /reports
modeline: " vim: set spl=nb: "
---

# Referater

---

Alle referater fra før 2019 finner du [her](http://fui.ifi.uio.no/referater/).

<h1>Test1</h1>
{% for report in reports %}
  <h1>Test</h1>
  <h2>{{ report.name }} - {{ report.type }}</h2>
  <p>{{ report.content | markdownify }}</p>
{% endfor %}