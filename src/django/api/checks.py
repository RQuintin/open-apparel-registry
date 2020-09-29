from watchman.decorators import check
from api.matching import GazetteerCache


@check
def gazetteercache():
    GazetteerCache.get_latest()
    return {'gazetteercache': 'ok'}
