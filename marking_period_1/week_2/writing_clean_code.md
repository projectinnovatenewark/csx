Writing readable code is really important! If you're working on a project with a group, it's imperative to set coding conventions (rules to writing code) that are mutually understood. One way to set rules for this is by using a "linter". For this, we will install a python extension in VS Code.

Shift + Command + P, then "python enable linting", then "on" then input this code into the "settings.json" file that comes up.

{
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "files.autoSaveDelay": 2500,
    "python.linting.pylintArgs": ["--max-line-length=100"]
}