import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 147) - 868
    _mask = _data(1181, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = 'rAEoYW%}X4#M|j a`^Fi;OfWugWK%O'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
