title: Building Blocks for Open Source Hardware
date: 2013-01-17
type: post

Many open source designs are based on existing hardware. This approach lets you
prototype your design using an off the shelf development board, then move to
your own PCB design once you're confident with your design. It's a popular and
effective way to build a product, just look at the number of projects that
started off as an Arduino.

One neat feature of [Upverter](http://www.upverter.com) is forking. This lets
you create a copy another open source project and start working on your own
version of it. It's very similar to forking on Github. This is great for open
source project where you want to reduce repeated work and build off someone
else's design.

Since there's a few very popular development boards, I've started creating
reference designs for these in Upverter. First off, we have the [Arduino
Reference
Design](http://upverter.com/ericevenchick/ad5b89911ead7cbd/Arduino-Reference-Design/).
This is a great start for any Arduino based project. It provides just the
basics: an ATmega328P microcontroller, crystal oscillator, FTDI compatible
serial header, and AVR programming port.

<img src="static/img/building-blocks-arduino.png" style='width:100%;'>

For fans of the MSP430 Launchpad from TI, there's the [MSP430 Launchpad
Reference
Design](http://upverter.com/ericevenchick/9b1044d4d7551c89/MSP430-Launchpad-Reference-Design/).
This lets you start working with MSP430 by providing a microcontroller, crystal,
and programming header that's compatible with the Launchpad.

<img src="static/img/building-blocks-launchpad.png" style='width:100%'>

The goal of this is to make it easy to move from development board to custom PCB
by giving hackers the same basic functionality as their development tools and
letting them expand it as they need. So try it out: fork a reference design, add
some components, and build something cool.

Want to see some more building blocks on Upverter? Let me know on
[Twitter](http://twitter.com/ericevenchick).
