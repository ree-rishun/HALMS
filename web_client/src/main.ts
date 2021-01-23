import Vue from 'vue'
import App from './App.vue'
import router from './router'
import firebase from 'firebase/app'

const firebaseConfig = {
    apiKey: "AIzaSyBAWq7qqMPPNpgB32LJnmgqhtv-Fg7LE8E",
    authDomain: "halms-49316.firebaseapp.com",
    databaseURL: "https://halms-49316-default-rtdb.firebaseio.com",
    projectId: "halms-49316",
    storageBucket: "halms-49316.appspot.com",
    messagingSenderId: "653309576534",
    appId: "1:653309576534:web:12ee2d11d56069f5ba02f7",
    measurementId: "G-V7F6VK55XD"
}

firebase.initializeApp(firebaseConfig)
window.firebase = firebase

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
