import string

from latex_escape import do_latex_escape


def test_replacements_without_spaces():
    RESULT = (
        "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "!\"\\#\\$\\%\\&'()*+,-./:;<=>?@["
        "\\textbackslash ]\\textasciicircum \\_`\\{|\\}\\textasciitilde "
        "\t\n\r\x0c"
    )

    assert do_latex_escape(string.printable.replace(" ", "")) == RESULT


def test_replacements_with_space():
    RESULT = (
        "0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z "
        'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! " '
        "\\# \\$ \\% \\& ' ( ) * + , - . / : ; < = > ? @ [ "
        "\\textbackslash\\space ] \\textasciicircum\\space \\_ `"
        " \\{ | \\} \\textasciitilde\\space   \t \n \r  \x0c"
    )

    spaced = " ".join([char for char in string.printable])
    assert do_latex_escape(spaced) == RESULT
