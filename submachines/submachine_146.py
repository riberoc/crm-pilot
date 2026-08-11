import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 941) - 652
    _mask = _data(199, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = 'wM9NpE F(Q><`(4RPR3/@mE<+9^~=<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
