from code.category_report import build_category_report
from pathlib import Path


def test_build_category_report(tmp_path):
    src = tmp_path / 'events.txt'
    dst = tmp_path / 'summary.txt'
    src.write_text('a\na\nb\n', encoding='utf-8')
    build_category_report(str(src), str(dst))
    assert Path(dst).read_text(encoding='utf-8').strip().splitlines()[0] == 'a: 2'
