# Default parameter values screen_width in line 2 don't have a space between '=' sign and 'value'.
# This changes if we annotate =. I'll copy what it looks like without annotation and change it with annotation
# def banner_text(text=" ", screen_width=100):
def banner_text(text: str = " ", screen_width: int = 100) -> None:
    """
    Create a centered text with asterisks around it to produce a banner.
    The text must be able to fit inside the screen width.

    :param text: `Str` input for banner.
    :param screen_width: `Int` value for width of banner.
    :raises:
        ValueError: if text is larger than screen_width - 4.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String '{0}' is larger than specified width '{1}'"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("The ocean saw the world begin,")
banner_text("and the ocean knows how the world will end.")
banner_text("Thus, it calls us down the path we must take.")
banner_text("Thus, it leads us to a just world.")
banner_text("It envelops all pain and suffering,")
banner_text("honorably and kindly wrapping them up.")
banner_text()
banner_text("The ocean saw the world begin,")
banner_text("and the ocean knows how the world will end.")
banner_text("Even after I'm gone,")
banner_text("the all-knowing ocean will lead the way.")
banner_text("I must not fear, because you are here.")
banner_text("I must not be timid, because my comrades wait for me.")
banner_text("We must advance towards the blue horizon.")
banner_text("*")
