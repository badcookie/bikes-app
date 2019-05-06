#! /bin/bash

# TODO: Сделать общий скрипт для запуска и вынести на уровень выше
cd ../bikes \
    && pytest ../lecture_2 -v \
    && cd ../lecture_2
