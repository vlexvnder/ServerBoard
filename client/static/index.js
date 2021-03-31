const app = { 
    delimiters: ['[[', ']]'],
    data() {
        return ({
          hi: 'Hello, Vue!'
    })
    }
}
Vue.createApp(app).mount('#app')