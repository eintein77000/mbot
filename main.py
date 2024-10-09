def right():
    servo_motor.motor(Motor.M2_B, Dir.FORWARD, 2000)
    servo_motor.motor(Motor.M1_A, Dir.FORWARD, 0)

def on_received_number(receivedNumber):
    global ordre
    ordre = receivedNumber
radio.on_received_number(on_received_number)

def left():
    servo_motor.motor(Motor.M1_A, Dir.FORWARD, 2000)
    servo_motor.motor(Motor.M2_B, Dir.FORWARD, 0)
def stop():
    servo_motor.motor(Motor.M1_A, Dir.FORWARD, 0)
    servo_motor.motor(Motor.M2_B, Dir.FORWARD, 0)
def backward():
    servo_motor.motor(Motor.M1_A, Dir.BACKWARD, 2000)
    servo_motor.motor(Motor.M2_B, Dir.BACKWARD, 2000)
def forward():
    servo_motor.motor(Motor.M1_A, Dir.FORWARD, 2000)
    servo_motor.motor(Motor.M2_B, Dir.FORWARD, 2000)
ordre = 0
radio.set_group(1)
basic.show_icon(IconNames.HEART)
strip = neopixel.create(DigitalPin.P16, 7, NeoPixelMode.RGB)
strip.set_brightness(100)
strip.clear()
strip.show()
strip.show_rainbow(1, 360)
angle_H = 85
angle_V = 85
angle_pince = 85
basic.pause(200)
servo_motor.servo(Servo_Ch.S1, angle_H)
basic.pause(200)
servo_motor.servo(Servo_Ch.S2, angle_V)
basic.pause(100)
servo_motor.servo(Servo_Ch.S3, angle_pince)
basic.pause(100)

def on_forever():
    global angle_V, angle_H
    if ordre == 1:
        forward()
    elif ordre == 2:
        left()
    elif ordre == 3:
        right()
    elif ordre == 4:
        backward()
    elif ordre == 5:
        angle_V += -6
        basic.pause(100)
        servo_motor.servo(Servo_Ch.S2, angle_V)
        basic.pause(100)
    elif ordre == 6:
        angle_H += 6
        basic.pause(100)
        servo_motor.servo(Servo_Ch.S1, angle_H)
        basic.pause(100)
    elif ordre == 7:
        angle_H += -6
        basic.pause(100)
        servo_motor.servo(Servo_Ch.S1, angle_H)
        basic.pause(100)
    elif ordre == 8:
        angle_V += 6
        basic.pause(100)
        servo_motor.servo(Servo_Ch.S2, angle_V)
        basic.pause(100)
    else:
        stop()
    basic.pause(200)
basic.forever(on_forever)
