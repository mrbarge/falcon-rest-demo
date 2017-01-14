falcon-rest-demo
================

This is a simple falcon-based app to explore some of its (and SQLAlchemy's) basic usage.

### See Also ###

This project is modelled after my other flask-ajaxdatademo project, which offers a similar
flask-driven API:

* https://github.com/mrbarge/flask-ajaxdatademo


### Installation ###

Initialise the database with some dummy entries constructed from a dictionary of words,
then run the app:

```bash
python dbinit.py /usr/share/dict/words app.db
gunicorn main:application
```

### See Also ###

* https://github.com/pallets/flask
* https://github.com/rosickey/flask-datatables
