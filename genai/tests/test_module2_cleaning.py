from code.module2_cleaning import clean_signups


def test_clean_signups_runs(tmp_path):
    src = tmp_path / 'raw.csv'
    dst = tmp_path / 'clean.csv'
    src.write_text('date,channel,signups\n2026-01-01, Email ,2\n', encoding='utf-8')
    clean_signups(str(src), str(dst))
    assert dst.exists()
