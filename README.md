# [Analog-signal-calculator](http://electronic.pythonanywhere.com/)

## Description

You can scale the signal range of the analog inputs and outputs .

## About

Scaling of the analog input  
The range of 0-20 mA without the "Scale_current_input" instruction corresponds to the PLC’s internal signal range of
0-27648. The "Scale_current_input" instruction adapts this internal range to 4-20 mA linearly, starting with "0" for 4
mA and ending up with "27648" for 20 mA. A limit for wire break monitoring can be chosen by hand..

## Copyright and License

Copyright 2020 Electronic | Radosław Tecmer [RT](http://electronic.pythonanywhere.com/#about) license.