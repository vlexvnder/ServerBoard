# ServerBoard
🔨 Work in progress 📏
⚠️ Do not use in a production environment. Only tested on Ubuntu 20.04. Possible bugs. ⚠️

ServerBoard is my all-in-one server management dashboard. Currently, it supports running containers via docker-compose, monitoring containers, removing containers, and managing server power. 

![image](https://user-images.githubusercontent.com/38928216/126381669-48e56693-0832-472b-859c-e40bdbddc7d6.png)
ServerBoard with two availible compose files. Heimdall is running; code-server is not, but is availible.

New containers can be added by putting a docker compose file in the compose_files directory and adding details to config/containers.json
