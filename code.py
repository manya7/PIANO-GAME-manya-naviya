from machine import Pin, TouchPad, PWM
import time
import random

buzzer = PWM(Pin(25))
buzzer.duty(0)
buzzer.freq(1000)


thinker = [1200,1400,1600,1400,1200,1400,1800,1600,
1500,1700,1900,1700,1500,1700,2000,1800,
1600,1400,1200,1400,1600,1800,2000,1800,
1700,1500,1300,1500,1700,1900,2100,1900,
2000,1800,1600,1800,2000,2200,2400,2200]

pb = Pin(4, Pin.IN, Pin.PULL_UP)

Sa = TouchPad(Pin(13))
Re = TouchPad(Pin(12))
Ga = TouchPad(Pin(14))
Ma = TouchPad(Pin(27))
Pa = TouchPad(Pin(33))
Dha = TouchPad(Pin(32))
Ni = TouchPad(Pin(15))

Sa_light = Pin(18,Pin.OUT)
Re_light = Pin(19,Pin.OUT)
Ga_light = Pin(21,Pin.OUT)
Ma_light = Pin(22,Pin.OUT)
Pa_light = Pin(23,Pin.OUT)
Dha_light = Pin(26,Pin.OUT)

Leds = [Sa_light, Re_light, Ga_light, Ma_light, Pa_light, Dha_light]

while True:

    if pb.value() == 0:
        time.sleep(0.5)

        gamenotes = [random.randint(0,6),random.randint(0,6),random.randint(0,6)]

        for note in gamenotes:

            for led in Leds:
                led.off()

            if note == 0:
                Sa_light.on()
                buzzer.freq(262)
            elif note == 1:
                Re_light.on()
                buzzer.freq(294)
            elif note == 2:
                Ga_light.on()
                buzzer.freq(330)
            elif note == 3:
                Ma_light.on()
                buzzer.freq(349)
            elif note == 4:
                Pa_light.on()
                buzzer.freq(392)
            elif note == 5:
                Dha_light.on()
                buzzer.freq(440)
            elif note == 6:
                Sa_light.on()
                buzzer.freq(494)

            buzzer.duty(512)
            time.sleep(0.5)
            buzzer.duty(0)
            time.sleep(0.5)


        for n in thinker:
            buzzer.freq(n)
            buzzer.duty(700)
            time.sleep_ms(100)
            buzzer.duty(0)
            time.sleep_ms(25)
            
            
        users = [10,10,10]

        for i in range(3):

            users[i] = 10  

            for t in range(200): 

                if Sa.read() < 250:
                    users[i] = 0
                    Sa_light.on()
                    buzzer.freq(262)
                    break

                elif Re.read() < 250:
                    users[i] = 1
                    Re_light.on()
                    buzzer.freq(294)
                    break

                elif Ga.read() < 250:
                    users[i] = 2
                    Ga_light.on()
                    buzzer.freq(330)
                    break

                elif Ma.read() < 250:
                    users[i] = 3
                    Ma_light.on()
                    buzzer.freq(349)
                    break

                elif Pa.read() < 250:
                    users[i] = 4
                    Pa_light.on()
                    buzzer.freq(392)
                    break

                elif Dha.read() < 250:
                    users[i] = 5
                    Dha_light.on()
                    buzzer.freq(440)
                    break

                elif Ni.read() < 250:
                    users[i] = 6
                    Sa_light.on()
                    buzzer.freq(494)
                    break

                time.sleep(0.01) 

            buzzer.duty(512)
            time.sleep(0.3)
            buzzer.duty(0)
            for led in Leds:
                led.off()

            time.sleep(0.3)

        
        if users == gamenotes:
            for led in Leds:
                led.on()
            print("WINNER WINNER CHICKEN DINNER")
            time.sleep(1)
        else:
            buzzer.freq(150)
            buzzer.duty(512)
            time.sleep(1)
            buzzer.duty(0)
            print("LOSER??????")
