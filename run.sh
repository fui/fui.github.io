#!/usr/bin/env bash

# Denne filen skal kun brukes ved utvikling

# Exit on error
set -e

bundle install
bundle exec jekyll serve --config _config.yml,_config_dev.yml
