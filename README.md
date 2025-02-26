# Pulsed Noise Jamming in Drone-sim
### **Malik Shummaim Khalil**
**GID:** G01574336

## ** What is Pulsed noise jamming?**
Pulsed Noise Jamming (Burst Jamming) is an electronic warfare technique used to disrupt or interfere with radar,communication, or navigation systems by emitting short bursts of high-power noise at specific intervals.

## **. How I Implemented Pulsed Noise Jamming?

###

```
 def __init__(self, jamming_probability=0.3, noise_intensity=0.7, jamming_power_dbm=-70, pulse_duration=2, pulse_interval=5):
 ``` 
 In this init method, we initialize a Pulsed Noise Jammer with:

jamming_probability = random number between 0 and 1 (default is 30% chance of jamming)

noise_intensity: The strength of the interference (defaults to 0.7).

jamming_power_dbm Jamming signal power (-70 dBm).

pulse_duration: Active Jamming Time (2 sec);

pulse_interval: Time between pulse (5 sec).

You can have pulse jamming, where it is active for pulse_duration and inactive for pulse_interval.

 def update_jamming_state(self):
 ``` def update_jamming_state(self): defines the method inside a class (presumably, a Pulsed Noise Jammer)

What It Does:

Update the jamming state (active / inactive).

Probably enables/disables jamming depend on pulse_duration and pulse_interval.

Invoked at regular intervals to start or stop jamming.

 def jam_signal(self, message):
 ``` def jam_signal(self, message): # Define a method inside a class (probably for a jammer)

What It Does:
Change, tamper with, or intercept the message according to jamming logic.
Decides how it will affect the signal, using parameters like jamming probability, noise intensity, and pulsing behavior.

 def jamming_signal_power(self):
 ``` def jamming_signal_powering=self):

It Tells;

What's the jamming signal power level (probably in dBm).
It give information according to jamming intensity, range, or pulse state.
This is used in the simulation to measure the effect of jamming.




