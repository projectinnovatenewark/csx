Linters are a way to format your code and set conventions for how you write it

Linters enforce rules that you set including things like how to name files, max line lengths for code, putting doctstrings at the top of your
python files, and many more applications you can learn about.

Linting helps collaborative teams my making sure they are all writing code in a similar format. Can you imagine working with 3 people
on a long-term project and when you merge all of the code together, it looks entirely different?! That is nightmare material.

You can go ahead and install pylint as an extension in VS Code. Then use Shift + Command (or control) + P and type "enable linting" to turn it 
on for Python. Then Shift + Command (or control) + P "Preferences: Open Settings(JSON)" and view the following lines of code that should already exist in your settings file.

{
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "files.autoSave": "onFocusChange",
    "python.linting.pylintArgs": ["--max-line-length=100"]
}