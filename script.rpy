# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define s = Character("[mainname]", color="#ffffff")
define b = Character('...', color="#ffffff")
define m = Character('Мама', color="#ffffff")
define c = Character('Странный кот', color="#ffffff")
define t = Character('Учительница Лей', color="#ffffff")
define c_n = Character("[cname]", color="#ffffff")

# Музыка и звуки
define audio.alarm = "audio/alarm.mp3"
define audio.door = "audio/door.mp3"
define audio.schoolbell = "audio/schoolbell.mp3"
define audio.heart = "audio/heart.mp3"


#  Первый день:
label start:

    $ mainname = renpy.input("Как вас зовут?")

    play sound alarm

    scene black with vpunch

    b "БЗЗЗЗЗЗЗЗЗЗ!!!!"
    b "БЗЗЗЗЗЗЗЗЗЗ!!!!"

    stop sound

    scene morning room
    with fade

    "{i}Да встаю я, встаю уже!{w} Как же сильно болит голова...{i}"

    play sound door
    b "Тук-тук!"
    stop sound
    b "[mainname], ты проснулся?"
    "{i}Точно! Сегодня первый день после каникул.{i}"

    
    show mom
    m "[mainname], утречка!"
    "Привет, мам."
    m "Завтрак уже готов, поэтому быстрее спускайся и поедай, пока ничего не остыло."
    "Спасибо, мам."
    hide mom
    "{i}Как всегда она слишком заботлива...{i}"
    "{i}Пора собираться в школу...{i}"
    scene black with fade
    b "..."
    scene saitoru
    "{i}Первый день, а я уже устал от этой формы.{i}"

    scene street with fade
    "{i}Надо не забыть после шко...{i}"
    b "Мяу..."
    "{i}Котенок?{i}"
    scene street with vpunch
    show cat scream at right:
        yalign 0.7
    b "МЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯУ!!!"

    menu:
        "{i}И что мне с ним делать...{i}"

        "{b}Попробовать сдружиться с котом.{b}":
            jump zabrat_cota
            
        "{b}Пройти мимо.{b}":
            jump cat_ne_nuzhen
    
    return

label zabrat_cota:
    hide cat scream
    "Ну что ты разорался тут?"
    show cat calm at right:
        yalign 0.7
    c "Мяу-мяу..."
    "Ну и дурной ты..."
    "Придется тебя с собой забрать...Главное, чтобы тебя не заметили."
    c "Мяу..."
    hide cat calm

    scene school with fade
    play sound schoolbell
    "Черт! Я опоздал на урок!"
    stop sound
    "{i}Куда же тебя спрятать...{i}"
    show cat calm at right:
        yalign 0.7
    c "Мяу..."
    "Точно. Тебя надо назвать как-нибудь."
    $ cname = renpy.input("Думаю тебе подойдет... (Введите имя)")
    "Прекрасно, будешь [cname]!"
    hide cat calm
    "Думаю, потерпишь пока у нас в кабинете технарей. Они посещают клуб лишь после уроков."
    show cat calm at right:
        yalign 0.7
    cname "Мяу!"
    hide cat calm
    "Думаю, что это да."
    scene old room with fade
    show cat calm at right:
        yalign 0.7
    cname "Мяу!"
    "Пока-пока!."

    scene school with fade
    "{i}Первый день, а я уже успел прогулять урок...{i}"
    scene school with vpunch
    b "БАМ!!"
    show teacher at right
    t "[mainname], первый день и ты уже опаздываешь? Так и еще не смотришь под глаза.{w} Мне стоит поговорить с твоей мамой."
    "{i}Какой же я везунчик...{i}"
    "Извините, Мисс Лей, просто по дор..."
    t "[mainname], ни слова больше! Ты и на прошлом семестре часто прогуливал учебу. Понимаю, что ты один из лучших учеников школы, но нельзя так халатно относиться к учебе."
    t "Как бы этого не хотелось, но ты наказан!"
    "{i}Только не это...{i}"
    t "Знакомься, это наша новая ученица Мирай Кумихо."
    scene first meet
    play sound heart
    b "Тук-тук..."
    b "{i}Мирай Кумихо...{i}"
    stop sound
    return

label cat_ne_nuzhen:
    "Странные нынче коты..."
    return