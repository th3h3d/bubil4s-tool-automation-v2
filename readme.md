Tool Automation Framework
=========================

This tool is a POC for tool automation. Different type tools can be added, modified and executed.

Mostly being used for Pentest Recon.

Supports
--------
----------------------------------------------
- Parallel tool execution

- Group execution

- Predefined command execution

- Custom command execution

- Extendable functionality (under Python)


Usage
-----
---------------------------------------------

List Executable Processes

```
▶ python -m pytest --setup-plan --disable-pytest-warnings
```


Execute Single Process - (Specific Name)

```
▶ python -m pytest -m asnlookup_get_ipv4_space -v --disable-pytest-warnings
```


Execute Grouped Processes - (Commonly defined name)

```
▶ python -m pytest -m recon -v --disable-pytest-warnings
```


Execute Grouped Processes in Parallel  - (Commonly defined name)

```
▶ python -m pytest -m recon -n 5 -v --disable-pytest-warnings
```

--------
Thanks to people those who build these small, cute pentest tools so that we can compine them.