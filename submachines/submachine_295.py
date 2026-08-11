import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 123) - 450
    _mask = _data(586, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = 'e~WIGXTY-h|} 1ij$gybUhPAS+`RA{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
