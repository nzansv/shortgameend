
## Основное ####################################################################
define config.name = _("Short Life No End")


## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = False


## Версия игры.

define config.version = "1.0"


## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.

define gui.about = _p("""
""")

define build.name = "ShortLifeNoEnd"


## Звуки и музыка ##############################################################


define config.has_sound = True
define config.has_music = True
define config.has_voice = True

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

## Вход и выход в игровое меню.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Переход между экранами игрового меню.

define config.intra_transition = dissolve

## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = None

define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Стандартные настройки #######################################################

default preferences.text_cps = 0


## Стандартная задержка авточтения.

default preferences.afm_time = 15


## Директория сохранений #######################################################

define config.save_directory = "ShortLifeNoEnd-1637951036"


## Иконка ######################################################################
define config.window_icon = "gui/window_icon.png"


## Настройка Дистрибутива ######################################################

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')

