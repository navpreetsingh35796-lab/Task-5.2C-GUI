# SIT210 Task 5.2C: Light Intensity Control Using GUI

A Raspberry Pi project demonstrating Pulse Width Modulation (PWM) to control LED brightness via a Python Tkinter graphical user interface.

---

## Overview

In this task, the basic ON/OFF control from Task 5.1P is extended to allow continuous brightness adjustment for a living room light. A GUI slider sets the PWM duty cycle from 0% to 100%, varying the average electrical power supplied to the LED.

---

## Hardware Requirements

* 1× Raspberry Pi (running Raspberry Pi OS)
* 1× Standard 5mm LED
* 1× Current-limiting resistor (220Ω – 330Ω)
* 1× Solderless breadboard
* 2× Female-to-male jumper wires

---

## Circuit Schematic & Pinout

| Raspberry Pi Pin | Pin Function | Component Connection | Purpose |
| :--- | :--- | :--- | :--- |
| **Physical Pin 12** | **GPIO 18** (PWM0) | LED Anode (longer leg) | PWM control signal |
| **Physical Pin 6** | **GND** (Ground) | Resistor (Lead 2) | Circuit return path |
| *Breadboard row* | — | LED Cathode (shorter leg) to Resistor (Lead 1) | Current-limiting protection |

---

## Software & Dependencies

* **OS:** Raspberry Pi OS
* **Language:** Python 3
* **Libraries:**
  * `RPi.GPIO` (Hardware pin control and PWM generation)
  * `tkinter` (Graphical user interface)
