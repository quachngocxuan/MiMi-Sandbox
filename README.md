# MiMi-Sandbox

Test repository for [MiMi](https://mimi.novasell.vn)'s delegated coding agents (runner host,
spike to choose the default agent — CR010). MiMi's agents only ever push `mimi/*` branches;
`main` is protected (pull request required, no force push, no deletion) and changes only
through a reviewed merge.

- Code: `mimi_demo/` (standard library only, Python 3.12)
- Tests: `python -m unittest -q` (this is the project's `verify_cmd`)
- `main` carries one known bug on purpose: `is_leap_year` treats every year divisible by 4
  as a leap year (1900 is not). Its test fails until the bug is fixed.
