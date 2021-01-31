# life-calendar

This is a [Life Calendar][life-weeks] generator.

To generate one--as there's no required lib other than python3--all you need to do is `make run bdate=YYYY-MM-DD` with your own birthday.

I, myself, made a line of cronjob to run this file every hour,

```bash
0 * * * * cd /Users/damiann/Developer/life-calendar && make run bdate=YYYY-MM-DD
```

to keep it updated and remind myself every hour I'm being not productive (neither to myself nor others).

---

TODO:

- handle `weeks` and `years` more generally


[life-weeks]: https://waitbutwhy.com/2014/05/life-weeks.html
