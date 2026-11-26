# Información de terceros - hojas de datos

Copias locales de **datasheets** usadas para el cargador `pcb/battery-charger/`.  
Los PDF corresponden a los circuitos integrados y al MOSFET dual del path de protección.

## Archivos en este directorio

| Archivo                                    | Componente               | Uso en el diseño                | Origen (descarga)                                                                                                            |
|--------------------------------------------|--------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [TP4056-42-ESOP8.pdf](TP4056-42-ESOP8.pdf) | TP4056 (variante ESOP-8) | **U1**, cargador lineal         | NanJing Top Power / [toppwr.com](https://www.toppwr.com/uploadfile/file/20260702/6a45ff9f6dfe2.pdf)                          |
| [DW01A.pdf](DW01A.pdf)                     | DW01A                    | **U2**, protección Li-ion       | Shenzhen H&M Semiconductor / [hmsemi.com](https://hmsemi.com/downfile/DW01A.PDF)                                             |
| [FS8205A.pdf](FS8205A.pdf)                 | FS8205A (dual N-MOSFET)  | **Q1**, interruptores en `BAT−` | Fortune Semiconductor (espejo) / [laskakit.cz](https://www.laskakit.cz/user/related_files/fs8205a-fortune_semiconductor.pdf) |

Detalle de fuentes y fecha de descarga: [fuentes-datasheets.md](fuentes-datasheets.md).

## Huellas de paquete

| Ref | Símbolo / valor  | Paquete en diseño |
|-----|------------------|-------------------|
| U1  | TP4056-42-ESOP8  | SOIC-8 + EP       | 
| U2  | DW01A            | SOT-23-6          | 
| Q1  | FS8205A / FS8205 | **SOT-23-6**      |
