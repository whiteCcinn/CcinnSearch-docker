# CcinnSearch-docker

http://chromedriver.chromium.org/downloads

https://www.chrome64bit.com/index.php/google-chrome-64-bit-for-linux

```
docker build -t ccinn-search-main .
```

```
docker run -it --rm -v "$PWD":/usr/src/myapp/ --link ccinn-search-mysql:mysql ccinn-search-main bash
```

