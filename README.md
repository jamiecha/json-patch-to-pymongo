
# jsonpatch2pymongo

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jsonpatch2pymongo)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://github.com/jamiecha/jsonpatch2pymongo/actions/workflows/check.yml/badge.svg)](https://github.com/jamiecha/jsonpatch2pymongo/actions/workflows/check.yml)
[![Publish to PyPI](https://github.com/jamiecha/jsonpatch2pymongo/actions/workflows/release.yml/badge.svg)](https://github.com/jamiecha/jsonpatch2pymongo/actions/workflows/release.yml)


## Introduction
- This is a port of [jsonpatch to mongodb](https://www.npmjs.com/package/jsonpatch-to-mongodb) and [jsonpatch to mongodb - golang](https://github.com/ZaninAndrea/json-patch-to-mongo/blob/main/main.go) into python language.
- Anyone who want to apply differences between 2 JSON data into mongodb using pymongo's update_many() function will be beneficial from this.

## How to use
First, you need to get patch list generated by [jsonpatch](https://pypi.org/project/jsonpatch/) package.
```python
>>> src = {'foo': 'bar', 'numbers': [1, 3, 4, 8]}
>>> dst = {'baz': 'qux', 'numbers': [1, 4, 7]}
>>> patch = jsonpatch.JsonPatch.from_diff(src, dst)
# or equivalently
>>> patch = jsonpatch.make_patch(src, dst)
>>> patch.patch
[{'op': 'remove', 'path': '/foo'}, {'op': 'add', 'path': '/baz', 'value': 'qux'}, {'op': 'remove', 'path': '/numbers/1'}, {'op': 'add', 'path': '/numbers/2', 'value': 7}, {'op': 'remove', 'path': '/numbers/3'}]
```
Once patch(list of each patch) is available, you can pass it to this function
```python
>>> update = jsonpatch2pymongo(patch.patch)
>>> update
{'$set': {'baz': 'qux'}, '$unset': {'foo': 1, 'numbers.1': 1, 'numbers.3': 1}, '$push': {'numbers': {'$each': [7], '$position': 2}}}
```
And finally, you can pass `update` into pymongo's update or update_many function
```python
db.collection.update_many(filter, update)
```

## Testcases
- Install pytest package and run `python -m pytest -v` under root directory.
- Then pytest will automatically run test_main.py which includes various test cases ported from the original javascript test cases.

## Code style
- `black -l 100`

## Setup pre-commit hook
- Plugins specified in `.pre-commit-config.yml` will be used before you commit changes.
- How to enable pre-commit hook
```bash
pip install pre-commit
pre-commit install
```
