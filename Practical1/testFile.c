#include <stdio.h>    // Used for printf() statements
#include <wiringPi.h> // Include WiringPi library!

// Pin number declarations. We're using the Broadcom chip pin numbers.
const int ledPin = 0; // Regular LED - Broadcom pin 23, P1 pin 16
const int butPin = 25; // Active-low button - Broadcom pin 17, P1 pin 11


int main(void)
{
    // Setup stuff:
    wiringPiSetup(); // Initialize wiringPi -- using Broadcom pin numbers

   
    pinMode(ledPin, OUTPUT);     // Set regular LED as output
    pinMode(butPin, INPUT);      // Set button as INPUT

    printf("Blinker is running! Press CTRL+C to quit.\n");

    // Loop (while(1)):
    while(1)
    {
        if (digitalRead(butPin)) // Button is released if this returns 1
        {
            digitalWrite(ledPin, HIGH);     // Regular LED on
        }
        else // If digitalRead returns 0, button is pressed
        {
            digitalWrite(ledPin, LOW); // Turn LED OFF
        }
    }

    return 0;
}