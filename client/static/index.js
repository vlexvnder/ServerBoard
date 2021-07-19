
const app = { 
    delimiters: ['[[', ']]'],
    data() {
        return ({
          running_services : null,
          available_services : [{name: "Code-Server"},
            {name: "app3"},
            {name: "app4"}]

    })
    },
    async created() {
      const response = await fetch( "/api/getServices" );
      running_services = response;
    }
}

Vue.createApp(app).mount('#app')