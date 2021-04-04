
function getContainers(url) {
var containers;
fetch( url )
  .then(response => response.json())
  .then(json => containers = json)
  .then(console.log(containers));
}
const app = { 
    delimiters: ['[[', ']]'],
    data() {
        return ({
          running_services : [
              {
                  name: "Heimdall",
                  status: "Online",
                  info: "A remote IDE",
                },
              {name: "Code-Server"},
              {name: "app3"},
              {name: "app4"}
          ],
          available_services : []

    })
    }
}

Vue.createApp(app).mount('#app')