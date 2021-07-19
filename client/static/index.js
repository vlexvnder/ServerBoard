
const app = { 
    delimiters: ['[[', ']]'],
    data() {
        return ({
          running_services : null,

    })
    },
    methods : {
      postData : async function(url, name){
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: "name="+name
        });
      }
    },
    async created() {
      const response = await fetch( "/api/getServices" );
      this.running_services = await response.json();
    }
}

Vue.createApp(app).mount('#app')