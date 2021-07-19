
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
          body: "name="+name,
          headers: {
            Accept: "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
          },
          method: "POST"});
          window.location.reload();
        }
    },
    async created() {
      const response = await fetch( "/api/getServices" );
      this.running_services = await response.json();
    }
}

Vue.createApp(app).mount('#app')