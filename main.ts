radio.onReceivedNumber(function (receivedNumber) {
    handplayer2 = receivedNumber
    if (handplayer2 == 0) {
        basic.showLeds(`
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            `)
    } else if (handplayer2 == 1) {
        basic.showLeds(`
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
    } else if (handplayer2 == 2) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            `)
    } else {
    	
    }
})
input.onGesture(Gesture.Shake, function () {
    hand = randint(0, 2)
    if (hand == 0) {
        basic.showLeds(`
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            `)
    } else if (hand == 2) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            `)
    } else if (hand == 1) {
        basic.showLeds(`
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
    } else {
    	
    }
    radio.sendNumber(hand)
})
let hand = 0
let handplayer2 = 0
radio.setGroup(20)
basic.forever(function () {
	
})
