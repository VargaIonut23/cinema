import string
import random


def unique_strings(k: int, ntokens: int,
                   pool: str = string.ascii_letters) -> set:
    'creeza un string unic'
    seen = set()

    join = ''.join
    add = seen.add

    while len(seen) < ntokens:
        token = join(random.choices(pool, k=k))
        add(token)
    return seen


def unique_number() -> int:
    'alege un numar intre 1800 - 2021'
    return random.randint(1800, 2021)


def inProgram() -> str:
    'alege intre da sau nu'
    items = ['da', 'nu']
    return random.choice(items)
