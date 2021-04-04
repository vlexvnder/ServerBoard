const app = { 
    delimiters: ['[[', ']]'],
    data() {
        return ({
          available_services : [
              {
                  name: "Heimdall",
                  status: "Online",
                  info: "A remote IDE",
                },
              {name: "Code-Server"},
              {name: "app3"},
              {name: "app4"}
          ],
          running_services : []

    })
    }
}

Vue.createApp(app).mount('#app')