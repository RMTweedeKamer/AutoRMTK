import reddit
from jinja2 import Template

from responders import VoorzitterResponder, StemmingResponder, EKResponder, EKTKResponder, TKResponder

def main():
    responders = [
        VoorzitterResponder(),
        StemmingResponder(),
        EKResponder(),
        EKTKResponder(),
        TKResponder()
    ]

    for comment in reddit.client().subreddit('rmtk').stream.comments().replace_more(limit=0):
        try:
            comment.refresh()
        except Exception as e:
            continue

        if comment.body and ("meta" in comment.body.lower() or comment.body == '[deleted]'):
            continue
        if [1 for c in comment.replies.list() if c and c.author and c.author.name == 'AutoRMTK']:
            continue
        if comment.author and comment.author.name in ['AutoRMTK', 'AutoModerator']:
            continue

        responses = [response for response in
          [responder.respond(comment) for responder in responders] if response != None]

        if len(responses) < 1:
          continue

        rendered_responses = [
          Template(open('templates/responses/' + r['template'] + '.md').read()).render(r)
            for r in responses
        ]

        response_text = Template(open('templates/response.md').read()).render(rendered_responses=rendered_responses)

        debug_permalink = comment.permalink

        comment.reply(response_text)

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
