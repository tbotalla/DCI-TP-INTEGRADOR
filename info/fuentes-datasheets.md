# Fuentes de datasheets - Registro

Descargas realizadas el **2026-11-21** para el TP integrador DCI.

| Archivo local | URL usada | Notas |
|---------------|-----------|--------|
| `TP4056-42-ESOP8.pdf` | https://www.toppwr.com/uploadfile/file/20260702/6a45ff9f6dfe2.pdf | Fabricante Top Power; incluye ordenamiento `TP4056-42-ESOP8`. La URL de LCSC en el esquema devolvía HTML sin PDF directo. |
| `DW01A.pdf` | https://hmsemi.com/downfile/DW01A.PDF | Coincide con el campo `Datasheet` de **U2** en `battery-charger.kicad_sch`. |
| `FS8205A.pdf` | https://www.laskakit.cz/user/related_files/fs8205a-fortune_semiconductor.pdf | Rev. Fortune Semiconductor (espejo europeo). El dominio `ic-fortune.com` falló SSL desde este entorno; el contenido es el datasheet FS8205A estándar. |

Verificación local:

```bash
file info/*.pdf   # debe reportar "PDF document" para los tres
```