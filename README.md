# Automatic Project Builder

This is an automated project repository builder that will generate a project structure typical to a programming language of your choosing!  

Example python project generated with the program:

```
project_name
|
│── README.md
|── TODO.md
└── main.py  
```

All files are automatically populated with your specified project name and author.

## Dependencies

The builder uses jinja2 for its templates, and therefore this is required to run.    

Install all dependencies: ```pip3 install -r requirements.txt```

## How to run

- Make sure all dependencies from above are installed
- ```python3 main.py```

## Supported Programming Languages

- Python

Please create an issue if there is any other programming language you want to be supported.

## Authors

Simon Damberg
