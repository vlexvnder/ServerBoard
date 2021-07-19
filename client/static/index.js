import axios from 'axios';

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
          running_services : null,
          available_services : [{name: "Code-Server"},
            {name: "app3"},
            {name: "app4"}]

    })
    },
    async created() {
      const response = await axios.get("/api/getServices");
      running_services = response.data
    }
}

Vue.createApp(app).mount('#app')