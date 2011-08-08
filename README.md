Scrapy Crawler за MkWordNet
===========================
Овој проект е наменет за собирање на македонски текстови во дигитална форма.
Главната цел е да се соберат текстови на македонски јазик и да се направи
нешто слично на [Princeton Wordnet][PWN], или уште поблиску [MultiWordnet][MWN]

[PWN]: http://wordnetweb.princeton.edu/perl/webwn
[MWN]: http://multiwordnet.fbk.eu/english/home.php

Како да се уклучите
-------------------

За да го симнете проектов:

    $ git clone git://github.com/mkwordnet/crawler.git

Кој сака веднаш да се уклучи може да [форка][fork-a-repo]

[fork-a-repo]: http://help.github.com/fork-a-repo/

Идејата е во oва репо да се чуваат сите работи поврзани
со crawler-от, а во друго работите поврзани со NLP.

Кога ќе бидете сигурни дека сѐ работи како што треба пуштете [pull request][pr]

[pr]: http://help.github.com/send-pull-requests/



Поставување на околината
------------------------

1. Симнете го [scrapy-home][scrapy] од [scrapy-download][овде], или

    $ wget http://hg.scrapy.org/scrapy-0.12/archive/tip.tar.gz

    $ tar -zxvf tip.tar.gz

    $ cd scrapy-0-12...

    $ python setup.py install

2. couchdb

    $ apt-get install couchdb python-couchdb

3. симнете го проектот, одете во неговиот фолдер

    $ scrapy crawl dnevnik.com.mk




**P.S.**

Знам дека crawler е многу generic име, ама немаше опции. Не го користете името во други проекти :)
