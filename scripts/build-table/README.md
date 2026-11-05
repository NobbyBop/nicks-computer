# build-table.py
The purpose of this file is to read the main project directory for HTML files and automatically generate a table of works in the main `index.html` page.

## Naming format
This program expects files to be named like: `type-mmddyyyy-title_with_underscores`
- `type` is `exp` for Experiment, `proj` for Project, and `blog` for Blog.
- `date` is mmddyyyy formatted date`
- `title` maintains its capitalization, underscores are replaced with spaces

## Sorting
The works are sorted by date, the newest entries will appear at the top of the table.

## Injection
The new table will overwrite the original table in the HTML File. 