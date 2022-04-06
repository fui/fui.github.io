# fui.github.io
![Build Status](https://github.com/fui/fui.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)

FUI sin nye hjemmeside!

## Kjøring
For å kjøre nettsiden lokalt, trenger du [ruby](https://www.ruby-lang.org/en/)
og `bundler`. Når du har installert ruby, kan du installere `bundler` med:

    gem install bundler

Du kan kjøre scriptet `run.sh` for å kjøre med riktig konfigurasjon. Om du på
død og liv ønsker å gjøre det selv, burde du kjøre:

    # Om du ikke har lastet ned alt ennå
    bundle install

    # For å starte siden lokalt
    jekyll serve --config _config.yml,_config_dev.yml

## Bidrag
Ønsker du å bidra? Send inn en PR (Pull Request) da vel! Er ingen krav til
innhold annet enn at ting skal kjøre.

## Tema
Vi benytter oss av en modifisert variant av
[HCZ Material Theme](http://jekyllthemes.org/themes/hcz-jekyll-material/).

[//]: # ( vim: set spl=nb: )
