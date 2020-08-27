import Vue from "vue";



Vue.config.productionTip = false

Vue.component("hello-world", () => import("@components/HelloWorld.vue"));

new Vue({

}).$mount('#app');