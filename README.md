# Minute-first time-card arithmetic checks

An original educational example by Leon Reed, maker of Calculator Toolkit. Eight small synthetic cases show why a two-decimal duration display should not become an input to a monetary calculation. These are fabricated arithmetic fixtures, not employee records, payroll data or a model performance benchmark.

## A concrete counterexample

One minute at $20/hour gives $0.33 after rounding the final money amount. Rounding duration first to 0.02 hours and multiplying by $20 gives $0.40.

For 09:05–12:00 and 12:40–17:20, the worked intervals are 175 and 280 minutes. The unpaid 40-minute gap is omitted in this illustrative record. Total:455 minutes or7h35m. At a single $21 rate, exact-minute gross is $159.25; using the displayed7.58 hours gives $159.18. A second week of460 minutes makes915 minutes combined and $320.25 at that same rate.

Try the related [Time Card Calculator](https://calculator-toolkit.com/time-card-calculator/) for a browser interface. Disclosure:I make the linked product. This reference deliberately covers exact-minute arithmetic only; overtime premiums, deductions, contractual break rules, local wage law and daylight-saving elapsed time are outside its scope. It is independently authored educational code, not a copy of the application implementation.

## Reproduce

Save `minute-pay-fixtures.csv` and `verify_minute_pay.py` in the same directory. Run `python verify_minute_pay.py` with Python3; no dependencies. Decimal arithmetic uses final-cent ROUND_HALF_UP. Expected outputs are provided separately from inputs, not as model features. The verifier checks8 rows, independently reconstructs the455-minute split day, combines two weeks and rejects negative minutes/rates. A different payroll rounding convention may produce different results; these fixtures do not establish entitlement.

## Columns

`case_id`: synthetic scenario label; `minutes`: nonnegative integer duration; `rate_usd`: illustrative decimal dollars/hour; `display_hours_2dp`: rounded duration for reading; `gross_from_minutes`: money from exact minutes; `gross_from_display`: deliberately early-rounded comparison. No real people or employer data.

## License and limits

MIT applies only to this original educational code, synthetic CSV and documentation. Copyright2026 Leon Reed. No production application source, website license, customer data or protected capability is released. This small fixture set is not exhaustive and makes no payroll-compliance claim.
