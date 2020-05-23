from flask import Flask

app = Flas(__name__)

#post

# Get /store

# Get /store/<string:name>

# GEt /store/<string:name>/item

# post /store data: {name: }

# post /store/<string:name>/item

app.run(port=5001)

