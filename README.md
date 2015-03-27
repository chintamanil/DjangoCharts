# Djang Charts

## Description

Django charts is buit wiyth pure python. There is no Javascript. The idea was to use pure python libraries and templating system to develop Charts in django. I m using  django chartkit library to show a JSON. django view is sending the JSON object.
 I was using a FITBIT Data. I could Import fitbit xls into my database. And SHOW data like waling and sleeping activity.

## Stack

* Django
* Bootstrap
* Django chartit
* Postgres

## Features

- [x] Import Data from XLS
- [x] Show Charts for users waling and sleeping activity
- [x] Show Charts for users height weight
- [x]  Show users Score
- [x] Login and logout for user  

## Installation

```bash
Django_Charts$ pip install -r requirements.py
Django_Charts$ python manage.py make migrations
Django_Charts$ python manage.py migrate

## Run
Django_Charts$ pthon manage.py runserver
You can now open your browser: `http://localhost:8000/`
 `http://localhost:8000/import_db`  :: this will import the csv file into the database. [crude way]

## Licence
The MIT License (MIT)

Copyright (c) 2014 Chintamani Lonkar (chintamani.lonkar@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.



