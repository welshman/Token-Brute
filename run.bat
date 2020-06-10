@echo off
title Token Brute
echo ====================
echo        Running
echo ====================
py gen.py > nul
py checker.py > nul
del tokens.txt
copy NUL tokens.txt > nul