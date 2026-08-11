import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 649) - 945
    _mask = _data(1548, None)
    _enc = 197
    return _mask, _enc

def run():
    matrix = 'N-yBXH{LWk<X9we{w ;PC/u%#OaKBj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
