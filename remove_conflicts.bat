@echo off
FOR /R . %%A in (*の競合コピー*) DO del "%%A"
echo Dropbox's conflicted files are removed.
pause
