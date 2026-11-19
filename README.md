# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/waz5211/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/waz5211/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A newspaper front page summing up the world's news of Thursday 19 November 2026. The lead story is the first-ever Trump–Xi–Putin trilateral summit in Shenzhen, held on the sidelines of APEC with Ukraine and nuclear arms control on the table. Below it, twelve short stories cover the day across regions and beats: Ukraine's third strike in four days on the Kerch Bridge, Iran widening attacks to Kuwait and Bahrain as the Strait of Hormuz crisis deepens, the International Court of Justice ruling on the Rohingya genocide case, Anthropic's IPO priced at $83 a share, COP31 ministers in Antalya, the IMF chief warning global inflation has hit 4.7%, Hakeem Jeffries set to become the first African-American Speaker of the US House, measles spreading again in the US, a Van Gogh selling for $190.4 million, unrest in Bangladesh, North Korea's expanded uranium enrichment, and a Houthi missile damaging a Saudi wealth fund tower in Riyadh. The page is drawn from scratch with Pillow: masthead, lead block with a globe and the three leaders' flags, and a numbered three-by-four story grid, each story with its own small motif.

## Run it

```sh
python3 build_image.py
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

`main.py` copies the 1024×1024 PNG drawn by `build_image.py` to `$MAKEFUN_OUTPUT_DIR/entry.png`; running it twice produces identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref={referral_code}&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
