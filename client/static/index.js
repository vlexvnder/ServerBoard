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

app.component('service',{
    props: ['s'],
    template: ` <div class="ui card">
                    <div class="content">
                        <div  class="header">
                        [[ service.name ]]
                        </div>
                        <div class="meta">[[ service.status ]]</div>
                        <div class="description">
                        <p>
                            [[ service.info ]]
                        </p>
                        </div>
                    </div>

                    
                </div>`
})
Vue.createApp(app).mount('#app')