import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 967) - 384
    _mask = _data(387, None)
    _enc = 199
    return _mask, _enc

def run():
    matrix = 'D}$ .?HlS]gssAqH<zpdTa~[WNndGQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
