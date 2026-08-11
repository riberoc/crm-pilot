import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 295) - 198
    _mask = _data(25, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = ':B?eEO@7u>V(LqB!cZC>C LGszE^VR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
