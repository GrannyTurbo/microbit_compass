bluetooth.start_magnetometer_service()
bluetooth.start_led_service()
degrees = input.compass_heading()
basic.show_string("COMPASS")

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 22.5 or degrees > 337.5:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif degrees < 22.5:
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif degrees < 67.5:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # # #
                        . . . . .
                        . . . . .
        """)
    elif degrees < 112.5:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . # .
                        . . . . #
        """)
    elif degrees < 157.5:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . # . .
                        . . # . .
        """)
    elif degrees < 202.5:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
    elif degrees < 247.5:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # . .
                        . . . . .
                        . . . . .
        """)
    else:
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
basic.forever(on_forever)
