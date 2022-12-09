# О проекте

Парсинг игр с сайта: https://store.steampowered.com/

Игры по каждому запросу на первых 3-ех страницах (150 результатов)
Из каждой конкретной игры, достаем:
  

* Название
* Категорию (весь путь, за исключением Все игры и самого названия игры)
* Число всех обзоров и общая оценка
* Дата выхода
* Разработчик
* Метки (тэги) игры
* Цена
* Доступные платформы

Происходит фильтрация игр, выпущенных только после 2000 года

# Как запустить проект


#### Склонируйте проект из гитхаба
#### Запустите виртуальное окружение проекта
#### Установите scrapy

<code>pip install Scrapy</code>


[https://docs.scrapy.org/en/latest/intro/install.html
]()

#### term ='' в кавычках можно поставить свой запрос

В папке по очереди запустить в терминале
<br>
<code> scrapy crawl steam_games -a term='инди' -O indy_steam_game.json</code>
<br>
<code> scrapy crawl steam_games -a term='стратегии' -O strategy_steam_game.json</code>
<br>
<code> scrapy crawl steam_games -a term='minecraft' -O minecraft_steam_game.json</code>

<br>
<br>
<br>

