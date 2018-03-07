# bigtext
generate obnoxious large ascii-art text made out of strings

```
$ ./bigtext.py FOO BAR

BARBAR  BARBAR  BARBAR
BA      RB  AR  BA  RB
BARB    AR  BA  RB  AR
BA      RB  AR  BA  RB
BA      RBARBA  RBARBA
```

Options that matter:
* `-r, --nolinereset`: don't reset the string's position when going to the next line.

```
$ ./bigtext.py -r FOO BAR

BARBAR  BARBAR  BARBAR
BA      RB  AR  BA  RB
ARBA    RB  AR  BA  RB
AR      BA  RB  AR  BA
RB      ARBARB  ARBARB
```

* `-p, --padding`: replace spaces inside characters and between words with another character
```
$ ./bigtext.py -p . FOO BAR

BARBAR..BARBAR..BARBAR
BA......RB..AR..BA..RB
BARB....AR..BA..RB..AR
BA......RB..AR..BA..RB
BA......RBARBA..RBARBA
```
