# line to ifttt bridge

* Receive LINE Message hook and send message text to IFTTT

#### deploy

1. set up apex http://apex.run/
2. execut init to create iam role. input project name you like.
```
apex init
```
3. remove created `hello` project.
4. execute apex like this:
```
apex deploy -s IFTTT_URL=...
```
