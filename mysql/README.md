# CcinnSearch-docker-mysql

```
docker build -t ccinn-search-mysql-image .
```

```
docker run -d --name ccinn-search-mysql -v "$PWD"/data:/var/lib/mysql -p 3308:3306 ccinn-search-mysql-image
```