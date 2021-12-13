# Персонажи.
define s = Character("[mainname]", color="#ffffff")
define b = Character('...', color="#ffffff")
define m = Character('Мама', color="#ffffff")
define mi = Character('Мирай', color="#e8685f")
define c = Character('Странный кот', color="#ff9933")
define t = Character('Учительница Рей', color="#ffffff")
define c_n = Character("[cname]", color="#ff9933")

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

    mainname "{i}Да встаю я, встаю уже!{w} Как же сильно болит голова...{i}"

    play sound door
    b "Тук-тук!"
    stop sound
    b "[mainname], ты проснулся?"
    mainname "{i}Точно! Сегодня первый день после каникул.{i}"


    show mom
    m "[mainname], утречка!"
    mainname "Привет, мам."
    m "Завтрак уже готов, поэтому быстрее спускайся и поедай, пока ничего не остыло."
    mainname "Спасибо, мам."
    hide mom
    mainname "{i}Как всегда она слишком заботлива...{i}"
    mainname "{i}Пора собираться в школу...{i}"
    scene black with fade
    play sound zip
    b "..."
    stop sound fadeout 1.0
    scene saitoru
    mainname "{i}Первый день, а я уже устал от этой формы.{i}"

    scene street with fade
    mainname "{i}Надо не забыть после шко...{i}"
    b "Мяу..."
    mainname "{i}Котенок?{i}"
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
    mainname "Ну что ты разорался тут?"
    show cat calm at right:
        yalign 0.7
    c "Мяу-мяу..."
    mainname "Ну и дурной ты..."
    mainname "Придется тебя с собой забрать...Главное, чтобы тебя не заметили."
    c "Мяу..."
    hide cat calm

    scene school with fade
    play sound schoolbell
    mainname "Черт! Я опоздал на урок!"
    stop sound
    mainname "{i}Куда же тебя спрятать...{i}"
    show cat calm at right:
        yalign 0.7
    c "Мяу..."
    mainname "Точно. Тебя надо назвать как-нибудь."
    $ cname = renpy.input("Думаю тебе подойдет... (Введите имя)")
    mainname "Прекрасно, будешь [cname]!"
    hide cat calm
    mainname "Думаю, потерпишь пока у нас в кабинете технарей. Они посещают клуб лишь после уроков."
    show cat calm at right:
        yalign 0.7
    cname "Мяу!"
    hide cat calm
    mainname "Думаю, что это да."
    scene old room with fade
    show cat calm at right:
        yalign 0.7
    cname "Мяу!"
    mainname "Пока-пока!."

    scene school with fade
    "{i}Первый день, а я уже успел прогулять урок...{i}"
    scene school with vpunch
    b "БАМ!!"
    show teacher at right
    t "[mainname], первый день и ты уже опаздываешь? Так и еще не смотришь под глаза.{w} Мне стоит поговорить с твоей мамой."
    mainname "{i}Какой же я везунчик...{i}"
    mainname "Извините, Мисс Лей, просто по дор..."
    t "[mainname], ни слова больше! Ты и на прошлом семестре часто прогуливал учебу. Понимаю, что ты один из лучших учеников школы, но нельзя так халатно относиться к учебе."
    t "Как бы этого не хотелось, но ты наказан!"
    mainname "{i}Только не это...{i}"
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
    mainname "{i}Теперь и лгать медсестре...{i}"
    b "[mainname], солнышко, что случилось?"
    "{i}Что с ней не так...{i}"
    b "Давай готовься к уколу..."
    mainname "Нет, погодите, мисс Танако!"
    scene med with vpunch
    show cat scream at right:
        yalign 0.7
    b "Хихиххи, [mainname], что тебя беспокоит?"
    mainname "ЧЁЁЁЁЁЁ%%%%%%%%%%%%%%?7????"
    hide cat scream
    show cat calm at right:
        yalign 0.7
    cname ""
    return

label cat_ne_nuzhen:
    mainname "Странные нынче коты..."
    play sound schoolbell
    scene black with fade
    scene school room with fade
    mainname "{i}Обычный день обычного старшеклассника. Ничего нового...{i}"
    stop sound fadeout 1.0
    scene night room with fade
    "{i}...{i}"
    return

