# Y

Automate actions for large amounts of files.

## Install

`//TODO : ADD INSTALL INSTRUCTIONS`

## YFILE

### In the `YFILE` you can set the rules for your enviorment

### Example YFILE

```yml
y: 1.0.0 #Version of Y
name: "example"
setup: "setup.y" #Runs on the project setup.
start: "start.y" #Runs when you run y in the project folder.
update: "b.y" #Runs on file updates
version: "1.0.0" #Version of this file (use for your own purposes)
```

### Example *.y file

```y
("*.js","node $file")   # Execute Command on any file matching the selector. Runs from the location of the YFILE
(none,"") # Execute Command
```

### VARIABLES

`$file` gets replaced with the current file  
`$random` random int  
`$timestamp` current timestamo  
`$os` either `win` or `other`

### OS SPECIFIC code

```y
["win",
("*.bat","start $file")
]
["other",
("*.sh","chmod +x $file && bash $file")
]
```
