# LCloud-task
LCloud test task

### Installation

1. Clone repository
```
git clone https://github.com/EnotShow/LCloud-task/
```
2. Install dependencies
```
pip3 install -r LCloud-task/requirements.txt
```
3. Install script as terminal cli
```
chmod +x LCloud-task/main.py
sudo mv -R LCloud-task /usr/local/bin/LCloud-task
sudo ln -s /usr/local/bin/LCloud-task/main.py /usr/local/bin/lcloud
```

### Usage

#### Authentication
```
lcloud auth
```
```
lcloud --access-key {access-key} --secret-key {secret-key}
```

#### List bucket files
```
lcloud list --bucket {bucket} --regex {regex} --prefix {prefix} 
```

#### List upload file
```
lcloud --bucket {bucket} --file {local-file-path} --key {key} --prefix {prefix}
```

#### Delete files
```
lcloud --bucket {bucket} --regex {regex} --prefix {prefix}
```