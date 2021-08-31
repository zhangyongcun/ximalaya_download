### 喜马拉雅专辑频道批量下载



下载工具使用 aria2p，请先安装 aria2 并开启 rpc：

```shell
pip install aria2p
```

先修改，album_id 的值，从网页地址中获取。

![](id.png)

修改 base_download_path，默认下载地址。

然后执行就可以批量下载了。

```shell
python xmly.py
```