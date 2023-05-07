bluetooth.startMagnetometerService()
bluetooth.startLEDService()
let degrees = input.compassHeading()
basic.showIcon(IconNames.Fabulous)
basic.forever(function () {
    degrees = input.compassHeading()
    if (degrees < 22.5 || degrees > 337.5) {
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else if (degrees < 67.5) {
        basic.showLeds(`
            . . . . #
            . . . # .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else if (degrees < 112.5) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # # #
            . . . . .
            . . . . .
            `)
    } else if (degrees < 157.5) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . # .
            . . . . #
            `)
    } else if (degrees < 202.5) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            `)
    } else if (degrees < 247.5) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . # . . .
            # . . . .
            `)
    } else if (degrees < 292.5) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # . .
            . . . . .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            # . . . .
            . # . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
})
