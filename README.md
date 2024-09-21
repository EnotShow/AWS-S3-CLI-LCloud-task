# LCloud-task
LCloud test task

### Installation

1. Clone repository
```
git clone https://github.com/EnotShow/LCloud-task/
```
2. Install package
```
cd LCloud
pip3 install .
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