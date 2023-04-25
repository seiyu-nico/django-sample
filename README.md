# Django

## アプリケーションを追加するとき
- プロジェクトルートにアプリを作成すると、名前によってconfigの上下に来てしまうのでappsディレクトリを作成し、その中に各アプリを作成
```
mkdir apps
cd apps && python ../manage.py startapp hoge && cd ..
```
