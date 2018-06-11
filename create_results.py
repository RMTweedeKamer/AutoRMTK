import reddit
from submissers import ResultatenSubmisser
from jinja2 import Template

def main():
  last_stemming = next(reddit.client().subreddit('rmtk').search('flair:"TK STEMMING"', limit=1, sort='new'))
  results = ResultatenSubmisser().submiss(last_stemming)

  text = Template(open('templates/submissions/resultaten.md').read()).render(results)

  reddit.client().redditor('-___-_').message(results['title'], text)
  reddit.client().subreddit('rmtk').message(results['title'], text)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        from raven import Client
        import os

        print(e)
        print('*****')

        client = Client(os.getenv('SENTRY_URL'))
        client.captureException()
