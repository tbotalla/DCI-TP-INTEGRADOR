#!/usr/bin/env python3
"""Add CHRG/STDBY LED strings inside TP4056 schematic box."""
from __future__ import annotations

import re
import sys
import uuid
from pathlib import Path

SCH = Path(__file__).resolve().parents[1] / "battery-charger.kicad_sch"
CYCLONE = Path("/tmp/cyclone.sch")
PROJECT_PATH = "/7876485e-db87-4332-b590-39e5e422cf56"
LIB_R_MARKER = '\t\t(symbol "Device:R"\n\t\t\t(pin_numbers'


def new_uuid() -> str:
    return str(uuid.uuid4())


def add_wire(wires: list[str], x1: float, y1: float, x2: float, y2: float) -> None:
    wires.append(
        f"""\t(wire
\t\t(pts
\t\t\t(xy {x1} {y1}) (xy {x2} {y2})
\t\t)
\t\t(stroke
\t\t\t(width 0)
\t\t\t(type default)
\t\t)
\t\t(uuid "{new_uuid()}")
\t)"""
    )


def add_junction(junctions: list[str], x: float, y: float) -> None:
    junctions.append(
        f"""\t(junction
\t\t(at {x} {y})
\t\t(diameter 0)
\t\t(color 0 0 0 0)
\t\t(uuid "{new_uuid()}")
\t)"""
    )


def resistor_block(
    ref: str,
    value: str,
    x: float,
    y: float,
    rotation: int,
    sym_uid: str,
    p1: str,
    p2: str,
) -> str:
    return f"""\t(symbol
\t\t(lib_id "Device:R")
\t\t(at {x} {y} {rotation})
\t\t(unit 1)
\t\t(body_style 1)
\t\t(exclude_from_sim no)
\t\t(in_bom yes)
\t\t(on_board yes)
\t\t(in_pos_files yes)
\t\t(dnp no)
\t\t(fields_autoplaced yes)
\t\t(uuid "{sym_uid}")
\t\t(property "Reference" "{ref}"
\t\t\t(at {x + 2.54} {y - 1.27} 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t\t(justify left)
\t\t\t)
\t\t)
\t\t(property "Value" "{value}"
\t\t\t(at {x + 2.54} {y + 1.27} 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t\t(justify left)
\t\t\t)
\t\t)
\t\t(property "Footprint" "Resistor_SMD:R_0805_2012Metric"
\t\t\t(at {x - 1.778} {y} 90)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(property "Datasheet" ""
\t\t\t(at {x} {y} 0)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(property "Description" "Resistor"
\t\t\t(at {x} {y} 0)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(pin "1"
\t\t\t(uuid "{p1}")
\t\t)
\t\t(pin "2"
\t\t\t(uuid "{p2}")
\t\t)
\t\t(instances
\t\t\t(project "battery-charger"
\t\t\t\t(path "{PROJECT_PATH}"
\t\t\t\t\t(reference "{ref}")
\t\t\t\t\t(unit 1)
\t\t\t\t)
\t\t\t)
\t\t)
\t)"""


def led_block(
    ref: str, value: str, x: float, y: float, sym_uid: str, p1: str, p2: str
) -> str:
    return f"""\t(symbol
\t\t(lib_id "Device:LED")
\t\t(at {x} {y} 0)
\t\t(unit 1)
\t\t(body_style 1)
\t\t(exclude_from_sim no)
\t\t(in_bom yes)
\t\t(on_board yes)
\t\t(in_pos_files yes)
\t\t(dnp no)
\t\t(fields_autoplaced yes)
\t\t(uuid "{sym_uid}")
\t\t(property "Reference" "{ref}"
\t\t\t(at {x + 2.54} {y - 1.27} 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t\t(justify left)
\t\t\t)
\t\t)
\t\t(property "Value" "{value}"
\t\t\t(at {x + 2.54} {y + 1.27} 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t\t(justify left)
\t\t\t)
\t\t)
\t\t(property "Footprint" "LED_SMD:LED_0805_2012Metric"
\t\t\t(at {x} {y} 0)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(property "Datasheet" ""
\t\t\t(at {x} {y} 0)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(property "Description" "Light emitting diode"
\t\t\t(at {x} {y} 0)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(pin "1"
\t\t\t(uuid "{p1}")
\t\t)
\t\t(pin "2"
\t\t\t(uuid "{p2}")
\t\t)
\t\t(instances
\t\t\t(project "battery-charger"
\t\t\t\t(path "{PROJECT_PATH}"
\t\t\t\t\t(reference "{ref}")
\t\t\t\t\t(unit 1)
\t\t\t\t)
\t\t\t)
\t\t)
\t)"""


