import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 946) - 886
    _mask = _data(1982, None)
    _enc = 145
    return _mask, _enc

def run():
    matrix = '4,@VLj! {L!85<A9q5qj$s&OGuo5MK'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
