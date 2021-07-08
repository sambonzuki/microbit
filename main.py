basic.show_string("Hello!")
music.play_melody("C C C5 C5 B G A B ", 120)
basic.show_leds("""
    # # # # #
    # . # . #
    # # # # #
    # . . . #
    # # # # #
    """)

def on_forever():
    pass
basic.forever(on_forever)