def ensure_led_lib_symbol(text: str) -> str:
    if '\t\t(symbol "Device:LED"' in text:
        return text
    if not CYCLONE.is_file():
        raise RuntimeError(f"Missing {CYCLONE} for Device:LED lib excerpt")
    cyclone = CYCLONE.read_text()
    m = re.search(
        r'\t\t\(symbol "Device:LED".*?\n\t\t\)\n\t\t\(symbol "Device:R"',
        cyclone,
        re.DOTALL,
    )
    if not m:
        raise RuntimeError("Could not extract Device:LED from cyclone reference")
    led_lib = m.group(0).removesuffix('\t\t(symbol "Device:R"').rstrip()
    if "(embedded_fonts no)" not in led_lib:
        led_lib = led_lib.replace(
            "\n\t\t)\n",
            "\n\t\t\t(embedded_fonts no)\n\t\t)\n",
            1,
        )
    if LIB_R_MARKER not in text:
        raise RuntimeError("Device:R lib anchor missing")
    return text.replace(LIB_R_MARKER, led_lib + LIB_R_MARKER, 1)


def patch(text: str) -> str:
    if '(reference "D1")' in text:
        print("D1 already present — no changes", file=sys.stderr)
        return text

    text = ensure_led_lib_symbol(text)

    text = re.sub(
        r"\t\(wire\n\t\t\(pts\n\t\t\t\(xy 110\.49 80\.01\) \(xy 109\.22 80\.01\)\n\t\t\).*?\n\t\t"
        r'\(uuid "4be09e66-a0ee-4b87-9b50-10793b1b5e28"\)\n\t\)\n',
        "",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\t\(wire\n\t\t\(pts\n\t\t\t\(xy 110\.49 38\.1\) \(xy 105\.41 38\.1\)\n\t\t\).*?\n\t\t"
        r'\(uuid "f0ed965f-0d4d-41f0-9a4c-7a776bddc8f4"\)\n\t\)\n',
        "",
        text,
        flags=re.DOTALL,
    )

    wires: list[str] = []
    junctions: list[str] = []

    # +5V tap for both LED strings (from existing vertical at 82.55)
    add_wire(wires, 82.55, 36.83, 82.55, 38.1)
    add_junction(junctions, 82.55, 38.1)
    add_wire(wires, 82.55, 38.1, 82.55, 35.56)
    add_junction(junctions, 82.55, 35.56)

    # CE must stay on +5V (do not leave wire 110.49/33.02 floating)
    add_wire(wires, 110.49, 33.02, 100.33, 33.02)

    # CHRG: +5V -> R1 -> D1 (A) — K at 92.71 -> U1 ~{CHRG} @ 110.49/38.1
    add_wire(wires, 82.55, 38.1, 85.09, 38.1)
    add_junction(junctions, 92.71, 38.1)
    add_wire(wires, 92.71, 38.1, 100.33, 38.1)
    add_wire(wires, 92.71, 38.1, 110.49, 38.1)

    # STDBY: +5V -> R2 -> D2 — K -> U1 ~{STDBY} @ 110.49/40.64
    add_wire(wires, 82.55, 35.56, 85.09, 35.56)
    add_junction(junctions, 92.71, 35.56)
    add_wire(wires, 92.71, 35.56, 100.33, 35.56)
    add_wire(wires, 92.71, 35.56, 110.49, 35.56)
    add_wire(wires, 110.49, 35.56, 110.49, 40.64)

    syms = "\n".join(
        [
            resistor_block("R1", "1k", 88.9, 38.1, 90, new_uuid(), new_uuid(), new_uuid()),
            resistor_block("R2", "1k", 88.9, 35.56, 90, new_uuid(), new_uuid(), new_uuid()),
            led_block("D1", "CHRG", 96.52, 38.1, new_uuid(), new_uuid(), new_uuid()),
            led_block("D2", "STDBY", 96.52, 35.56, new_uuid(), new_uuid(), new_uuid()),
        ]
    )

    insert = "\n".join(junctions + wires) + "\n" + syms + "\n"
    marker = '\t(symbol\n\t\t(lib_id "Device:R")\n\t\t(at 130.81 52.07 0)'
    if marker not in text:
        raise RuntimeError("R3 marker not found — schematic layout changed?")
    text = text.replace(marker, insert + marker, 1)
    return text


def main() -> None:
    text = SCH.read_text()
    out = patch(text)
    SCH.write_text(out)
    print(f"Patched {SCH}")


if __name__ == "__main__":
    main()