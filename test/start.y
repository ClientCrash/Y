[win,
("*.bat","start $file")
]

[other,
("*.sh","chmod +x $file && bash $file")
]

[any,
(*.js,"node $file")
]