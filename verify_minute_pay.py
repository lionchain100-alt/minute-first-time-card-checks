"""Original educational arithmetic; not production application source."""
import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

def cents(x):
    return x.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

def gross(minutes, rate):
    if minutes < 0 or Decimal(rate) < 0:
        raise ValueError("Minutes and rate must be nonnegative")
    return cents(Decimal(minutes) * Decimal(rate) / 60)

def verify():
    rows = list(csv.DictReader(Path(__file__).with_name("minute-pay-fixtures.csv").open()))
    for row in rows:
        m, rate = int(row["minutes"]), Decimal(row["rate_usd"])
        display = cents(Decimal(m) / 60)
        assert display == Decimal(row["display_hours_2dp"]), row["case_id"]
        assert gross(m, rate) == Decimal(row["gross_from_minutes"]), row["case_id"]
        assert cents(display * rate) == Decimal(row["gross_from_display"]), row["case_id"]
    assert (12*60 - (9*60+5)) + (17*60+20 - (12*60+40)) == 455
    assert gross(455+460, "21") == Decimal("320.25")
    for m, r in [(-1, "20"), (1, "-20")]:
        try:
            gross(m, r)
        except ValueError:
            pass
        else:
            raise AssertionError("Negative values must fail")
    print(f"{len(rows)} fixtures, split-day, combined-week and negative-input checks passed")

if __name__ == "__main__":
    verify()
