## Trabajo práctico INTEGRADOR de la asignatura DCI ##

Este repositorio contiene el trabajo práctico final para la asignatura de Diseño de Circuitos Impresos de la carrera de
posgrado de FIUBA.

* Autor: Tomás Botalla (tbotalla@fi.uba.ar)
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

Y además colcar el archivo de texto de la misma en el directorio raíz (ver [LICENSE](LICENSE)).

Para este TP se pide que la licencia sea de hardware abierto. Ver la sección "What license should I
use?": https://www.oshwa.org/faq/

Material de terceros (imágenes y esquemático de referencia Cyclone-92, PDFs de fabricantes en `info/`) no está cubierto
por esta licencia; ver atribuciones en [doc/propuesta/README.md](doc/propuesta/README.md).

## Estructura del TP INTEGRADOR ##

Se propone y se pide utilizar la siguiente estructura.

* doc: Toda la información sobre el circuito, principalmente de autoría o procesamiento propio. Por ejemplo:
    * Notas de ingeniería propias.
    * Notas de aplicación propias.
    * Estudios previos, estado del arte, resumen de las investigaciones.
    * Notas con cálculos.
    * Dibujos adicionales.
    * Fotos de los prototipos.
    * Presupuestos, cotizaciones.
* info: Toda la iformación recolectada, principalmente de terceros, como por ejemplo:
    * Hojas de datos.
    * Notas de aplicación.
    * Info de productos comerciales.
    * Info en internet.
* pcb: Archivos de diseño esquemático y pcb.

Dependiendo la magnitud del proyecto, tendremos más o menos información en estos directorios.
Revisar los README.md en cada directorio para conocer las pautas de cada uno para este TP.

**Contenido actual de este trabajo (punteros):**

* [doc/propuesta/README.md](doc/propuesta/README.md), propuesta, modalidad réplica, imágenes de referencia.
* [info/README.md](info/README.md), datasheets TP4056, DW01A, FS8205A (`info/*.pdf`).
* [pcb/battery-charger/](pcb/battery-charger/battery-charger.kicad_pro), proyecto KiCad 10.
* [DCI - Checklist TP.xlsx](<DCI - Checklist TP.xlsx>), checklist de autoevaluación del TP.

NOTA: El alumno puede y debe borrar de este archivo todo lo que considere necesario, por ejemplo las aclaraciones del
docente y esta misma nota.

## Obligatorios para el TP INTEGRADOR ##

* doc/propuesta/README.md (con textos y links, formato markdown, a imágenes que deben estar en el mismo repo. Las
  imágenes son las que se piden en las pautas de TP).
* info/*.pdf (Se piden solo las hojas de datos de los componentes relevantes como circuitos integrados, conectores
  particulares, módulos, etc. No es necesario poner hojas de pasivos, discretos comunes, conectores estándar.)
* pcb/* (Acá va el proyecto KiCad, modelos 3D, bibliotecas particulares y archivos generados como BOM, gerbers, etc.).
  EVITE subir al git archivos temporales de KiCad. Se recomienda usar un .gitignore adecuado.
* El alumnos es libre de agregar otras cosas, pero siempre tenga en cuenta que el repositorio es público. Evitar colocar
  información personal o documentación confidencial. 