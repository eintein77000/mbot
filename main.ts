/**
 */
function right () {
    servo_motor.motor(Motor.M2_B, Dir.forward, 2000)
    servo_motor.motor(Motor.M1_A, Dir.forward, 0)
}
radio.onReceivedNumber(function (receivedNumber) {
    ordre = receivedNumber
})
function left () {
    servo_motor.motor(Motor.M1_A, Dir.forward, 2000)
    servo_motor.motor(Motor.M2_B, Dir.forward, 0)
}
function stop () {
    servo_motor.motor(Motor.M1_A, Dir.forward, 0)
    servo_motor.motor(Motor.M2_B, Dir.forward, 0)
}
function backward () {
    servo_motor.motor(Motor.M1_A, Dir.backward, 2000)
    servo_motor.motor(Motor.M2_B, Dir.backward, 2000)
}
function forward () {
    servo_motor.motor(Motor.M1_A, Dir.forward, 2000)
    servo_motor.motor(Motor.M2_B, Dir.forward, 2000)
}
let ordre = 0
radio.setGroup(1)
basic.showIcon(IconNames.Heart)
let strip = neopixel.create(DigitalPin.P16, 7, NeoPixelMode.RGB)
strip.setBrightness(100)
strip.clear()
strip.show()
strip.showRainbow(1, 360)
let angle_H = 85
let angle_V = 85
let angle_pince = 85
basic.pause(200)
servo_motor.servo(Servo_Ch.S1, angle_H)
basic.pause(200)
servo_motor.servo(Servo_Ch.S2, angle_V)
basic.pause(100)
servo_motor.servo(Servo_Ch.S3, angle_pince)
basic.pause(100)
basic.forever(function () {
    if (ordre == 1) {
        forward()
    } else if (ordre == 2) {
        left()
    } else if (ordre == 3) {
        right()
    } else if (ordre == 4) {
        backward()
    } else if (ordre == 5) {
        angle_V += -6
        basic.pause(100)
        servo_motor.servo(Servo_Ch.S2, angle_V)
        basic.pause(100)
    } else if (ordre == 6) {
        angle_H += 6
        basic.pause(100)
        servo_motor.servo(Servo_Ch.S1, angle_H)
        basic.pause(100)
    } else if (ordre == 7) {
        angle_H += -6
        basic.pause(100)
        servo_motor.servo(Servo_Ch.S1, angle_H)
        basic.pause(100)
    } else if (ordre == 8) {
        angle_V += 6
        basic.pause(100)
        servo_motor.servo(Servo_Ch.S2, angle_V)
        basic.pause(100)
    } else {
        stop()
    }
    basic.pause(200)
})
