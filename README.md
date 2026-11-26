## Trabajo práctico INTEGRADOR de la asignatura DCI ##

Este repositorio contiene el trabajo práctico final para la asignatura de Diseño de Circuitos Impresos de la carrera de
posgrado de FIUBA.

* Autor: Tomás Enrique Botalla (tbotalla@fi.uba.ar)
* Título corto del trabajo: Cargador Li-ion TP4056 con protección DW01A / FS8205A (réplica)
* Descripción: Placa para cargar y proteger una celda Li-ion 18650 desde 5 V USB: cargador lineal TP4056 (CC/CV,
  corriente programable con RPROG), protección DW01A con interruptores FS8205A en BAT−, entrada USB-C solo VBUS/GND,
  indicación CHRG/STDBY. Rediseño en KiCad 10 a partir de la
  referencia [Cyclone-92](https://github.com/Cyclone-92/TP4056-LiPo-charger-with-DW01A-and-FS8205A-MOSFET-protection).
  Proyecto KiCad: `pcb/battery-charger/`. Repositorio: https://github.com/tbotalla/DCI-TP-INTEGRADOR
* Cursada: OCT-NOV-DIC 2026 (DCI26A)

## Licencia de este trabajo ##

El diseño hardware, documentación de autoría y archivos KiCad propios de este repositorio se publican bajo
**[CERN Open Hardware Licence v2, Strongly Reciprocal (CERN-OHL-S-2.0)](https://opensource.cern.ch/cern-open-hardware-licence/version-2/strongly-reciprocal/)**
(`SPDX-License-Identifier: CERN-OHL-S-2.0`). Es una licencia de **hardware abierto con copyleft fuerte**: permite uso,
estudio, modificación y redistribución, y exige compartir modificaciones del diseño en las mismas condiciones.

El texto completo de la licencia está en [LICENSE](LICENSE) en la raíz del repositorio.

Material de terceros (imágenes y esquemático de referencia Cyclone-92, PDFs de fabricantes en `info/`) no está cubierto
por esta licencia. Ver atribuciones en [doc/propuesta/README.md](doc/propuesta/README.md).

## Estructura del TP INTEGRADOR ##
* [doc/propuesta/README.md](doc/propuesta/README.md), propuesta, modalidad réplica, imágenes de referencia.
* [info/README.md](info/README.md), datasheets TP4056, DW01A, FS8205A (`info/*.pdf`).
* [pcb/battery-charger/](pcb/battery-charger/battery-charger.kicad_pro), proyecto KiCad 10.
* [DCI - Checklist TP.xlsx](<DCI - Checklist TP.xlsx>), checklist de autoevaluación del TP.