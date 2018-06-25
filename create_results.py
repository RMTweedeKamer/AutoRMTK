import reddit
from submissers import ResultatenSubmisser
from jinja2 import Template
import sys

def main():
  last_stemming = next(reddit.client().subreddit('rmtk').search('flair:"' + sys.argv[1] + '"', limit=1, sort='new'))
  results = ResultatenSubmisser().submiss(last_stemming)

  text = Template(open('templates/submissions/resultaten.md').read()).render(results)

  reddit.client().subreddit(sys.argv[2]).submit(results['title'], text)

if __name__ == "__main__":
    try:
        print(sys.argv[1])
        print(sys.argv[2])
        main()
    except Exception as e:
        from raven import Client
        import os

        print(e)
        print('*****')

        client = Client(os.getenv('SENTRY_URL'))
        client.captureException()
