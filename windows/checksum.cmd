FORFILES /p %1 /m *.* /c "cmd /c certutil -hashfile @file SHA1"
