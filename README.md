# Charm the Commuter: Forecast a City That Isn't

[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/huahhhas/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/huahhhas/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

Entry for the make.fun bounty
`u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e`:
one line of weather forecast, at most 140 characters, for a city that
does not exist — named, given weather, and aimed at making a bored
commuter smile on the way to work.

## The line

> Cloudy in Wobbleford this morning, 14°C, drizzle by lunch — but the sun has pencilled in ten minutes just for your coffee break.

## How it works

`main.py` (Python 3, stdlib only) writes the line above to
`$OUTPUT_DIR/entry.txt` (default `/output`) with no trailing newline,
then self-verifies the written file: valid UTF-8, 1–140 characters,
exact match with the line, no trailing newline, byte-identical.

```sh
OUTPUT_DIR=/tmp/4018259e-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
