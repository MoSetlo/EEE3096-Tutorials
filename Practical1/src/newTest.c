/*
 * BinClock.c
 * Jarrod Olivier
 * Modified by Keegan Crankshaw
 * Further Modified By: Mark Njoroge 
 *
 * 
 * STLMOU001 NTLSIP016
 * 19/08/21
*/

#include <signal.h> //for catching signals
#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <stdio.h> //For printf functions
#include <stdlib.h> // For system functions

#include "BinClock.h"
#include "CurrentTime.h"

//Global variables
int hours, mins, secs;
long lastInterruptTime = 0; //Used for button debounce
int RTC; //Holds the RTC instance

int HH,MM,SS;

int main(void){
	RTC = wiringPiI2CSetup(RTCAddr); //Set up the RTC

	//Set random time (3:04PM)
	//You can comment this file out later
	wiringPiI2CWriteReg8(RTC, HOUR_REGISTER, 0x13+TIMEZONE);
	wiringPiI2CWriteReg8(RTC, MIN_REGISTER, 0x4);
	wiringPiI2CWriteReg8(RTC, SEC_REGISTER, 0x00);
	
	int data=wiringPiI2CReadReg8(RTC, HOUR_REGISTER);

	printf("The data is: %d", data)	

	}
	return 0;
}