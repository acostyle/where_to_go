# Where to go

"Where to go" is a web application where points of interest are marked on an interactive map of Moscow. By clicking on them, you can see more information, photos, and contacts. 
You can check this out here: [Link](http://acostyle.pythonanywhere.com)

### How to run
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip3 install -r requirements.txt
```
Create environment variables:
```
SECRET_KEY=[django secret key]
DEBUG=[True or False]
```
Run the Django development server:
```
python manage.py runserver
```
Open https://127.0.0.1:8000 in your browser.

### How to edit data or fill the app database with naew data using the admin site
- Open the admin site at https://127.0.0.1:8000/admin/places/place/
- Enter admin username and password (available on request)
- Click on "Places"
- Click on "Add place" in the upper right corner or choose an existing place
- Fill/edit the fields, upload photos
- Drug'n'drop the photo's fields to choose the order
- Click "Save"

### How to add new places using a console command
- What the json file should look like
```
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",

    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. </p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```
- Run the following command
```
python3 manage.py load_place [link to the new place JSON file]
```
