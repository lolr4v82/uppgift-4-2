def on_received_number(receivedNumber):
    global handplayer2
    handplayer2 = receivedNumber
    if handplayer2 == 0:
        basic.show_leds("""
            . # # # .
                        # # # # #
                        # # # # #
                        # # # # #
                        . # # # .
        """)
    elif handplayer2 == 1:
        basic.show_leds("""
            . # # # .
                        . # # # .
                        . # # # .
                        . # # # .
                        . # # # .
        """)
    elif handplayer2 == 2:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        # # . # #
                        # # . # #
        """)
    else:
        pass
radio.on_received_number(on_received_number)

def on_gesture_shake():
    global hand
    hand = randint(0, 2)
    if hand == 0:
        basic.show_leds("""
            . # # # .
                        # # # # #
                        # # # # #
                        # # # # #
                        . # # # .
        """)
    elif hand == 2:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        # # . # #
                        # # . # #
        """)
    elif hand == 1:
        basic.show_leds("""
            . # # # .
                        . # # # .
                        . # # # .
                        . # # # .
                        . # # # .
        """)
    else:
        pass
    radio.send_number(hand)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

hand = 0
handplayer2 = 0
radio.set_group(20)

def on_forever():
    pass
basic.forever(on_forever)
