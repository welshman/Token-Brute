@echo off
title Token Brute
SET /A X=0
:loop
cls
echo ====================
echo        Running
echo ====================
echo Loop = %X%
py gen.py > nul
py checker.py > nul
del tokens.txt
copy NUL tokens.txt > nul
SET /A X+=1
goto loop