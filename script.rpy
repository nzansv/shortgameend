# Персонажи.
define s = Character("[mainname]", color="#ffffff")
define b = Character('...', color="#ffffff")
define m = Character('Мама', color="#ffffff")
define mi = Character('Мирай', color="#ffffff")
define c = Character('Странный кот', color="#ffffff")
define t = Character('Учительница Лей', color="#ffffff")
define c_n = Character("[cname]", color="#ffffff")

# Музыка и звуки
define audio.alarm = "audio/alarm.mp3"
define audio.door = "audio/door.mp3"
define audio.schoolbell = "audio/schoolbell.mp3"
define audio.heart = "audio/heart.mp3"
define audio.zip = "audio/zip.mp3"
define audio.classroom = "audio/classroom.mp3"


#  Первый день:
label start:
    stop music fadeout 1.0

    $ mainname = renpy.input("Как вас зовут?")

    play sound alarm

    scene black with vpunch

    b "БЗЗЗЗЗЗЗЗЗЗ!!!!"

    stop sound fadeout 1.0

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
    play sound zip
    b "..."
    stop sound fadeout 1.0
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
# Дефолт концовка первого дня
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
    t "Знакомься, это наша новая ученица Мирай Кумихо. И ты должен показать ей нашу шко..."
    scene first meet
    play sound heart
    b "Тук-тук..."
    b "{i}Мирай Кумихо...{i}"
    stop sound
    scene black with fade
    menu:
        "{i}Как мне быть...{i}"

        "{b}Согласиться с наказанием и показать школу Мирай.{b}":
            jump show_school

        "{b}Отмазаться.{b}":
            jump medical

        "{b}Отказаться.{b}":
            jump deny_to_teacher
    return

label medical:
    scene school with fade
    show teacher at right
    "Мисс Лей, я чувствую себя неважно. Мне стоит сходить в медпункт."
    t "[mainname], ты безнадежен..."
    scene med with fade
    "{i}Теперь и лгать медсестре...{i}"
    b "[mainname], солнышко, что случилось?"
    "{i}Что с ней не так...{i}"
    b "Давай готовься к уколу..."
    "Нет, погодите, мисс Танако!"
    scene med with vpunch
    show cat scream at right:
        yalign 0.7
    b "Хихиххи, [mainname], что тебя беспокоит?"
    "ЧЁЁЁЁЁЁ%%%%%%%%%%%%%%?7????"
    hide cat scream
    show cat calm at right:
        yalign 0.7
    cname ""
    return

label cat_ne_nuzhen:
    "Странные нынче коты..."
    play sound schoolbell
    scene black with fade
    scene school room with fade
    "{i}Обычный день обычного старшеклассника. Ничего нового...{i}"
    stop sound fadeout 1.0
    scene night room with fade
    "{i}...{i}"
    return

label show_school:
    scene first meet with fade
    "Меня зовут [mainname] Акиро и я ученик класса 3-1."
    mi "О, я тоже перевелась в этот класс. Получается сегодня прогуляем геометрию и английский."
    "{i}Почему она так знакомо выглядит...{i}"
    mi "Аууу??? Мы пойдем?"
    "Ой, пошли. Начнем со школьного двора."
    scene school backyard with fade
    show era at right:
    mi "У вас тут так красиво!"
    "Странно, что ты удивляешься обычному школьному двору."
    show era disp at right
    mi "Ну знаешь, в моей прошлой школе всё было мрачно и серо. Да и кто-то впервые со мной прогуливается по школьному двору..."
    "Прости, я не знал."
    show era at right
    mi "Глупости! Ты чего извиняешься?"
    scene school backyard with vpunch
    show cat calm at right:
        yalign 0.7
    cname "Мяу-мяу"
    "Я же тебя запер в кабинете... Да как ты..."
    cname "А ключи запасные были-то на столе."
    scene school backyard with vpunch
    "ЧЁЁЁЁЁЁ%%%%%%%%%%%%%%?7????"
    show eru afraid at right:
        yalign 0.54
    "Он что-то сказал или мне это мерещится?"
    hide eru afraid at right
    show cat calm at right:
        yalign 0.7
    cname "Голубчики, я всего-то лишь говорящий кот, или какое имя ты там мне придумал... [cname]... Ну и имя..."
    "Какой наглый..."
    hide cat calm
    show eru afraid at right:
         yalign 0.54
    "Так значит ты волшебный..."
    hide eru afraid at right
    show cat calm at right:
        yalign 0.7
    cname "А все мы втроем знакомы неспроста, дорогие мои. Будьте бдительны и внимательнее."
    scene black with fade
    b "..."
    scene school room with fade
    "{i}Что произошло...{i}"
    show eru afraid at right:
         yalign 0.54
    "Этот кот каким-то образом отправил нас в класс..."
    "Да что происходит..."
    hide eru afraid at right
    show teacher at right
    t "Мирай и [mainname], никаких разговоров во время уроков!"
    play sound schoolbell
    scene black with fade
    scene school room with fade
    "{i}Мирай выбежала из класса.Что за странный день...{i}"
    stop sound fadeout 1.0
    scene night room with fade
    "{i}...{i}"
    return
label deny_to_teacher:
    scene school with fade
    show teacher at right
    "Извиняюсь, сегодня у меня важная контрольная по геометрии. Мне надо готовиться."
    t "[mainname], ты безнадежен..."
    play sound schoolbell
    scene black with fade
    scene school room with fade
    "{i}Обычный день обычного старшеклассника. Ничего нового... Но откуда такое странное чувство внутри.{i}"
    stop sound fadeout 1.0
    scene night room with fade
    "{i}...{i}"

    return