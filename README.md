# jinjaroot

## Installation

```
pip install jinjaroot
```

## Basic usage

Put a `.jinjaroot` folder in the root directory of your repo with jinja2 template files (do not add the .j2 extension to these; can be recursive directory structure)

Add a `jinjaroot.yaml`  with the data to be filled in

Also add `<filename>.j2` files adjacent to any other files

Then just run

```
jinjaroot generate
```

at the root directory of your repo.

For more information, use:

```
jinjaroot --help
```
