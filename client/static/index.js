
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
      this.running_services = response.json();
    }
}

Vue.createApp(app).mount('#app')