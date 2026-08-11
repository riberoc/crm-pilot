import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 583) - 688
    _mask = _data(260, None)
    _enc = 146
    return _mask, _enc

def run():
    matrix = 'u oE8zh],w@&!-zmUu5L:;Op{]NEgc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