label show_school:
    scene first meet with fade
    mainname "Меня зовут [mainname] Акиро и я ученик класса 3-1."
    mi "О, я тоже перевелась в этот класс. Получается сегодня прогуляем геометрию и английский."
    mainname "{i}Почему она так знакомо выглядит...{i}"
    mi "Аууу??? Мы пойдем?"
    mainname "Ой, пошли. Начнем со школьного двора."
    scene school backyard with fade
    show era at right:
    mi "У вас тут так красиво!"
    mainname "Странно, что ты удивляешься обычному школьному двору."
    show era disp at right
    mi "Ну знаешь, в моей прошлой школе всё было мрачно и серо. Да и кто-то впервые со мной прогуливается по школьному двору..."
    mainname "Прости, я не знал."
    show era at right
    mi "Глупости! Ты чего извиняешься?"
    scene school backyard with vpunch
    show cat calm at right:
        yalign 0.7
    cname "Мяу-мяу"
    mainname "Я же тебя запер в кабинете... Да как ты..."
    cname "А ключи запасные были-то на столе."
    scene school backyard with vpunch
    mainname "ЧЁЁЁЁЁЁ%%%%%%%%%%%%%%?7????"
    show eru afraid at right:
        yalign 0.54
    mainname "Он что-то сказал или мне это мерещится?"
    hide eru afraid at right
    show cat calm at right:
        yalign 0.7
    cname "Голубчики, я всего-то лишь говорящий кот, или какое имя ты там мне придумал... [cname]... Ну и имя..."
    mainname "Какой наглый..."
    hide cat calm
    show eru afraid at right:
         yalign 0.54
    mainname "Так значит ты волшебный..."
    hide eru afraid at right
    show cat calm at right:
        yalign 0.7
    cname "А все мы втроем знакомы неспроста, дорогие мои. Будьте бдительны и внимательнее."
    scene black with fade
    b "..."
    scene school room with fade
    mainname "{i}Что произошло...{i}"
    show eru afraid at right:
         yalign 0.54
    mainname "Этот кот каким-то образом отправил нас в класс..."
    mainname "Да что происходит..."
    hide eru afraid at right
    show teacher at right
    t "Мирай и [mainname], никаких разговоров во время уроков!"
    play sound schoolbell
    scene black with fade
    scene school room with fade
    mainname "{i}Мирай выбежала из класса.Что за странный день...{i}"
    stop sound fadeout 1.0
    scene night room with fade
    mainname "{i}...{i}"
    scene black with fade
    b "zzzZZzzZZZzzz"
    scene black with vpunch

    b "БЗЗЗЗЗЗЗЗЗЗ!!!!"

    stop sound fadeout 1.0

    scene morning room
    with fade
    mainname "{i}Пора вставать...{i}"
    play sound door
    b "Тук-тук!"
    stop sound
    b "[mainname], ты проснулся?"
    show mom
    m "[mainname], утречка!"
    mainname "Привет, мам."
    m "Завтрак уже готов, поэтому быстрее спускайся и поедай, пока ничего не остыло."
    mainname "Спасибо, мам."
    mainname "{i}Как странно, что она ведет себя будто под запись...{i}"
    hide mom
    mainname "{i}Надо поскорее в школу, чтобы встретиться с Мирай...{i}"
    scene black with fade
    play sound zip
    b "..."
    stop sound fadeout 1.0
    scene school with fade
    mainname "{i}Вот она!{i}"
    mainname "Мирай!!!"
    show era at right
    mi "Утречка, [mainname]. Прости, что вчера внезапно ушла. Поплохело и я ушла в медпункт."
    mainname "Главное, что сейчас всё хорошо. Ты не видела этого кота? Нам надо срочно отыскать его. После встречи с ним, я тоже чувствовал себя очень странно."
    mi "Согласна, пойдем искать его. Тогда скажем учительнице, что ты ознакомишь меня со школьными клубами."
    mainname "Вот и она..."
    hide era
    show teacher at right
    t "Мирай и [mainname], почему вы не спешите в класс?!"
    show era at left
    mi "[mainname] покажет мне все организации! А с оценками всё отлично, тем более [mainname] любимец учителей."
    t "Эх, хорошо. Заодно проверьте школьный двор. С утра охранник пытался поймать кота, но тот вечно исчезал. Не хватало нам тут зоопарк завести."
    hide teacher
    hide era
    scene school backyard with fade
    show eru afraid at right:
    mi "[mainname], вон он! Валяется под деревом."
    hide eru afraid
    show cat calm at right:
        yalign 0.7
    c_n "О, голубчики мои. Что ж вы нетерпеливые. Чего хотите? Хи-хи"
    mainname "Мы хотим узнать всю правду. Кто ты, что за странности происходят с нами. Почему моя мама ведет себя каждое утро одинаково."
    c_n "Если ты готов и хочешь этого, то для начала нам надо поменять локацию."
    scene world with fade
    c_n "А теперь сядьте поудобнее и прислушайтесь к истории..."
    scene space with fade
    "Один мудрец сказал однажды, что на самом деле ничто не умирает по-настоящему, а просто возвращается в другом обличии."
    scene w with fade
    "Так и устроено в этом мире, все мы - оболочки нашей души, а души наши - послушники вселенной, чьи дары сохраняются, но память обновляется, чтобы защититить от людских грез."
    scene death with fade
    "Каждый миг стороны вселенной распределяют в чью сторону забрать душу или же подарить тот самый шанс, в котором душа определится, сможет ли он принять терния. "
    scene real with fade
    "Каждый миг стороны вселенной распределяют в чью сторону забрать душу или же подарить тот самый шанс, в котором душа определится, сможет ли он принять терния. "
    scene real with fade
    return

label deny_to_teacher:
    scene school with fade
    show teacher at right
    mainname "Извиняюсь, сегодня у меня важная контрольная по геометрии. Мне надо готовиться."
    t "[mainname], ты безнадежен..."
    play sound schoolbell
    scene black with fade
    scene school room with fade
    mainname "{i}Обычный день обычного старшеклассника. Ничего нового... Но откуда такое странное чувство внутри.{i}"
    stop sound fadeout 1.0
    scene night room with fade
    "{i}...{i}"
    return