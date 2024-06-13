import json

from creators.models import Creator
from contents.models import Content


f = open('scripts/creators.json', 'r')
data = json.load(f)

for item in data:
    content = item.pop('content')
    creator = Creator.objects.create(**item)
    Content.objects.create(creator=creator, url=content)