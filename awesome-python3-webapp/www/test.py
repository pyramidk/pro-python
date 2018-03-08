import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='root', db='awesome')
    
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop.run_until_complete(test())