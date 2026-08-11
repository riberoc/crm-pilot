import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 627) - 121
    _mask = _data(731, None)
    _enc = 55
    return _mask, _enc

def run():
    matrix = '3>Eo!QIM|>aZr$S!(:qk^<,% >Vaa!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
