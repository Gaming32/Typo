python3 -m PyInstaller "./typo/lang/__main__.py" -F -n "Typo Script" --add-data "./typo/lang/_quits.py:./typo/lang" --add-data "./typo/lang/_built_in_cmds.py:./typo/lang"
