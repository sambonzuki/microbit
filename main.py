basic.show_string("Hello!")
music.play_melody("E B C5 A B G A F ", 120)
basic.show_leds("""
    . . . . .
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    """)

def on_forever():
    pass
basic.forever(on_forever)
