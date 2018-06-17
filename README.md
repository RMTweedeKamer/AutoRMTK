
# Mirror AutoRMTK
[See https://gitlab.com/RMTweedeKamer/AutoRMTK](https://gitlab.com/RMTweedeKamer/AutoRMTK)

## Setup

1. Execute:

```
pip install -r requirements.txt
cp .env.example .env
```

2. Set environment variables in `.env`

3. Set cronjobs to `python create_results.py "EK STEMMING"` and `python create_results.py "TK STEMMING"`

4. Execute `python main.py`.
