import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 481) - 973
    _mask = _data(524, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = 'J,lGN@5~XOV3k!GfHh38BxD4Tr7bIL'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
