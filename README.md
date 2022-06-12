# Spotify to VK

**Показывает текущую проигрываемую песню в статус-баре ВК.**  
(*Display your current listen to a song from Spotify in the VK status.*)

## Установка (Installation)

1. **Клонируем репозиторий** (*Clone repository*)

    ```bash
    git clone https://github.com/TheDarkFireDesu/spoty-to-vk.git
    ```

2. **Переходим в папку с репозиторием** (*Go to "spoty-to-vk" folder*)

    ```bash
    cd spoty-to-vk
    ```

3. **Установливаем зависимости при помощью pip** (*Install libraries using pip*)

    ```bash
    pip install -r requirements.txt
    ```

## Настройка (Setting up)

1. **Заполним файл конфигурации settings.py** (*Fill in the config*)

    ```python
    class Settings:
        MAIN_STATUS = ""
        STATUS = "{artist} — {track}"
        CLIENT_ID = ""
        CLIENT_SECRET = ""
        REDIRECT_URI = "http://localhost:8888/callback"
        USERNAME = ""
        SCOPE = "user-read-playback-state user-library-read"
        VK_TOKEN= ""
        LANGUAGE = "RUS"
    ```

2. **Заполним строку MAIN_STATUS**

    В строку MAIN_STATUS пишем тот текст, который хотим видеть во время простоя программы.

3. **Заполним строку STATUS**

    Ее можно оставить, как есть, но если прям хочется что-то изменить, то имя артиста - *{artist}*, название песни - *{track}*, альбом - *{album}*.

4. **Получение Clien ID и Secret ID**

    - Переходим на сайт Spotify Developer: [тык](https://developer.spotify.com/dashboard/applications)
    - Заходим в свой профиль Spotify.
    - Нажимаем на кнопку: **CREATE AN APP**.
    - Вводим любое название и описание, затем ставим галочку (*можно и прочитать что-там*), потом далее.
    - В левой части под названием будет Client ID - его записываем в строку CLIENT_ID.
    - Нажав кнопку **SHOW SECRET ID**, получим Secret ID - его записываем в строку SECRET ID.
    - Нажав кнопку **EDIT SETTINGS**, в графе **REDIRECT URIs** вписываем <http://localhost:8888/callback> и нажимаем **ADD**.
    - Сохраняем, нажимая кнопку **SAVE**.

5. **Заполним строку REDIRECT_URI**

    Лучше оставить ее, как есть, потому что оно и так работает. А дивиз по жизни: "Работает? Не трожь".

6. **Заполним строку USERNAME**

    Самое легкое, что тут есть после строки STATUS. Сюда вписываем имя своего аккаунт Spotify.

7. **Заполним строку SCOPE**

    Ее тоже лучше оставить, кто хочет разобраться с этим, сюда: [тык](https://developer.spotify.com/documentation/general/guides/authorization/scopes/).

8. **Заполним строку VK_TOKEN**

    - Переходим по этой ссылке: [тык](https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1)
    - В поисковой строке нужный нам токен лежит после строки ```access_token=``` и заканчивается ```&expiries_in```.  
    Получается что-то аля ```...access_token=<TOKEN>&expiries_in...```.
    - Вписываем искомый токен в наш конфигурационный файл.

9. **Заполним строку LANGUAGE**

    Строка, в которую вписываем наш язык. Список всех языков [тут](https://www.loc.gov/standards/iso639-2/php/code_list.php). Лично мне подошли коды из двух знаков: RU, EN и так далее.

## Запуск (Start)

```bash
python main.py
```

## ЧаВО (FAQ)

1. **Библиотеки** (*Used libraries*)
    - vk_api
        - [github.com](https://github.com/python273/vk_api)
    - spotipy
        - [github.com](https://github.com/plamere/spotipy)

2. **Отличия от оригинала** (Diffences from original)
    - Можно выбрать язык.
    - Отсутствие Colorama по причине: «А зачем, если можно без этого?».
    - Ну, и все, пока что.

3. **Авторство** (*Credits*)
    - [Feschenko](https://github.com/feschenko) - автор оригинала.
    - [MazZz3R](https://github.com/mazZz3R) - автор оригинала.
    - [d1rknwh1te3](https://github.com/d1rknwh1te3) - скромнейший форкнувший чел.
