# German translation — consistency items for review

Reviewer notes for `assets/enroute_de.ts`. These are **consistency / stylistic
choices**, not outright errors, so they were left for you to decide on. The
🔴 meaning errors and 🟠 typo/grammar fixes from the same review have already
been applied to the file.

For each item below, pick a preferred form and we can apply it consistently
across the file.

---

## 1. Number formatting (German conventions)

German uses `.` as the thousands separator and `,` as the decimal separator.
A few strings still use the English convention:

- `TrafficReceiver` — *Traffic is considered relevant…*: `1,500 m` → should be
  `1.500 m` (currently reads as "1.5 m" to a German speaker). The same string
  has `20 NM` which is fine.
- `TrafficReceiver` — *…standard pressure of 1013.2hPa…*: `1013.2 hPa` → should
  be `1013,2 hPa`.
- Elsewhere `5.000 ft` and `9.500 ft` are already done correctly — these two are
  the outliers.

## 2. Ellipsis character

Three styles are mixed throughout the file:

- `…` (proper single-character ellipsis, U+2026) — e.g. `Umbenennen…`
- ` ...` (space + three periods) — e.g. `Entfernen ...`, `Verbinde erneut ...`
- `...` (three periods, no space) — e.g. `Disconnecting...` → `Löse Verbindung...`

Qt source strings mostly use `…`. Recommendation: normalise everything to `…`
(no leading space).

## 3. "Aircraft" — term varies

The English *Aircraft* / *aircraft* is rendered as all of:

- `Luftfahrzeug` (most common, neutral)
- `Lfz.` (abbreviation, with period) — e.g. `Lfz. überschreiben?`
- `Lfz` (abbreviation, no period) — e.g. `Lfz-Bibliothek`
- `Flugzeug` — e.g. in the OGN/callsign help texts

Recommendation: pick `Luftfahrzeug` for body text and one fixed abbreviation
(`Lfz.`) where space is tight; avoid `Flugzeug` unless "aeroplane" is really
meant (it excludes gliders/helicopters).

## 4. "Trip kit" capitalisation

Mixed: `TripKit`, `Tripkit`, `Trip-Kit`, `trip kit`. The English source is also
inconsistent (and even has the typo "TripKip"). Recommendation: settle on one
form, e.g. `TripKit`.

## 5. "socket" — term varies

Within the Bluetooth/network classes:

- `Traffic::TrafficDataSource_AbstractSocket` keeps the English `Socket`
  (e.g. *Socketvorgang*, *Der Socket benutzt einen Proxy…*).
- `Traffic::TrafficDataSource_BluetoothClassic` translates it as `Anschluss`
  (e.g. *Der Anschluss versucht, sich zu verbinden.*).

Recommendation: use one term for the same concept across both contexts.

## 6. Weather: "rime icing"

`Weather::Decoder` renders *rime icing* three different ways:

- `Light rime icing in cloud` → `Leichter Eisansatz in Wolken`
- `Moderate rime icing in cloud` → was *"gemischte Vereisung"* (wrong; **already
  fixed** to `Mäßiger Eisansatz in Wolken`)
- `Severe rime icing in cloud` → `Schwere Eiskristalle in Wolken`

The precise term for rime ice is **Raueis** (vs. *Klareis* = clear ice, already
used correctly). Recommendation: decide between the simple `Eisansatz` family or
the precise `Raueisansatz`, and apply to all three (the "severe" one currently
says *Eiskristalle*, ice crystals, which is a different phenomenon).

## 7. Weather: "small hail" / "ice pellets"

- *small hail* appears as `Graupel`, `Frostgraupel`, and `kleiner Hagel`.
- *ice pellets* / *ice pellet precipitation* appears as `Eiskörner`,
  `Eiskugeln` (and previously `Hagelschlag`, **already fixed** to `Eiskugeln`).

Recommendation: meteorologically, *small hail / snow pellets* = **Graupel** and
*ice pellets* = **Eiskörner**. Consider standardising on those and applying
consistently (the `light/moderate/heavy ice pellet…` entries currently use
`Eiskugeln`).

## 8. "true north/south/east/west"

Rendered as `geografisch Nord` etc. The aviation-standard German term is
`rechtweisend Nord`. `geografisch` is correct and clear; flagged only in case you
prefer the navigation idiom.

## 9. "Statute miles"

- `AircraftPage`: `Statute Miles` → `Britische Meilen`
- `Weather::Decoder`: `statute miles` → `brit. Meilen`

Statute miles are not British-specific. Recommendation: `Landmeilen`
(this was also noted in the main review under terminology).

## 10. `demselben` / `derselben` written as two words

- `SettingsPage`: *…mit dem selben Protokoll…* → `demselben`
- `Traffic::TrafficDataSource_Abstract`: *…mit der selben 'Radio-ID'…* → `derselben`

Modern spelling writes these as one word.

## 11. Minor: double spaces

A handful of strings contain a stray double space, e.g.:

- `QObject`: `Service:  Serieller Port`
- `Weather::Decoder`: `schweres  Gewitter mit Niederschlag`,
  `Häufig  schwere Turbulenz in Wolken`
- `AircraftPage`: `nutzt  Enroute Flight Navigation`

Harmless, but easy to clean up in one pass.

## 12. Minor: `z.B.` vs `zB`

`Weather::Decoder` has one `zB` (*Reif auf dem Instrument (zB durch…)*) while the
rest of the file uses `z.B.`.

## 13. "Clear sky" → "Blauer Himmel"

`Weather::Decoder`: *Clear sky* → `Blauer Himmel` ("blue sky"). At night the sky
isn't blue; `Wolkenlos` or `Klarer Himmel` is more literal. Minor stylistic call.
