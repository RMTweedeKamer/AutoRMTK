import reddit
from jinja2 import Template

from responders import VoorzitterResponder, StemmingResponder

responders = [
  VoorzitterResponder(),
  StemmingResponder()
]

for comment in reddit.client().subreddit('rmtk').comments():
    comment.refresh()

    if "meta" in comment.body.lower():
        continue
    if [1 for c in comment.replies.list() if c.author.name == 'AutoRMTK']:
        continue

    responses = [response for response in
      [responder.respond(comment) for responder in responders] if response != None]

    print(comment.body)
    print(comment.id)

    if len(responses) < 1:
      continue

    rendered_responses = [
      Template(open('templates/responses/' + r['template'] + '.md').read()).render(response=r)
        for r in responses
    ]

    response_text = Template(open('templates/response.md').read()).render(rendered_responses=rendered_responses)

    import code; code.interact(local=dict(globals(), **locals()))
