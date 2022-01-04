# OCW Resources Grabber
Download the lecture notes and video lectures from MIT Open Cource Ware Website.

TBH, you could do that with the following wget command in 'nix [^1] - 

```
wget -A pdf,jpg -m -p -E -k -K -np http://site/path/ 
``` 

### But why did I create this script then ?
> I was getting bored.

## How to use the script - 

```
python ./scr/main.py <ocw link of notes or videos page> <file extention>
```

> This will create a folder on the `root` directory with current timestamp and you can move to the desired location and rename it as you like. 


[^1]: https://stackoverflow.com/questions/8755229/how-to-download-all-files-but-not-html-from-a-website-using-wget