# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/waz5211/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/waz5211/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A single-image summary of Thursday 19 November 2026 world news,
drawn as a newspaper front page: masthead, the date, a lead story
on the first-ever Trump–Xi–Putin trilateral summit in Shenzhen
(with the three flags), and twelve more stories — Ukraine's third
strike on the Kerch Bridge, Iran widening attacks to Kuwait and
Bahrain amid the Hormuz crisis, the World Court's Rohingya ruling,
Anthropic's IPO priced at $83, COP31 talks in Antalya, IMF chief
Georgieva's warning that global inflation hit 4.7%, Hakeem
Jeffries set to become the first African-American Speaker, measles
spreading again in the US, a Van Gogh selling for $190.4 million,
unrest in Bangladesh, North Korea expanding uranium enrichment,
and a Houthi missile damaging a Saudi wealth fund tower in Riyadh.

Everything in the image is drawn programmatically with Pillow
(`build_image.py`); there is no AI-generated imagery or text in it.

## Files

- `entry.png` — the entry image (1024×1024, PNG, under 1 MiB)
- `main.py` — entrypoint: copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (stdlib only)
- `build_image.py` — regenerates `entry.png` (needs Pillow)

## Run it

```sh
python3 build_image.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref={referral_code}&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
