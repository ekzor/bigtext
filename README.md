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

Use quotation marks to get spaces:
```
$ ./bigtext.py -r "foo bar" "HELLOWORLD"

HELLOW  ORLDHE  LLOWOR     LDHEL   LOWORL  DHELL
OW      OR  LD  HE  LL     OW  OR  LD  HE  LL   O
WORL    DH  EL  LO  WO     RLDHE   LLOWOR  LDHEL
LO      WO  RL  DH  EL     LO  WO  RL  DH  EL  L
OW      ORLDHE  LLOWOR     LDHELL  OW  OR  LD   H

```
