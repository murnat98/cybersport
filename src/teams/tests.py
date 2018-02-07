import random
import string

from teams.models import Teams
from tournaments.tests import TestUUIDSharding, ShardTest


class TeamsTest(TestUUIDSharding, ShardTest):
    model = Teams
    names = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(1, 10))) for _
             in range(100)]  # Generate a random string of random length from 1 to 10
