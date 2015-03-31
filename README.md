## path2zip ##
This script is used to write all files found within a folder to a zip file, while keeping the same directory structure.

An example of how to call the script

```
    >>patch2zip.py "/path/to/folder/" "output_name" "^.*\.(zip|rar|tar|tar\.gz|7z)$"  
```

This call will zip all files with the extension zip,rar,tar,tar.gz and 7z into a zip file.