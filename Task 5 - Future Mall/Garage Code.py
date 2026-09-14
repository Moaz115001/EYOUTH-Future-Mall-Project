from machine import Pin
from time import sleep_ms

ENTRY_BUTTON = 14
EXIT_BUTTON = 27

YELLOW_LED = 5
GREEN_LED = 2
BLUE_LED = 18
RED_LED = 4

MAX_CAPACITY = 15

entry_button = Pin(ENTRY_BUTTON, Pin.IN, Pin.PULL_UP)
exit_button = Pin(EXIT_BUTTON, Pin.IN, Pin.PULL_UP)

yellow_led = Pin(YELLOW_LED, Pin.OUT)
green_led = Pin(GREEN_LED, Pin.OUT)
blue_led = Pin(BLUE_LED, Pin.OUT)
red_led = Pin(RED_LED, Pin.OUT)

car_count = 0


def update_status():
    green_led.value(car_count < MAX_CAPACITY)
    red_led.value(car_count >= MAX_CAPACITY)


def blink(led):
    led.on()
    sleep_ms(250)
    led.off()


def show_status():
    print()
    print("================================")
    print("       FUTURE MALL GARAGE")
    print("================================")
    print(" Cars      : {}/{}".format(car_count, MAX_CAPACITY))
    print(" Available : {}".format(MAX_CAPACITY - car_count))

    if car_count >= MAX_CAPACITY:
        print(" Status    : FULL")
    else:
        print(" Status    : AVAILABLE")

    print("================================")


update_status()
show_status()

while True:

    if entry_button.value() == 0:

        if car_count < MAX_CAPACITY:
            car_count += 1
            blink(yellow_led)
            update_status()

            print(">> ENTRY")
            show_status()

        while entry_button.value() == 0:
            sleep_ms(20)

    if exit_button.value() == 0:

        if car_count > 0:
            car_count -= 1
            blink(blue_led)
            update_status()

            print(">> EXIT")
            show_status()

        while exit_button.value() == 0:
            sleep_ms(20)

    sleep_ms(20)