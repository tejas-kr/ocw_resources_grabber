# OCW Resources Grabber
Download the lecture notes and assignments&solutions  from MIT Open Course Ware Website.
## Why write this
Due the structure change of the MIT Open Course Ware Website, those old download scripts may fail to work.

In the past time, the notes' links are under the `../<course code>_<course name>/lecture-notes/`. But after some change, now only by clicking the the pdf button on notes page(`../<course code>_<course name>/pages/lecture-notes/`), can you enter a specific notes download page(`../<course code>_<course name>/resources/<course code>_lecxx`). And then, you can get the notes file by clicking `Download File` button again. There are same structure change for assignments&solutions.

So write a script to save time.

## How to use the script 

Run

```bash
python ./src/main.py <ocw link of notes or assignments&solutions page> <file extension>
```

For example, we want to download the lecture notes of *signal and systems*.

```bash
python ./src/main.py https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/pages/lecture-notes/ pdf
```

You can edit the **file name** and **folder name** in the `downloader.py` and `main.py`. The default script only remain the **last part** of the file name. In this example, the original file name is `e6c75426e220f1a406b0b9be1f55bbc1_MITRES_6_007S11_lec01.pdf`. The same as the assignments&solutions.

![image-20220817000621964](https://cdn.jsdelivr.net/gh/frinkleko/PicgoPabloBED@master/images_for_wechat/image-20220817000621964.png)

> This will create a folder on the `root` directory with FileExtension_\<course code>\_\<course name>  and you can move to the desired location and rename it as you like. 

## ToDo:

- [ ] video lectures download
