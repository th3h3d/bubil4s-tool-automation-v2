Configurations
=========================

There are two type of configs, one for framework and one for tools.

--------------

Framework Configs
================
----------------------------------------------

_ENABLED_CONFIGS
-----

```
[SETTINGS]
_ENABLED_CONFIGS = NAME_TEXT|INPUT_OUTPUT_PATH|SUB_DOMAIN_FILE
```

Used for activation of other framework configs, it uses '|' as delimiter.

All defined configs under '_ENABLED_CONFIGS' will be resolved in one loop.


<config name\>_TEXT
-----

Used for single text definition, for example target domain name.

```
NAME_TEXT = tesla
DOMAIN_TEXT = tesla.com
```

<config name\>_PATH
-----

Used for directory definition, for example input/output file directory.

```
INPUT_OUTPUT_PATH = ./in_out
```

<config name\>_FILE
-----

Used for single file name definition, for example subdomains.txt or C://subdomains.txt.

```
SUB_DOMAIN_FILE = ALL_SUB_DOMAINS.txt
```

Tools Configs
=============
----------------------------------------------

_ENABLED_CONFIGS
-----

```
[SETTINGS]
_ENABLED_CONFIGS = _ENABLED_AMASS|_ENABLED_GOSPIDER|_ENABLED_SUBFINDER
```

Used for activation of other tools' configs, it uses '|' as delimiter.

All defined configs under '_ENABLED_CONFIGS' will be resolved in one loop.


\_ENABLED_<tool name\>
-----

Used for activation of tool configs, it uses '|' as delimiter.

this should be provided to '_ENABLED_CONFIGS' of tool configs

```
_ENABLED_AMASS = AMASS_TOOL_PATH|AMASS_CUSTOM_COMMAND
AMASS_TOOL_PATH = /usr/bin/amass
AMASS_CUSTOM_COMMAND = ?

```


--------
Thanks to people those who build these small, cute pentest tools so that we can compine them.